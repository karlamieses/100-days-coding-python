import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_new_dictionary = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def nato_words():
    enter_name = input("Enter a word: ").upper()
    try:
        list_of_nato_words = [nato_new_dictionary[word] for word in enter_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_words()
    else:
        print(list_of_nato_words)


nato_words()