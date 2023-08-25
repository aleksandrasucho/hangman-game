import os
import random
from colorama import Fore, Style, init
from words import easy_words, difficult_words
from constants import *
from game_variables import *

init(autoreset=True)


def game_welcome():
    """
    Game Logo from patorjk.com
    Welcomes the user and asks for the name
    """
    for line in logo:
        print(f"{Fore.CYAN+Style.BRIGHT}{line}")
    while True:
        name = input(f"{Fore.GREEN+Style.BRIGHT}What is your name?\n").capitalize()
        # Ensures that the user enters a name and this is not left blank
        if len(name) == 0:
            print(f"{Fore.RED+Style.BRIGHT}Your name must be letters only!")
            continue
        elif not name.isalpha():
            print(f"{Fore.RED+Style.BRIGHT}Your name must be letters only!")
            continue
        else:
            print(f'Hello, {name}')
            break

def display_rules():
#Explains game rules
    for game_rule in game_rules:
        print(f"{Fore.GREEN+Style.BRIGHT}{game_rule}")

def clear_screen():
#Clears the screen https://www.101computing.net/python-typing-text-effect/
    if os.name == "nt":
        os.system('cls')
    else: 
        os.system('clear')


def select_level():
    """Option of words difficulty"""
    for game_levels in game_level:
        print(f"{Fore.GREEN+Style.BRIGHT}{game_levels}")
    while True:
        option = input("\n").upper()
        if option == "E":
            return easy_words
        elif option == "D":
            return difficult_words
        else:
            print(f"{Fore.RED+Style.BRIGHT}Invalid option. Please choose 'E' for Easy or 'D' for Difficult.")
            

def random_word(difficulty_level):
    """Returns a random word based on selected difficulty,
        the words are contained in an imported list.
    """
    if difficulty_level == easy_words:
        return random.choice(easy_words)
    elif difficulty_level == difficult_words:
        return random.choice(difficult_words)
    else:
        return None
    

def hangman_lives(lives):
    """Displays Hangman stages"""
    for stage in hangman_stages[:lives+1]:
        print(stage)


def display_game_state(word_to_guess, guessed_letters):
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "
    print(f"Word to guess: {display_word}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    
def get_player_guess():
    guess = input("Guess a letter: ").lower()
    return guess

def game_start(name):
    """
    Starts the game off with options of:
    1. To see the game Rules
    2. To select level of words difficulty
    """
    for options in menu:
        print(f"{Fore.GREEN+Style.BRIGHT}{options}")
    start = False
    while not start:
        choice = input("\n")
        if choice == "1":
            display_rules() 
            input("Press Enter to return to Menu \n")
            print("\n")
            clear_screen()
            return game_start(name)
        elif choice == "2":
            selected_level = select_level()
            start = True
        else:
            print(f"{Fore.RED+Style.BRIGHT}Invalid option. Please choose 1 or 2")
    if start:
        play_game()

def play_game():
    selected_level = select_level()
    word_to_guess = random_word(selected_level)
    guessed_letters = []
    remaining_lives = MAX_INCORRECT_GUESSES
    
    while remaining_lives > 0:
        hangman_lives(MAX_INCORRECT_GUESSES - remaining_lives)
        display_game_state(word_to_guess, guessed_letters)
        print(f"Remaining lives: {remaining_lives}")
        guess = get_player_guess()

        if len(guess) != 1 or not guess.isalpha():
            print(f"{Fore.RED+Style.BRIGHT}Please enter a valid letter.")
        else:
            if guess in guessed_letters:
                print(f"{Fore.RED+Style.BRIGHT}You've already guessed that letter.")
            else:
                guessed_letters.append(guess)
                if guess in word_to_guess:
                    if all(letter in guessed_letters for letter in word_to_guess):
                        display_game_state(word_to_guess, guessed_letters)
                        display_you_win()
                        return True
                else:
                    remaining_lives -= 1
                    print(f"Incorrect guess! You have {remaining_lives} lives left.")

    display_game_over()
    return False


def display_game_over():
    for you_lose in game_over:
        print(f"{Fore.RED+Style.BRIGHT}{you_lose}")
    
    
def display_you_win():
    for you_won in you_win:
        print(f"{Fore.RED+Style.BRIGHT}{you_won}")
        

def play_again():
    play_again_input = input("Do you want to play again? (Y/N): ").lower()
    return play_again_input == "y"

def main():
    """Runs all program functions used for the Game"""
    name = game_welcome()
    
    while True:
        game_start(name)
        if not play_again():
            # Clear the terminal
            clear_screen()
            print(f"{Fore.GREEN+Style.BRIGHT}Thanks for playing the game!")
            break
        
    
main()