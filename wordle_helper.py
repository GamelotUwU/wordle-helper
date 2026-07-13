possible_solutions = []
solution = "*****"
yellow_letters = []
gray_letters_list = []
allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*"

from validation import check_validity, fix_input
from filters import filter_by_greens, filter_by_yellows, filter_by_gray_letters
from storage import initiate_answer_list, update_solutions_file

def modify_solution_word(hint, solution):
    
    while True: 
            if (len(hint) == 5):
                break
            else:
                print("Hint should be 5 letters long!")
                hint = input("Type known letters:")

    valid = check_validity(hint, allowed)

    if(not valid): hint = fix_input(hint)

    if solution == "*****":
        solution = hint

    word = ""
    
    for i in range(len(solution)):
        if solution[i] != "*":
            word += solution[i]
        elif solution[i] == "*" and hint[i] != "*":
            word += hint[i]
        else:
            word += "*"

    return word

def add_yellows(lst):
    hint = input("Yellow letters:").upper()

    while True: 
        if (len(hint) == 5):
            break
        else:
            print("Hint should be 5 letters long!")
            hint = input("Yellow letters in word:")

    valid = check_validity(hint, allowed)

    if(not valid): hint = fix_input(hint)

    for i in range(len(hint)):
        if(hint[i] == "*"):
            pass
        else:
            pair = (hint[i], i)
            if pair not in lst:
                lst.append(pair)

def show_yellows(lst):
    yellows = []
    for ch,position in lst:
        if ch not in yellows:
            yellows.append(ch)
    return yellows

def reset(wordlist,yellowlist,graylist):

    with open("Result_words.txt", "w") as resultfile:
        pass
    
    wordlist.clear()

    yellowlist.clear()

    graylist.clear()

    return "*****"


possible_solutions = initiate_answer_list()


while True:
    yellows = show_yellows(yellow_letters)
    print(f"\nCurrent hint: {solution}")
    print(f"Yellow letters:{(",").join(yellows)}") 
    print(f"Gray letters: {(",").join(gray_letters_list)}")
    print("")
    print("\n1.Green Letters:")
    print("2.Yellow letters")
    print("3.Gray letters")
    print("4.Reset\n")
    
    option = input()

    if option == "exit":
        break

    elif option == "1":
        hint = input("(Please use '*' for empty spots)\nType known letters:").upper()
        solution = modify_solution_word(hint, solution)
        possible_solutions = filter_by_greens(solution, possible_solutions)
        update_solutions_file(possible_solutions)

    elif option == "2":
            
            add_yellows(yellow_letters)
            possible_solutions = filter_by_yellows(possible_solutions,yellow_letters)
            update_solutions_file(possible_solutions)

    elif option == "3":
            possible_solutions = filter_by_gray_letters(gray_letters_list,possible_solutions)
            update_solutions_file(possible_solutions)
    
    elif option == "4":
        print("Are you sure you want to reset the helper?")
        option = input("Y - Yes      N - No\n\n")

        if(option.upper() == "Y"):
            solution = reset(possible_solutions,yellow_letters,gray_letters_list)






          

   
