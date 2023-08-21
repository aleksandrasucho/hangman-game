import random
import os
import colorama
from colorama import Fore, Style
from words import easy_words, difficult_words
from constants import hangman_stages
from constants import logo
from constants import game_over
from constants import you_win
from constants import game_rules
from constants import menu
from constants import game_level

colorama.init(autoreset=True)


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
            print(f"{Fore.RED+Style.BRIGHT}This is not a valid name!")
            continue
        elif not name.isalpha():
            print(f"{Fore.RED+Style.BRIGHT}Your name must be letters only")
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
    os.system("clear")

def select_level():
#Option of words difficulty
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
            input("Enter to return to Menu \n")
            print("\n")
            clear_screen()
            return game_start(name)
        elif choice == "2":
            selected_level = select_level()
            start = True
        else:
            print(f"{Fore.RED+Style.BRIGHT}Invalid option. Please choose 1 or 2")
            
        



def main():
    """Runs all program functions used for the Game"""
    name = game_welcome()
    game_start(name)
    
main()