import random
import os
import colorama
from colorama import Fore, Style
from words import easy_words, difficult_words
from constants import hangman_stages
from constants import logo
from constants import game_over
from constants import you_win
from constants import rules
from constants import menu

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
            break

def rules():
#Explains game rules
    for game_rules in rules:
        print(f"{Fore.GREEN+Style.BRIGHT}{game_rules}")


def game_start():
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




def main():
    """
    Runs all program functions used for the Game
    """
    game_welcome()
    game_start()
    
main()