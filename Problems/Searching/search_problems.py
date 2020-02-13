"""
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
"""
import re


def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest word in the provided dictionary. If there are more than
# one longest word, print them all.

file = open("dictionary.txt")
my_list = []
x = 0
longest_word = 0

for line in file:
    word = line.strip().upper()
    my_list.append(word)
print(my_list)

for word in my_list:
    if len(word[x]) >= longest_word:
        longest_word = len(word[x])
        x += 1
    else:
        x += 1
print(longest_word)

# 2.  (8pts) Write code which finds the total word count AND average word length in "AliceInWonderLand.txt"


# 3.  (3pts) How many times does the name Alice appear in Alice in Wonderland?


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"


# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
