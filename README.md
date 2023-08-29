<h1 align="center">Hangman Game - Project Portfolio 3</h1>

---

# *Hangman Game*

Hangman is a word-guessing game where players attempt to unravel a hidden word by suggesting individual letters. Incorrect guesses result in the gradual formation of a hangman figure, while correct guesses reveal the letters' positions. 

The site can be accessed by this [link](https://hang-man-game55-2e55bd9f26a2.herokuapp.com/)

---

## How to play:
1. Click this *[link](https://hang-man-game55-2e55bd9f26a2.herokuapp.com/)* or copy this text: `https://hang-man-game55-2e55bd9f26a2.herokuapp.com/` and paste it in your browser's address bar.
1. As soon as the page is loaded, click 'RUN PROGRAM'.
1. Introduce yourself to the program.
1. Learn the rules.
1. Select the difficulty of words to play the game. 
1. After selecting the difficulty level, the game begins.
1. A secret word will be chosen, and its letters are represented by blank spaces.
1. Start guessing letters one by one. Each correct letter guess reveals its position in the word.
1. Be cautious! Incorrect letter guesses cost you one life.
1. You win if you correctly guess all the letters in the word before running out of lives. The hidden word will be revealed, and you'll emerge victorious!
1. If you lose all 6 lives before guessing the word, the hangman is fully hanged, and the game ends.


## User Stories

### First Time Visitor Goals:

* As a First Time Visitor to the Hangman game, my primary objective is to understand the game's concept and rules. I want to familiarize myself with the idea that I need to guess a hidden word by suggesting individual letters, while also comprehending the consequences of incorrect guesses.
* As a First Time Visitor, I want to see how many attempts I have left when playing.
* As a First Time Visitor, I want to choose the difficulty level, so I can tailor the game to my skill level.
* As a First Time Visitor, I want feedback after each guess, so I can adjust my strategy.
* As a First Time Visitor, I want the option to play again, so I can improve my skills and have another shot at winning.

### Returning Visitor Goals:

* As a Returning Visitor, I want to challenge myself with a different difficulty level, so I can experience varying levels of gameplay.
* As a Returning Visitor, I want to easily find and access the "Rules" section, so I can refresh my memory if needed.
---

## Features
  
  - **When the program is loaded**

  The user can see a welcoming message and the polite question to enter the user's name:
  
  ![loading Program](documentation/features/feature-1-min.PNG)

   - **When the user types a name.**

  - Sends personal greetings and short instruction on the next step;
  
  - Shows the  menu with two options:

    1. Press 1 to Read the Hangman Rules

    1.  Press 2 to Select the difficulty to play the game

- The user must choose by pressing either 1 or 2, based on their preference.

![Menu Program](documentation/features/feature2-min.PNG)

- **When the user chose "Read the Hangman Rules"**

  The user will see the main rules of the game which are required to be followed.
  Below the rules, the user will find a message instructing them to press the "Enter" key if they wish to return to the main menu.

![Rules Program](documentation/features/feature-3-min.PNG)

   - **When the user chose "Select the difficulty to play the game"**

  The program will display the message:

  - "Select the level you wish to play at." 
  
  Along with the following menu:

  1. Press E for Easy words;

  1. Press D for Difficult words;


![Difficulty Program](documentation/features/feature4-min.PNG)

- The user must choose by pressing either E or D, based on their preferred difficulty level for playing the game.

- **When the user chose a difficulty**

  The main game screen provides all information regarding the users current game of hangman. This includes:
- Word to guess
- Remaining lives
- Guessed letters

![Game Program](documentation/features/feature5-min.PNG)

- **When the user guesses the wrong letter**

  If user guesses the wrong letter, a message will be displayed saying: 
  - "Incorrect guess! You have (number of lives left) lives left"

![Game Program](documentation/features/feature6-min.PNG)

- **When the user guesses the same letter as before**
    
    If user guessed the same letter as before, a message will be displayed saying: 
  - "(user name), You've already guessed that letter"
  
![Game Program](documentation/features/feature7-min.PNG)

- **When the user wins**
    If the user has successfully guessed all the letters correctly, a customized "You Win" message will be displayed. Underneath this message, the following question will be presented:
        
    - "Do you want to play again? (Y/N)"

  The user will have the option to choose by pressing either "Y" to indicate they want to play again, or "N" to indicate they want to end the game.

![Game Program](documentation/features/feature8-min.PNG)

- When the user chooses 'Y,' they will be directed to the main menu.

![Play Again Program](documentation/features/feature9-min.PNG)

- When the user chooses 'N,' they will be directed to the exit screen that will display the following message: "Thanks for playing the game! 

![Exit Program](documentation/features/feature10-min.PNG)

- **When the user loses**
    If the user hasn't guessed the word, a customized 'Game Over' message will be displayed. Underneath this message, the following question will be presented:
        
    - "Do you want to play again? (Y/N)"

  The user will have the option to choose by pressing either "Y" to indicate they want to play again, or "N" to indicate they want to end the game.

![Game Program](documentation/features/feature11-min.PNG)

---
## Technologies Used
### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random letter generation.
- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before running the program.

##### Third-party imports:

- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.
#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [GitHub](https://github.com/) was used to host the code of the website.

---
## Future Features
- I would like to implement leaderboard functionality (calculations etc).

## Bugs
-
---
## Testing
-
---
## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://hang-man-game55-2e55bd9f26a2.herokuapp.com/)
### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/aleksandrasucho/hangman-game).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/aleksandrasucho/hangman-game.git`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/new#https://github.com/aleksandrasucho/hangman-game)

 1. Install Python module dependencies:
    1. Navigate to the folder hangman-game by executing the command:
        - `cd hangman-game`
    1. Run the command pip install -r requirements.txt
        - `pip3 install -r requirements.txt`

**The app was deployed to Heroku**

### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/aleksandrasucho/hangman-game.git`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

      - ![New Heroku App](documentation/deployment/dep1-min.PNG)

 1. Go to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/dep2-min.PNG)

      - ![Deployment Method](documentation/deployment/dep3-min.PNG)

1. Link your GitHub account and connect the application to the repository you created.

      - ![Link GitHub account](documentation/deployment/link-to-github-min.PNG)

1. Go to the Settings tab:
  
      - ![Settings Tab](documentation/deployment/go-to-settings-min.PNG)

 1. Click "Add buildpack":

      - ![Add Buildpack](documentation/deployment/add-buildpacks-min.PNG)

  1. Add the Python and Node.js buildpacks in the following order:

      - ![Add Python and Node.js](documentation/deployment/add-python-nodejs-min.PNG)

  1. Click "Reveal Config Vars."

      - ![Reveal Config Vars](documentation/deployment/config-vars-min.PNG)

  1. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

  1. Go back to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/dep2-min.PNG)

  1. Click "Deploy Branch":

      - ![Deploy Branch](documentation/deployment/deploy-min.PNG)

      - Wait for the completion of the deployment.

      - ![Deploying Branch](documentation/deployment/wait-for-deploy-min.PNG)

  1. Click "Open app" to launch the application inside a web page.

      - ![View Button](documentation/deployment/view-game-min.PNG)

## Credits

- Color formatting: [Colorama](https://pypi.org/project/colorama/).
- List of words was made based on the [Randomlists](https://www.randomlists.com/random-words)

## Acknowledgments

- [Juliia Konovalova ](https://github.com/IuliiaKonovalova) was a great supporter. She guided me through the development of the project and helped me to learn a lot of new things by challenging me to do something new.
- [Code Institute](https://codeinstitute.net/) tutors and Slack community members for their support and help.

