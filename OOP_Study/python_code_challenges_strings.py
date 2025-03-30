# Challenge 1.
# Count Letters
# Count the of uniqie letters that appaear in a string. New letters to be counted, duplicates to be ignored.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    unique_letters = []
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return len(unique_letters)

# print(unique_english_letters("mississippi"))

# Challenge 2.
# Count X
# Count the number of times a letter appears in a string.

def count_char_x(word, x):
  char_count = 0
  for letter in word:
    if letter == x:
      char_count += 1
  return char_count

# print(count_char_x("mississippi", "s"))

# Challenge 3.
# Count Multi X
# Create a function which accepts a string and a substring.
# Return the number of instances the substring appears in the string.

def count_multi_char_x(word, x):
    return word.count(x)

print(count_multi_char_x("mississippi", "iss"))