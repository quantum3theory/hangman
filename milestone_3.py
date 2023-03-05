import random
#create list of favourite fruits
word_list = ['apple','banana','peach','pineapple', 'watermellon']
#randomly selecting a fruit from the list
word = random.choice(word_list)
print(word)
#Asks for user's input so you can 
guess = input("Please type your letter here: ")

def ask_for_input():
    while True:
        if len(guess)==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
ask_for_input() 


#This is the check_guess function wich 
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess}")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
check_guess(guess)  
    
     
