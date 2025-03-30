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

# Challenge 4.
# Subsring Between 
# Creaea a function that that is able to extract a substring between two characters.
# The function should accept a string and two characters.

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start != -1 and end != -1:
    return word[start_ind + 1:end_ind] 
  return word

# print(substring_between_letters("apple", "p", "e"))

#Challlenge 5.
# X Length
# Create a function which returns Truo if every number in the sentence is greater than or equal to x.

def x_length_words(sentence, x):
  word_list = sentence.split(" ")
  for word in word_list:
    if len(word) < x:
      return False
    return True
  
# print(x_length_words("i like apples", 2))