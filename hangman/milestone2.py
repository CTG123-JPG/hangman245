import random
word_list = ["Dragon Fruit", "Apple", "Grape", "Orange","Pineapple"] # A list of words in string format containing the names of fruits needed for the rest of the code to run


word = random.choice(word_list) # Allocates a random word from the word list to the variable names "word"


print(word) # Prints the content in the variable "word"


guess = input(f'Input a Letter') # Asks the user to input a letter


if len(guess) == 1 and guess.isalpha(): # Checks the number of characters in the input from the user and checkks if it is equal to 1
  print(f"Good Guess") # If the number of characters is 1 the code continues with "Good Guess"
else:
   print(f"Oops! That is not a valid input") # If the user inputted more than 1 character then the code displays "Oops! That is not a valid input"
