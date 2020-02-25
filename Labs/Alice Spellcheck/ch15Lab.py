"""
James Grove
Alice Spellcheck
"""

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dict_file = open("dictionary.txt")
dictionary_list = []
for line in dict_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)
print(dictionary_list)
dict_file.close()

# LINEAR SEARCH
print("\n--- Linear Search ---")
alice_file = open("AliceInWonderLand200.txt")
line_number = 0
for line in alice_file:
    line_number += 1
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        found = False
        there = 0
        while not found:
            for i in dictionary_list:
                if i == word:
                    there += 1
            if there == 0:
                print(word, "on line", line_number)
            found = True
alice_file.close()

# BINARY SEARCH
print("\n--- Binary Search ---")
alice_file = open("AliceInWonderLand200.txt")
line_number = 0

for line in alice_file:
    line_number += 1
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False

        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if dictionary_list[middle_pos] < word:
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word:
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print(word, "on line", line_number)
alice_file.close()

# Challenge: Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
print("\n--- Challenge ---")
alice_file = open("AliceInWonderLand.txt")
alice_list = []
line_number = 0

for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)
alice_list.sort()

looking_file = open("AliceThroughTheLookingGlass.txt")

for line in looking_file:
    line_number += 1
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        lower_bound = 0
        upper_bound = len(alice_list) - 1
        found = False

        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if alice_list[middle_pos] < word:
                lower_bound = middle_pos + 1
            elif alice_list[middle_pos] > word:
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print(word, "on line", line_number)
alice_file.close()
