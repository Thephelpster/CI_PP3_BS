# Star Trek Battleship Game

![logo2](./assets/readme-images/game-logo2.png)

Developer : Jamie Phelps.

[Live Webpage](https://ci-pp3-bs-thephelpster.herokuapp.com/)

# Table of Content

1. [Project Description](#project-description)
2. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requrements-and-expectations)
    3. [User Stories](#user-stories)
4. [Design](#design)
    1. [Design Choices](#design-choices)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
6. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Features](#future-features)
7. [Testing](#validation)
    1. [Device testing](#performing-tests-on-various-devices)
    2. [Browser Compatibility](#browser-compatability)
    3. [Testing User Stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

# Project Description
This is like the classic Battleship game with a Star Trek twist. Players can play as a Starfleet Captain as they defend against a Klingon attack.


# Project Goals
* Play a game of Battleships against the computer,
* Use different sized boards to change the difficulty level,
* Learn how to play Battleships.

## User Goals
* To play as many games of Battleships as I want,
* To have a clear game space to see how the board looks.

## Site Owner Goals
* For players to enjoy a game of Battleships as many times as they want,
* To leave the player with a good feeling after they've played the game.


# User Experience

## Target Audience
* Battleship game fans,
* Star Trek fans,
* Anyone who wants a fun little game to play.

## User Requirements and Expectations


## User Stories
### First Time User
1. As a first time user, I want to be able to play a game of Battleships,
2. As a first time user, I want to be able to learn the rules of Battleships,
3. As a first time user, I want to see a nice design to the game.

### Returning User
4. As a returning user, I want to be able to change the size of the board for an extra challenge,
5. As a returning user, I want to be able to easily see what move I'm on.

### Website Owner
6. As the game designer, I want people to have a good time playing the game,
7. As the game designer, I want people to be able to replay the game as much as they want.


# Design
## Design Choices
When designing the game I wanted to give the player something a bit nicer to look at than just the code repeated over and over again. This is why I added the logo in and why it appears consistantly throughout the game.

## Flowchart
The flowchart shows the structure of the program.

<details>
<summary>Flowchart</summary>
<br>
<img src="./assets/readme-images/flowchart.drawio.png" alt="Flowchart">
</details>

# Technologies Used
## Languages
* Python

## Frameworks & Tools
* Git
* GitHub
* GitPod
* PEP8
* Heroku
* Diagrams.net

## Python Libraries
* os - used to clear the terminal,
* random - used to give a random board each play through,
* sys and time - used to add a typing effect to the rules and greeting.

# Features
## Existing Features
### Playable Game
* The most important feature of this battleship game is that it's a game that anyone can play and have fun.

User Stories covered: 1, 6

### Logo
* The logo appears at the top of the game everytime you start it.

User stories covered: 3

<details>
<summary>Logo</summary>
<br>
<img src="./assets/readme-images/game-logo.png" alt="Logo">
</details>

### Clear Function
* The clear function allows the game to clear the console after every move, keeping the view clear and easy to see where you are in the game.

User stories covered: 5

### Slow Print Function
* The slow print function makes it look like someone is typing out the greeting and rules.

User stories covered: 3

<details>
<summary>Slowprint</summary>
<br>
<img src="./assets/readme-images/slow-print.png" alt="Slowprint">
</details>

### Greeting
* The greeting welcomes the player to the game and explains what's happening.

User stories covered: 3

<details>
<summary>Greeting</summary>
<br>
<img src="./assets/readme-images/greeting.png" alt="Greeting">
</details>

### Rules
* The rules explain how to play battleships.

User stories covered: 2

<details>
<summary>Rules</summary>
<br>
<img src="./assets/readme-images/rules.png" alt="Rules">
</details>

### Board Size Choice
* The board size choice allows the player to choose what size board they'll play the game on.

User stories covered: 3, 4

<details>
<summary>Size-Choice</summary>
<br>
<img src="./assets/readme-images/size-choice.png" alt="Size-Choice">
</details>

### In-Game Messages
* The in-game messages give the player feedback on how the game is going and what they need to do next.

User stories covered: 3

<details>
<summary>Messages</summary>
<br>
<img src="./assets/readme-images/game-messages.png" alt="Messages">
</details>

### Restart Function
* Last function added to the game was the ablitly to restart the game when finished or to exit the game.

User stories covered: 7

<details>
<summary>Restart</summary>
<br>
<img src="./assets/readme-images/restart.png" alt="Restart">
</details>

## Future Features
* Score loging system
* A login function


# Validation and Testing
I have put the python code through PEP8 in the workspace where I wrote the code as the pep8online.com website was down.

No issues where flagged up apart from the spacing in the logo that make up the words 'BattleShips'.

To test the game ran as expected, I played through it multiple times both as intended and trying to get it to not work to see if there were any issues that needed fixing. 


## Testing user stories

1. As a first time user, I want to be able to play a game of Battleships.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game | Play the game | Enjoy playing battleships | Enjoyed playing battleships |

2. As a first time user, I want to be able to learn the rules of Battleships.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game rules | See the rules appear | Read the rules | Learn the rules |

3. As a first time user, I want to see a nice design to the game.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Logo, Slowprint, Greeting, Board Size, Messages | See all the designs | Enjoy the game | Enjoyed the game |

4. As a returning user, I want to be able to change the size of the board for an extra challenge.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Board size | Change the size of the game board | Choose multiple sizes to play on | Play on multiple size boards |

5. As a returning user, I want to be able to easily see what move I'm on.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Clear function | Clear the console automatically | Clear the console to see the game better | Clears console to see the game better |

6. As the game designer I want people to have a good time playing the game.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Play the game | Play the game | Enjoy gameplay | Enjoy playing the game |

7. As the game designer, I want people to be able to replay the game as much as they want.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Restart function | Player can replay the game when finished | The game can either exit or restart | The game restarts or exits |

## Bugs
| **Bug** | **Fix** |
| ----------- | ----------- |
| Spacing error when played in Heroku | Added spaces to the front of the print()s |
| Board printed Y axis 2x as much as it should | Code error where it's iterated through the list twice |
| Various run issues | Indentation checked and corrected |
| Code layout errors | Making sure that each def had two spaces above |

### Unfixed bugs
The console doesn't clear the logo when running on Heroku, not sure why this is but it clears as it should in the console in GitPod.

# Deployment
## Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "ci-pp3-bs-thephelpster") and choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up our Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
9. Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.


## GitHub
The website was deployed using GitHub Pages by following these steps:
1. In the GitHub repository navigate to the Settings tab
2. On the left hand menu select Pages
3. For the source select Branch: main
4. Once saved, GitHub will refresh and your website will be publishd from GitHub repository

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner

### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone
# Credits

## Content
All referances to Star Trek came from the TV show.

## Code and Design
* Stack Over Flow - for the slow typing function basics.
https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing

* Youtube - video for the starting point for my Battleship game.
https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=390s

* Copy Assignment - helped with starting point as well.
https://copyassignment.com/battleship-game-code-in-python/

# Acknowledgements

I'd like to thank these people who gave me all the help and support I needed to finish and make this project look as good as it does.

* Mo Shami, my mentor, for all the guidance, help and keeping me from giving up when the code wasn't working out the way I wanted.

* Kate for being my rock when I was struggling to keep going with the course and keeping me sane.