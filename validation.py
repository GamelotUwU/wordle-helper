def check_validity(hint, string):

    valid = True

    for char in hint:
        if char not in string:
            valid = False
            break
    return valid

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
