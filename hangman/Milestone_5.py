import random
from word_list_for_hangman import word_list
#The above code imports the necessary items for the code to run including the Word_list kept in another file for ease

class Hangman:# A class for the entire Hangman game
    def __init__(self, word_list, num_lives=5):# Defining each parameter within the function and ensuring the default number of lives is 5
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)  # selects a random word from the word_list
        self.word_guessed = ['_'] * len(self.word)  # the underscores represent each letter not guessed within the random word selected
        self.num_letters = len(self.word)  # The number of letters the user has to guess
        self.list_of_guesses = []  # An empty list so that the user's guesses have somewhere to go so we can tell them they have already tried a letter.

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives remaining.")
            if self.num_lives == 0:
                return False
        return True

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if not self.check_guess(guess):
                    return False
                self.list_of_guesses.append(guess)
                
def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives <= 0:
            print("You lost!")
            print(f"The word was: {game.word}")
            break
        elif game.num_letters > 0:
            print(game.word_guessed)
            game.ask_for_input()
            break
        else:
            print("Congratulations. You won the game!")
            break
play_game(word_list)
