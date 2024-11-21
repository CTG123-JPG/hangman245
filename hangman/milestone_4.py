import random
from Milestone_2 import word_list
#The above code imports the necessary items for the code to run including the Word_list kept in another file for ease

class Hangman:# A class for the entire Hangman game
    def __init__(self, word_list, num_lives=5):# Defining each parameter within the function and ensuring the default number of lives is 5
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)  # selects a random word from the word_list
        self.word_guessed = ['_'] * len(self.word)  # the underscores represent each letter not guessed within the random word selected
        self.num_letters = len(self.word)  # The number of letters the user has to guess
        self.list_of_guesses = []  # An empty list so that the user's guesses have somewhere to go so we can tell them they have already tried a letter.

    def check_guess(self, guess): # a function to check weather the user's input is in the randomly selected word
        guess.lower() # makes all characters in the guess lower case so that the code can run smoothly
        if guess in self.word: # An if statement that prompts the user if they have guessed correctly and if not reduce a life from them. The code also displays to the user how many lives they have left.
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining.")

    def ask_for_input(self): # The function that holds the user input
        while True: # A while statement that checks if the input from the user is a single letter and prompts them if not, or if they have tried the letter already.
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) # Adds the letter the player guessed to the list of guesses so that a prompt can say they have already tried the letter.

