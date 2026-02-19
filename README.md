# Python-Group-Projects
Final group Python projects: Dice Rolling Simulator, Guess The Number, Personal Budget Tracker, Grid Based Exploration, and Hangman Game, showcasing fundamental coding and problem-solving skills.
This repository contains five Python projects completed as part of our group assignment:

## 1. Dice Rolling Simulator
A simple program that simulates rolling a dice and tells the user the random number obtained between 1 and 6.

**Key points:**
- Developed in Python using PyCharm
- Uses a while loop to keep asking the user if they want to roll again
- Implements string handling (using .upper()) to prevent errors when users enter lowercase letters

## 2. Guess The Number
A game where the computer generates a random integer between 1 and 26, and the user has to guess the correct number.

**Key points:**
- Developed in Python using PyCharm
- Provides responsive feedback letting the user know if their guess is "too high" or "too low"
- Uses a while loop that keeps running until the user guesses correctly
- Handles inputs that are outside the specified 1-26 range

## 3. Personal Budget Tracker
A personal budget tracker that helps users input a monthly budget and record several expense amounts.

**Key points:**
- Developed in Python using PyCharm
- Uses a list to store expense data and a for loop to collect input repeatedly
- Automatically calculates the total spent, average expense, and highest expense using built-in functions 
  (sum(), len(), max())
- Compares total spending to the budget and displays the result (under budget, exactly on budget, or over   
  budget)

## 4. Grid Based Exploration
A text-based exploration game where the player navigates a small map represented by a 3x3 grid of connected rooms.

**Key points:**
- Developed in Python using VS Code
- Players navigate the map by typing directional inputs (north, south, east, west)
- Uses 2D lists to store unique room names and descriptions
- Tracks the player's coordinates and prevents movement outside the map boundaries ("walls")

## 5. Hangman Game
An adaptation of the classic word-guessing game where the computer randomly selects a secret word and the user guesses it letter by letter.

**Key points:**
- Developed in Python using PyCharm
- Uses the random.choice module to select a word from a predefined list
- Displays underscores for hidden letters and reveals them upon correct guesses
- Tracks a limit of 6 incorrect attempts and warns the user if they enter invalid input (not in the alphabet 
  or already guessed)

## Files
- `Dice Rolling Simulator/` → Python code for Dice Rolling Simulator
- `Guess The Number/` → Python code for Guess The Number
- `Personal Budget Tracker/` → Python code for Personal Budget Tracker
- `Grid Based Exploration/` → Python code for Grid Based Exploration
- `Hangman Game/` → Python code for Hangman Game

## Skills Practiced
- Python programming
- Debugging and code improvement
- User input validation and handling text interactions
- Data structure management like Lists, Strings, and 2D lists
- Teamwork

## How to Run
1. Open the respective `.py` file in Python or an IDE (e.g., PyCharm, VS Code)  
2. Run the program  
3. Follow the prompts in the GUI to interact with the project

