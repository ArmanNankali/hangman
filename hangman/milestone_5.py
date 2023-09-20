# %%
import random 

word_list = ["kiwi", "pomegranite", "mango", "nectarine", "apple"]
word = random.choice(word_list)

class Hangman():
    def __init__(self, word_list = ["kiwi", "pomegranite", "mango", "nectarine", "apple"], num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = self.word_guessed.count("_")
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters = self.word_guessed.count("_")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            print(self.word_guessed)
            guess = input("Please guess a single letter")
            if guess.isalpha() == False:
                print(f"{guess} is an nvalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            game.num_letters == 0 and game.num_lives > 0
            print("Congratulations. You won the game!")
            break
        


play_game(word_list)
# %%
