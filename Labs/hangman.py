"""
James Grove - 2020
Hangman Game
"""

import random

# Images of Different Stages of Gallows
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

# List of Possible Hidden Words
word_list = [
    "ABOOD", "AUSTIN", "AYMAR", "BANKS", "BARR", "BIGELOW", "BRANDON", "BRUNO", "CASTALDI", "CHILDREY",
    "COLLINS", "CONLON", "DAVIS", "DENIEN", "DONOHUE", "DRUGER", "ELLIOTT", "GIBSON", "GREENSTONE", "IACONIANNI",
    "LAUFER", "LEE", "LESAK", "LESINSKI", "LEVINE", "MAHANY", "MARKER", "OLT", "POPE", "PRITIKIN",
    "RIFF", "SABIR", "SCHUPP", "SHEPARD", "STARKS", "TYLER", "VILLAGOMEZ", "WEBSTER", "WILSON", "ZAREMBA",
    "ZELLER", "ZHANG"
]

done = False
my_word = word_list.pop(random.randrange(len(word_list)))  # Choose a random word in the list
number_of_letters = len(my_word)  # Count the number of letters in the word
wrong_guesses = 0  # Player starts with no incorrect letter guesses
used_letters = []  # Player starts with no used letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letters able to be used

print("\nWelcome to Hangman - Teachers Edition!")  # Welcome Message
print("This teacher's name has", number_of_letters, "letters.")  # Number of letters in the word

while not done:
    print(gallows[wrong_guesses])  # Show the stage of the gallows
    for letter in my_word:
        if letter in used_letters:
            print(letter, end=" ")  # If the letter has been used, show the letter
        else:
            print("_", end=" ")  # If the letter has not been used, show a blank
    print()

    if number_of_letters > 0:  # If there are any letters left to be found in the word
        print("\nUsed Letters:", used_letters)  # Show the letters that the player has guessed
        chosen_letter = input("Pick a letter: ").upper()  # Take a letter guess from the player
        number_of_letters = number_of_letters - my_word.count(chosen_letter)  # Number of letters left to be found

        if chosen_letter in used_letters:  # If the player already guessed that letter
            number_of_letters = number_of_letters + my_word.count(chosen_letter)
            print("\nYou already guessed that letter! Choose a different letter.")

        elif chosen_letter not in letters:  # If the player chooses a non-letter character
            print("\nThat's not a letter. Please choose a letter.")

        elif chosen_letter in my_word:  # If the player guesses a letter correctly
            used_letters.append(chosen_letter)  # Add that letter to the list of used letters
            print("\nNice job! The letter", chosen_letter, "is in your word!")

        elif len(chosen_letter) != 1:  # If the player guesses multiple letters at once
            print("\nYou must guess one letter at a time!")

        elif chosen_letter not in my_word:  # If the player incorrectly guesses a letter
            used_letters.append(chosen_letter)  # Add that letter to the list of used letters
            if wrong_guesses < 6:  # If the player still has lives left
                wrong_guesses += 1  # Player loses a life
                print("\nSorry,", chosen_letter, "is not in your word.")
            if wrong_guesses >= 6:  # If the player is out of lives
                print("YOU LOSE. The word was " + my_word + ". Thanks for Playing!")  # Player loses
                done = True  # Game is over

    elif number_of_letters == 0:  # If there are no letters left to be found in the word
        print("\nYOU WIN! The word was", my_word + ". Thanks for Playing!")  # Player wins
        done = True  # Game is over
