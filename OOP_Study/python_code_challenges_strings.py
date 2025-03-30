# Challenge 1.
# Count Letters
# Count the of uniqie letters that appaear in a string. New letters to be counted, dupiates to be ignroed.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    unique_letters = []
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return len(unique_letters)

