import random

class Hangman:
    def __init__ (self):
        #create list of favourite fruits
        self.word_list = ['apple','banana','peach','pineapple', 'watermellon']
        #randomly select a fruit from the list
        self.word = random.choice(self.word_list)
        #The number of UNIQUE letters in the word that have not been guessed yet.
        self.num_letters = len(set(self.word))
        #number of lives
        self.num_lives = 5
        # Word guessed
        self.word_guessed = list(self.word)
        #A list of the guesses that have already been tried. Set this to an empty list initially.
        self.list_of_guesses = []
        #Asks for user's input so you can 
        self.guess = input("Please type your letter here: ")

    def ask_for_input(self):
        while True:
            if len(self.guess)==1 and self.guess.isalpha():
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

    #This is the check_guess function wich 
    def check_guess(self):
        self.guess = self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess}")
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")

    
     
