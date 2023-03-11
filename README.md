# Python Hangman
In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.

For this project, we trained a neural network to play Hangman by appropriately guessing letters in a partially or fully obscured word. The network receives as input a representation of the word (total number of characters, the identity of any revealed letters) as well as a list of which letters have been guessed so far. It returns a guess for the letter that should be picked next. This repo shows our method for training the network with Microsoft's Cognitive Toolkit (CNTK) and validating its performance on a withheld test set, as well as operationalizing the model for gameplay on an Azure Web App.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
# Python Hangman Milestone 2
A repository containing the guide for AiCore Milestone 2. This syntax does:
- imports the random module to randomly assign a word from the list to guess
- creates a list of fruits to be picked up by the random module
- uses the random module and picks a word from the fruits list
- asks for user's input to guess the letters in the word
- validates the user's input - if the letter is in the word
# Python Hangman Milestone 3
A repository containing the guide for AiCore Milestone 3. This syntax creates two functions:
- creates a user input function. When calld the function will ask for the user's input.
- creates a check function to verify the user's input. check user's input compared to the randomly assigned word in the list. 
- calls the two functions to test if they return the correct result. 
# Python Hangman Milestone 4
- creates a class
- create methods for running the checks
- defines what happens if the letter is in the word
- defines what happens if the letter is not in the word
- updates the documentation 

# Python Hangman Milestone 5
- this programme checks for 
- this programme checks for

