from validation import check_validity, fix_input

def modify_solution_word(hint, solution, string):
    
    while True: 
            if (len(hint) == 5):
                break
            else:
                print("Hint should be 5 letters long!")
                hint = input("Type known letters:").upper()

    valid = check_validity(hint, string)

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

def add_yellows(lst, string, hint):
    
    while True: 
        if (len(hint) == 5):
            break
        else:
            print("Hint should be 5 letters long!")
            hint = input("Yellow letters in word:")

    valid = check_validity(hint, string)

    if(not valid): hint = fix_input(hint)

    for i in range(len(hint)):
        if(hint[i] == "*"):
            pass
        else:
            pair = (hint[i], i)
            if pair not in lst:
                lst.append(pair)

def filter_by_greens(solution, result_list):

    temp_list = []

    valid_characters = 0
    for char in solution:
        if char != "*":
            valid_characters += 1
    
    for word in result_list:
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

def filter_by_gray_letters(gray_list, result_list):

    temp_list = []

    print("Type the gray letters:")
    input_grays = input().split()
    for char in input_grays:
        if char not in gray_list:
            gray_list.append(char)

    gray_chars = len(gray_list)

    for word in result_list:
        remaining_chars = gray_chars
        for char in gray_list:
            if char not in word:
                remaining_chars -= 1
        if(remaining_chars == 0):
            temp_list.append(word)

    return temp_list   