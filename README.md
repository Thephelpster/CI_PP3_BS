# Star Trek Battleship Game

Developer : Jamie Phelps

[Live Webpage]

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
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    4. [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
6. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Features](#future-features)
7. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Mock up](#mock-up)
    5. [Performance](#performance)
    6. [Device testing](#performing-tests-on-various-devices)
    7. [Browser Compatibility](#browser-compatability)
    8. [Testing User Stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

# Project Description
This is the classic Battleship game that i have given a Star Trek feel to. Players can play as Starfleet as they try to attack Klingon ships.


# Project Goals
* Play a game of battleships against the computer.
* Use different sized board to change difficulty.
* Learn how to play Battleships.

## User Goals
* To play as many games of Battleships as I want.
* To have a clear game space to see how the board looks.

## Site Owner Goals
* For players to enjoy a game of battleships as many times as they want.
* To leave the player witha good feeling after they've played the game.


# User Experience

## Target Audience
* Battleship game fans.
* Star Trek fans.
* Anyone who wants a fun little game to play.

## User Requirements and Expectations


## User Stories
### First Time User
1. As a first time user, I want to be able to play a game of Battleships.
2. As a first time user, I want to be able to learn the rules of Battleships.
3. As a first time user, I want to see a nice design to the game.

### Returning User
4. As a returning user, I want to be able to change the size of the board for an extra challenge.
5. As a returning user, I want to be able to easily be able to see what move I'm on.

### Website Owner
6. As the game desginer I want people to have a good time playing the game.
7. As the game desginer I want people to be able to restart the game as much as they want.


# Design
## Design Choices
When designing the game I wanted to give they player something a bit nicer to look at than just the code repeated over and over again. This is why i added the logo in and why it appeared consistantly throughout the game.

## Flowchart
The flowchart shows the structure of the program.


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
* os - used to clear the terminal.
* random - used to give a random board each play through.
* sys and time - used to add a typing effect to the rules and greeting.

# Features
## Existing Features
### Logo

### Greeting

### Rules

### Board Size Choice

### In-Game Messages


## Future Features
* Score loging system
* A login function

# Validation and Testing
I have put the python code through PEP8 in the workspace where I wrote the code as the pep8online.com website was down.

No issues where flagged up apart from the spacing in the logo that make up the words 'BattleShips'.

To test the game ran as i expected it to, I played through it multiple times both playing as is expected and trying to get it not to work.


## Testing user stories

1. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|




## Bugs
| **Bug** | **Fix** |
| ----------- | ----------- |


# Deployment
## GitHub
The website was deployed using GitHub Pages by following these steps:
1. In the GitHub repository navigate to the Settings tab
2. On the left hand menu select Pages
3. For the source select Branch: main
4. Once saved, GitHub will refresh and your website will be publishd from GitHub repository
5. The link to your published website will appear: "Your site is published at https://thephelpster.github.io/CI_PP2_RPSLS/"

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
* Stack Over FLow - for the slow typing function basics.
https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing

* Youtube - video for the starting point for my Battleship game.
https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=390s

* Copy Assignment - helped with starting point as well.
https://copyassignment.com/battleship-game-code-in-python/

# Acknowledgements

I'd like to thank these people who gave me all the help and support I needed to finish and make this project look as good as it does.

* Mo Shami, my mentor, for all the guidance, help and keeping me from giving up when the code wasn't working out the way I wanted.

* Kate for being my rock when I was struggling to keep going with the course and keeping me sane.













![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Thephelpster,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

resources
https://www.folkstalk.com/tech/how-to-make-a-typing-effect-in-python-with-code-examples/
https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console