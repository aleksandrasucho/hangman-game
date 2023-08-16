"""
Stores all the things to be used in the game
Game Logo, Welcome,
Game Levels Options, Game Rules and Hangman Stages
"""

#Hangman Stages
hangman_stages = [
     # Initial empty state
    '''
     +---+
         |
         |
         |
        ===
    ''',
    # Head
    '''
     +---+
     O   |
         |
         |
        ===
    ''',
     # Head and torso
    '''
     +---+
     O   |
     |   |
         |
        ===
    ''',
     # Head, torso, and one arm
    '''
     +---+
     O   |
    /|   |
         |
        ===
    ''',
     # Head, torso, and both arms
    '''
     +---+
     O   |
    /|\  |
         |
        ===
    ''',
    # Head, torso, both arms, and one leg
    '''
     +---+
     O   |
    /|\  |
    /    |
        ===
    ''',
     # Final state: head, torso, both arms, and both legs
    '''
     +---+
     O   |
    /|\  |
    / \  |
        ===
    '''
]

#Logo from  patorjk.com and a welcome to the player
logo = [
    """
 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
""",
"Welcome to Hangman!",
"May your guesses be as clever as a detective's hunch."
]

#Game Over announcement
game_over = [
    """
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
    """
]

#You Win announcement
you_win = [
    """
____    ____  ______    __    __     ____    __    ____  __  .__   __.  __  
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__| 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__) 
                                                                            
    """
]