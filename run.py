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

def display_rules():
#Explains game rules
    for game_rule in game_rules:
        print(f"{Fore.GREEN+Style.BRIGHT}{game_rule}")
        
def clear_screen():
#Clears the screen
    os.system("clear")



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
            display_rules() 
            input("Enter to return to Menu \n")
            print("\n")
            clear_screen()
            return game_start()




def main():
    """
    Runs all program functions used for the Game
    """
    game_welcome()
    game_start()
    
main()