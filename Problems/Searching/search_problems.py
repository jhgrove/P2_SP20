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
    if len(word) >= longest_word:
        longest_word = len(word)
    x += 1
print(longest_word)


# 2.  (8pts) Write code which finds the total word count AND average word length in "AliceInWonderLand.txt"
file2 = open("../Searching/AliceInWonderLand.txt")
my_list2 = []

for line2 in file2:
    line2 = line2.strip().upper()
    words2 = split_line(line2)
    for word2 in words2:
        my_list2.append(word2)
print("Total Word Count:", len(my_list2), "words")

total_length = 0
for i in my_list2:
    word_len = len(i)
    total_length += word_len

print("Average Word Length:", total_length // len(my_list2), "letters")


# 3.  (3pts) How many times does the name Alice appear in Alice in Wonderland?
num_of_alice = 0
for i in my_list2:
    if i == "ALICE":
        num_of_alice += 1
print("Alice Found:", num_of_alice, "times")


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_list = []

for i in my_list2:
    if len(i) == 7:
        seven_list.append(i)

appearances = 0
seven_word = 0

for n in seven_list:
    if seven_list.count(n) > appearances:
        appearances = seven_list.count(n)
        seven_word = n.lower()

print("Most Common Seven Letter Word:", seven_word.capitalize())


# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
