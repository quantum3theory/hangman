import random
class Hangman:
    def __init__ (self, word_list, num_lives): 
        #create list of favourite fruits
        self.word_list = word_list
        #randomly select a fruit from the list
        self.word = random.choice(word_list)
        #The number of UNIQUE letters in the word that have not been guessed yet.
        self.num_letters = len(set(self.word))
        #number of lives
        self.num_lives = num_lives
        # Word guessed
        self.word_guessed = ['_'] * len(self.word)
        #A list of the guesses that have already been tried. Set this to an empty list initially.
        self.list_of_guesses = []
          
    #This is the check_guess function wich 
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
                    
            self.num_letters -= 1
            print(self.num_letters)

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
  

    #function that asks for the user's input        
    def ask_for_input(self):
        #Asks for user's input so you can 
       while True:
            guess = input("Please type your letter here: ")
            if len(guess)>1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


            
def play_game(word_list):
    word_list = [word_list]
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters < 0:
            print('Congratulation. You won the game!')
            break
            
game_1 = play_game('banana')