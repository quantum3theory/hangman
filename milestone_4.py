import random
import re

class Hangman:
    def __init__ (self, word_list, num_lives=5):
        #create list of favourite fruits
        self.word_list = word_list
        #randomly select a fruit from the list
        self.word = random.choice(self.word_list)
        #The number of UNIQUE letters in the word that have not been guessed yet.
        self.num_letters = len(set(self.word))
        #number of lives
        self.num_lives = num_lives
        # Word guessed
        self.word_guessed = list(map(lambda i: i.replace(i, '_'), list(self.word)))
        
        #A list of the guesses that have already been tried. Set this to an empty list initially.
        self.list_of_guesses = []

    def ask_for_input(self):
        #Asks for user's input so you can 
        self.guess = input("Please type your letter here: ")
        while True:
            if len(self.guess)==1 and self.guess.isalpha():
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

    #This is the check_guess function wich 
    def check_guess(self):
        print(self.word_guessed)
        self.guess = self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess}")
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")
