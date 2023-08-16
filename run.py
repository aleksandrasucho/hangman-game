import random
import os
import colorama
import simple_term_menu
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
from words import easy_words, difficult_words
from constants import hangman_stages
from constants import LOGO
from constants import game_over
from constants import you_win

colorama.init(autoreset=True)

def game_welcome ():
    """
    Game Logo from patorjk.com
    Welcomes the user and asks for the name
    """
    for logo in LOGO:
        print(f"{Fore.GREEN+Style.BRIGHT}{logo}")



def main():
    """
    Runs all program functions used for the Game
    """
    game_welcome()
    
    
main()