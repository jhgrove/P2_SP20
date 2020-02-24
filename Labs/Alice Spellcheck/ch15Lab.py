"""
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
"""

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.

file = open("dictionary.txt")
dictionary_list = []

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)
print(dictionary_list)

file.close()

print("\n--- Linear Search ---")
alice_file = open("AliceInWonderLand200.txt")
alice_list = []
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)
print(alice_list)


# Using a linear search, check the current word against the words in the dictionary.
# The linear search is just a few lines long.
# When comparing to the word to the other words in the dictionary, convert the word to uppercase.
# In your while loop just use word.upper() instead of word for the key.
# This linear search will exist inside the for loop created in the prior step.
# We are looping through each word in the dictionary, looking for the current word in the line that we just read in.
