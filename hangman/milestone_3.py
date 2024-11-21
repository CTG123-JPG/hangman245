import random 
from word_list_for_hangman import word

#The above imports the necessary items needed to run the code. With the second code importing the word list from another .py file

def check_guess(guess): #This is a function to check if the guess inputted by the player is in the randomly selected word from the word list
    guess.lower() #Makes sure the input by the player is converted to a lower letter of the alphabet
    while True:# A loop to show weather the user input is in the randomly selected word from the word list
     if guess in word:
        print(f"Good guess! {guess} is in the word.") # prompts the user that the letter they have chosen is in the word
   
     else:
        print(f"Sorry, {guess} is not in the word. Try again.")# prompts the user that the letter they have chosen is outside of the word
     break

def ask_for_input():#function to get an input from the user ensuring it is only 1 letter.
    while True:
         guess = input("Guess a letter: ")
         
         if len(guess) == 1 and guess.isalpha():
            break
         else: 
          print(f"Invalid letter. Please, enter a single alphabetical character.")#prompts the user to retry as the entry does not match the required specifications.
    check_guess(guess)


ask_for_input()     # calling the function to start the game
