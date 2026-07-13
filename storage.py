def initiate_answer_list():

    with open("Wordle_words_list.txt", "r") as textfile:
        wordlist = textfile.read().splitlines("\n")

    return wordlist

def update_solutions_file(solutions):

    with open("Result_words.txt", "w") as solutions_file:
        for word in solutions:
            solutions_file.write(word)