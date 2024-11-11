import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)  
        self.word_guessed = ['_'] * len(self.word) 
        self.list_of_guesses = [] 

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
                self.display_word()
                if self.num_lives == 0:
                    print("You lost!")
                    return
                elif '_' not in self.word_guessed:
                    print("Congratulations. You won the game!")
                    return

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for num in range(len(self.word)):
                if self.word[num] == guess:
                    self.word_guessed[num] = guess
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
        print(f"You have {self.num_lives} lives remaining.")

    def display_word(self):
        print(" ".join(self.word_guessed))

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        game.ask_for_input()

word_list = ["apple", "banana", "cherry"]
play_game(word_list)
