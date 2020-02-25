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

for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if not dictionary_list.__contains__(word):
            print(word)
file.close()
# add steps 13 and 14

print("\n--- Binary Search ---")
alice_file = open("AliceInWonderLand200.txt")
file = open("dictionary.txt")

for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        key = word
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False

        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if dictionary_list[middle_pos] < key:
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > key:
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print(key)

file.close()
