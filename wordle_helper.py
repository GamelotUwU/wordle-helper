possible_solutions = []
solution = "*****"
yellow_letters = []
gray_letters_list = []
allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*"

from filters import filter_by_greens, filter_by_yellows, filter_by_gray_letters, modify_solution_word, add_yellows
from storage import initiate_answer_list, update_solutions_file

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
        solution = modify_solution_word(hint, solution, allowed)
        possible_solutions = filter_by_greens(solution, possible_solutions)
        update_solutions_file(possible_solutions)

    elif option == "2":
            hint = input("Yellow letters:").upper()
            add_yellows(yellow_letters, allowed, hint)
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






          

   
