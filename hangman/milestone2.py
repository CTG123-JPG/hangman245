import random
word_list = ["Dragon Fruit", "Apple", "Grape", "Orange","Pinapple"]

print(random.choice(word_list))

guess = input(f'Input a Letter')
# Asks the user to input a letter
if len(guess) == 1 and guess.isalpha():
  print(f"Good Guess")
else:
   print(f"Please try again")

