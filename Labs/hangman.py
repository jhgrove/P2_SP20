"""
James Grove
Hangman Lab
"""

import random

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

done = False

word_list = ["JAMES", "HENRY", "GROVE"]
# my_word = word_list[random.randrange(3)]
my_word = "JAMES"
wrong_guesses = 0

letters = [chr(x) for x in range(65, 65 + 26)]
used_letters = []

'''
num_of_spaces = len(my_word)
for i in range(num_of_spaces):
    print("__ ", end="")
'''


def hangman():
    blank_1 = "__"
    blank_2 = "__"
    blank_3 = "__"
    blank_4 = "__"
    blank_5 = "__"
    print(
        blank_1, blank_2, blank_3, blank_4, blank_5
    )

    while not done:
        print(gallows[wrong_guesses])
        guess = input("\nGuess a Letter: ")
        for letter in my_word:
            if guess.upper() == letter:
                if guess.upper() == "A":
                    blank_2 = "A"
                used_letters.append(letter)
