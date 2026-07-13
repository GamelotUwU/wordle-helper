possible_solutions = []
solution = "*****"
yellow_letters = []
gray_letters_list = []
allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*"

def fix_input(hint):

    valid_input = ""

    for char in hint:
        if (char.isalpha()):
            valid_input += char
        else:
            if(char == "*"):
                valid_input += char
            else:
                char = "*"
                valid_input += char
    return valid_input

def check_validity(hint):

    valid = True

    for char in hint:
        if char not in allowed:
            valid = False
            break
    return valid

def initiate_answer_list():

    with open("Wordle_words_list.txt", "r") as textfile:
        wordlist = textfile.read().splitlines("\n")

    return wordlist

def filter_by_greens(solution):

    temp_list = []

    valid_characters = 0
    for char in solution:
        if char != "*":
            valid_characters += 1
    
    for word in possible_solutions:
        matching_chars = valid_characters
        for i in range(len(solution)):
            if solution[i] == "*":
                pass
            elif word[i] == solution[i]:
                matching_chars -= 1

        if(matching_chars == 0):
            temp_list.append(word)
                
    print(f"List size:{len(temp_list)}")

    return temp_list

def filter_by_yellows(word_lst,yellow_lst):

    temp_list = []
    yellows_needed = len(yellow_lst)

    for word in word_lst:
        remaining_chars = yellows_needed
        for ch,position in yellow_lst:
            if ch in word and ch != word[position]:
                remaining_chars -= 1
        if(remaining_chars == 0):
            temp_list.append(word)

    
    return temp_list

def modify_solution_word(hint, solution):
    
    while True: 
            if (len(hint) == 5):
                break
            else:
                print("Hint should be 5 letters long!")
                hint = input("Type known letters:")

    valid = check_validity(hint)

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

def filter_by_gray_letters():

    temp_list = []

    print("Type the gray letters:")
    input_grays = input().split()
    for char in input_grays:
        if char not in gray_letters_list:
            gray_letters_list.append(char)

    gray_chars = len(gray_letters_list)

    for word in possible_solutions:
        remaining_chars = gray_chars
        for char in gray_letters_list:
            if char not in word:
                remaining_chars -= 1
        if(remaining_chars == 0):
            temp_list.append(word)

    return temp_list                  

def update_solutions_file(solutions):

    with open("Result_words.txt", "w") as solutions_file:
        for word in solutions:
            solutions_file.write(word)

def add_yellows(lst):
    hint = input("Yellow letters:").upper()

    while True: 
        if (len(hint) == 5):
            break
        else:
            print("Hint should be 5 letters long!")
            hint = input("Yellow letters in word:")

    valid = check_validity(hint)

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
        possible_solutions = filter_by_greens(solution) 
        update_solutions_file(possible_solutions)

    elif option == "2":
            
            add_yellows(yellow_letters)
            possible_solutions = filter_by_yellows(possible_solutions,yellow_letters)
            update_solutions_file(possible_solutions)

    elif option == "3":
            possible_solutions = filter_by_gray_letters()
            update_solutions_file(possible_solutions)
    
    elif option == "4":
        print("Are you sure you want to reset the helper?")
        option = input("Y - Yes      N - No\n\n")

        if(option.upper() == "Y"):
            solution = reset(possible_solutions,yellow_letters,gray_letters_list)






          

   
