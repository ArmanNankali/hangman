
import random 

word_list = ["kiwi", "pomegranite", "mango", "nectarine", "apple"]
word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please guess a single letter")
        if guess.isalpha():
            break
        else:
            print(f"{guess} is an nvalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
