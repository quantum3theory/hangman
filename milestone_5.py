import random
from milestone_4 import Hangman

            
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
        elif num_lives != 0 and game.num_letters <= 0:
            print('Congratulation. You won the game!')
            break
            
            
game_1 = Hangman.play_game('banana')