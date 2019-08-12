import random
import time

"""
This is a slightly changed version of hangman from the book Invent your own Computer Games with Python,
by Al Sweigart. I did a few modifications like adding a flag with colours, deleting a word from the list
so it wouldn't repeat and adding a wins and loses counts at the end of the game.
"""

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    0   |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\\  |
        |
       ===''','''       
    +---+
    0   |
   /|\\  |
   /    |
       ===''','''       
    +---+
    0   |
   /|\\  |
   / \\  |
       ===''']

# The usa flag, with the colour code
flag = ['''
+-----------+
|\033[1;37;44m*.* \033[1;31;49m#######\033[1;39;49m|
|\033[1;37;44m*.* \033[1;31;49m#######\033[1;39;49m|
|\033[1;31;49m###########\033[1;39;49m|
+-----------+
            |
            |
            |
           ===''']

words = ['alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

def get_random_word(word_list):
    #This function return a random string from the passed list of strings.
    word_index = random.randint(0, len(word_list) -1)
    return word_list[word_index]

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('Missed letters:', end='')
    for letter in missed_letters:
        print(letter, end='')
    print()
    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end='')
    print()

def get_guess(already_guessed):
    #Returns the letter the player entered. This functions makes sure the player entered a single letter and not something else.
    while True:
        print("Guess a letter:")
        guess = input(">").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You already guessed that letter. Try again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    #This function returns True if the player wants to play again; otherwise it returns False.
    print("Would you like to play again?")
    return input(">").lower().startswith('y')

print("This is H A N G M A N")
time.sleep(2)
print(flag[0])
time.sleep(1)
print("       US STATES")
time.sleep(2)
print("LET'S PLAY!")
time.sleep(2)

missed_letters = ''
correct_letters = '  ' #I added a space here for the words that have a space in the middle
secret_word = get_random_word(words)
words.remove(secret_word) #This removes the word from the list so it wouldn't repeat itself in the same game

game_is_done = False
win = 0
lose = 0

while True:
    display_board(missed_letters, correct_letters, secret_word)
    
    #Let the player enter a letter.
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess
        #Check if the player has won.
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            win += 1
            print("Yes! The state is " + secret_word + "! You won!")
            game_is_done = True
    else:
        missed_letters = missed_letters + guess
        #Check if the player has guessed too many times and lost.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            lose += 1
            display_board(missed_letters, correct_letters, secret_word)
            print("You have run out of guesses!\nAfter " + str(len(missed_letters)) + " missed guesses and " + str(len(correct_letters) - 1) + " of correct guesses, the word was " + secret_word)
            game_is_done = True

    #Ask the player if they want to play again (but only if the game is done).
    if game_is_done:
        if len(words) >= 1: #If you played less than all the options the game can continue
            if play_again():
                missed_letters = ''
                correct_letters = '  '
                game_is_done = False
                secret_word = get_random_word(words)
                words.remove(secret_word)
            else:
                print("Game over! Wins: " + str(win) + " | Loses: " + str(lose))
                break                
                
        else: #If you played all the words in the list, the game is automatically over
            print("Game over! Wins: " + str(win) + " | Loses: " + str(lose))
            break
