import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)  # select a random word from the list
        self.word_guessed = ['_'] * len(self.word)  # initialize word_guessed with underscores
        self.num_letters = len(self.word)  # initialize num_letters to the length of the word
        self.list_of_guesses = []  # initialize list_of_guesses as an empty list

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
        print(f"You have {self.num_lives} lives remaining.")
        print(' '.join(self.word_guessed))  # print the current state of the word

    def play_game(self):
        self.ask_for_input()

# create an instance of the class
game = Hangman(['apple', 'banana', 'cherry'], 5)
game.play_game()