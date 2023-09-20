# Aicore Hangman project - Arman Nankali

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Table of Contents
- Project Description
- Installation Instructions
- Usage Instructions
- File Structure
- License Information

## Project description:
This project aims to create a game of hangman based on Python code, leveraging GitHub to manage and document iterations of the code. The game has been implemented as a Python class, which makes the code more organized and easier to manage. The class includes methods for checking guesses, asking for input, and initializing a new game.

## Installation instructions
To install this game, clone the repository to your local machine using Git.

## Usage instructions
In the updated version of the game, the Hangman game is implemented as a Python class. This allows for more organized code and makes it easier to manage the game state. Here’s how to use it:

Initialization: Now the function called play_game that takes word_list as a parameter and will run all the code to run the game. An instance of the Hangman game is created with the line game = Hangman(). This initializes a new game with a random word selected from the provided word list and sets the number of lives to 5.

Guessing a letter: game.ask_for_input() will start the game. This method prompts the user to guess a single letter. The input is automatically checked for validity (being a single letter of the alphabet). If the input is invalid, the user is prompted to try again.

Checking the guess: If the guessed letter is in the word, a message is printed to let the user know their guess was correct. The guessed letter replaces the corresponding underscore(s) in self.word_guessed. If the guessed letter is not in the word, the user loses a life and is informed about it.

Repeated guesses: If a user guesses a letter that they’ve already guessed before, they are asked to guess again.

Game status: After each guess, self.word_guessed is printed to show the current status of the word being guessed.


## File structure of the project

## License information

