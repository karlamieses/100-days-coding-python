import pandas


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_new_dictionary = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

enter_name = input("Enter a word: ").upper()

list_of_nato_words = [nato_new_dictionary[word] for word in enter_name]

print(list_of_nato_words)