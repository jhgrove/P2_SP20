# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1, 101)]
print(my_list)

# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20, 41) if x % 2 == 0]
print(my_list)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(1, 101)]
print(my_list)

# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_positives = [x for x in my_list if x > 0]
print(my_positives)

from Problems import number_list

my_number_list = number_list.num_list

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
print(my_number_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(my_number_list))

# Find and print the lowest number in num_list (1pt)
print(min(my_number_list))

# Find and print the average of num_list (2pts)
print(sum(my_number_list) / len(my_number_list))

# Remove the lowest number from num_list (2pt)
del my_number_list[my_number_list.index(min(my_number_list))]
print(my_number_list)

# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
top_ten = []
my_number_list.sort()
top_ten.append(my_number_list[-10:])
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
'''
from Problems import number_list
my_number_list = number_list.num_list
print(max(my_number_list, key=my_number_list.count))
'''

from Problems import number_list
my_number_list = number_list.num_list

appearances = 0
number = 0

for n in my_number_list:
    if my_number_list.count(n) > appearances:
        appearances = my_number_list.count(n)
        number = n

print(number)

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
# DOES NOT WORK!!!!
from Problems import number_list
my_number_list2 = number_list.num_list
for num in my_number_list2:
    num_of_primes = 0
    for i in range(2, num):
        if num % i == 0:
            del my_number_list2[my_number_list2.index(num)]
    print(my_number_list2)
    print(len(my_number_list2))

# Find the number of palindromes
# Hint: This may be easier to do with strings
num_of_palindromes = 0
for i in range(len(my_number_list)):
    possibilities = str(my_number_list[i])
    if possibilities[0] == possibilities[3] and possibilities[1] == possibilities[2]:
        num_of_palindromes += 1

print(num_of_palindromes)
