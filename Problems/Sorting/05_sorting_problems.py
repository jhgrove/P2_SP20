"""
James Grove
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py. The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
"""

# 1  Pop off the first item in the list and print it. It contains the column headers. (1pt)
from NBAStats import data
print(data.pop(0), "\n")

# 2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
num = 0
my_list = [[i[-1], i[2]] for i in data]
my_list.sort(reverse=True, key=lambda a: a[0])
for i in my_list[:10]:
    num += 1
    print(num, i[1], "had", i[0], "points.")
print()

# 3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
my_list2 = [i[-1] for i in data if i[2] == "Kobe Bryant"]
print("Kobe Bryant had", sum(my_list2), "career points.", "\n")

# 4  What player has the most 3point field goals in a single season. (3pts)
my_list3 = [[i[34], i[2]] for i in data]
my_list3.sort(reverse=True, key=lambda a: a[0])
print(my_list3[0][1], "made the most 3 pointers with", my_list3[0][0], "\n")

# 5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data. It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
my_list4 = [[i[25], i[2]] for i in data]
my_list4.sort(reverse=True, key=lambda a: a[0])
print(my_list4[0][1], "had the highest WS/48 season with", my_list4[0][0], "\n")

# 6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?" or "Who played the most games?"
# or "Who has the most combined blocks and steals?".
print("Who was the oldest player to make 250 three pointers in a season?")
my_list5 = [[i[4], i[34], i[2]] for i in data if i[34] >= 250]
my_list5.sort(reverse=True, key=lambda a: a[0])
print(my_list5[0][2], "made", my_list5[0][1], "threes at age", my_list5[0][0] + ".\n")

# 7  Big challenge, few points. Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage? Which had the best? (2pts)
my_list6 = [[i[-1], i[2], i[-10]] for i in data]
my_list6.sort(reverse=True, key=lambda a: a[0])
my_list6_2 = my_list6[:100]
my_list6_2.sort(reverse=True, key=lambda a: a[2])
print(my_list6_2[-1][1], "had the worst free throw percentage with", my_list6_2[-1][2])
print(my_list6_2[0][1], "had the best free throw percentage with", my_list6_2[0][2])
