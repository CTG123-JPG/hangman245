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
          guess = guess.lower()
          if guess in self.word.lower():  # The guess and word are both now lower to ensure the code is case-insensitive.
              print(f"Good guess! {guess} is in the word.") 
              for letter in range(len(self.word)):# A for loop to replace the underscores at each letter guessed by the user.
                  if self.word[letter].lower() == guess:
                      self.word_guessed[letter] = guess
              print(f"Word: {' '.join(self.word_guessed)}") # Displays the present standing of the underscores and letters guessed to the user.
              if guess not in self.list_of_guesses: # A code to ensure the num_letters is only decremented once per word guessed by the user in case there are duplicate letters in the word. 
            
                 self.num_letters -= 1
          else:
              self.num_lives -= 1 # An else statement that prompts the user the guess is not in the word selected.
              print(f"Sorry, {guess} is not in the word. Try again.")
              print(f"Word: {' '.join(self.word_guessed)}") # Shows the current state of the guessed word to the user.
              print(f"You have {self.num_lives} lives remaining.") # Promopts the user how many lives they have left
              if self.num_lives == 0:# An if statement to ensure the code only runs when the users life is above 
                  return False 
          return True
    def ask_for_input(self): # A function to ask for the users input and check if it is a single alphabetical character.
        while True:
            guess = input("Guess a letter: ").lower() # Converts the input from the user to lower case to make the code case-insensitive.
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.") # Prompts the user if they have inputted incorrectly.
            elif guess in self.list_of_guesses:
                print("You already tried that letter!") # Prompts the user if they have guessed a letter already which is saved in the empty list "List of guesses"
            else:
                if not self.check_guess(guess):
                    return False                    
            self.list_of_guesses.append(guess) # Appends the guess from the player to the list of guesses list. 
                
def play_game(word_list): # The function to initialise the entire game
    game = Hangman(word_list) # Calls the hangman class and passes the Word_list as an argument
    
    while True:
        if game.num_letters == 0 and game.num_lives > 0:  # The condition for a win if the number of lives is above 0 and the number of letters is 0.
            print(f"Word: {' '.join(game.word_guessed)}") # Shows the user the current state of the word they have guessed.
            print("Congratulations. You won the game!") # Prompts the user they have won the game
            break
            
        if game.num_lives == 0:# The losing condition if lives are 0
            print("You lost!") # Prompts the user they have lost the game
            print(f"The word was: {game.word}") # Prints the actual word they were meant to guess.
            break
            
        print(f"Word: {' '.join(game.word_guessed)}") # Prints the current state of the word being guessed by the user.
        if not game.ask_for_input(): # The game continues until one of the above conditions are met
            print("You lost!")
            print(f"The word was: {game.word}")
            break

play_game(word_list)
