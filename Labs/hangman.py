"""
James Grove
Hangman Lab
"""

import random

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

word_list = [
    "ABOOD", "AUSTIN", "AYMAR", "BANKS", "BARR", "BIGELOW", "BRANDON", "BRUNO", "CASTALDI", "CHILDREY",
    "COLLINS", "CONLON", "DAVIS", "DENIEN", "DONOHUE", "DRUGER", "ELLIOTT", "GIBSON", "GREENSTONE", "IACONIANNI",
    "LAUFER", "LEE", "LESAK", "LESINSKI", "LEVINE", "MAHANY", "MARKER", "OLT", "POPE", "PRITIKIN",
    "RIFF", "SABIR", "SCHUPP", "SHEPARD", "STARKS", "TYLER", "VILLAGOMEZ", "WEBSTER", "WILSON", "ZAREMBA",
    "ZELLER", "ZHANG"
]

done = False
my_word = word_list.pop(random.randrange(len(word_list)))
number_of_letters = len(my_word)
wrong_guesses = 0
used_letters = []
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\n" + my_word)

print("\nWelcome to Hangman - Teachers Edition!")
print("This teacher's name has", number_of_letters, "letters.")

while not done:
    print(gallows[wrong_guesses])
    for letter in my_word:
        if letter in used_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    if number_of_letters > 0:
        print("\nUsed Letters:", used_letters)
        chosen_letter = input("Pick a letter: ").upper()
        number_of_letters = number_of_letters - my_word.count(chosen_letter)

        if chosen_letter in used_letters:
            number_of_letters = number_of_letters + my_word.count(chosen_letter)
            print("\nYou already guessed that letter! Choose a different letter.")

        elif chosen_letter in my_word:
            used_letters.append(chosen_letter)
            print("\nNice job! The letter", chosen_letter, "is in your word!")

        elif len(chosen_letter) != 1:
            print("\nYou must guess one letter at a time!")

        elif chosen_letter not in my_word:
            used_letters.append(chosen_letter)
            if wrong_guesses < 6:
                wrong_guesses += 1
                print("\nSorry,", chosen_letter, "is not in your word.")
            if wrong_guesses >= 6:
                print("YOU LOSE. The word was " + my_word)
                done = True

        elif chosen_letter not in letters:
            print("\nThat's not a letter. Please choose a letter.")

    elif number_of_letters == 0:
        print("\nYOU WIN! The word was", my_word + ". Thanks for Playing!")
        done = True
