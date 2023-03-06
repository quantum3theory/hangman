#import random module
import random

#create list of favourite fruits
word_list = ['apple','banana','peach','pineapple', 'watermellon']
#randomly selecting a fruit from the list
word = random.choice(word_list)
#printing the fav fruit
print(word)
#asking user for input 
guess = input("Type your input here: ")
#validating the user input
if len(guess)==1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input")