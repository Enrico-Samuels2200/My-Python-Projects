# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:22:38 2019

@author: Kay
"""

from random import *

player_score = 0;
computer_score = 0;

def hangedman(hangman) :
    graphic = [
            """
                +-------+
                |
                |
                |
                |
                |
             --------------
             --------------
            """
               ,
            """ 
                +-------+
                |       |
                |       O 
                |
                |
                |
             --------------
             --------------
            """,
            """ 
                +-------+
                |       |
                |       O 
                |       |
                |
                |
             --------------
             --------------
            """,
            """ 
                +-------+
                |       |
                |       O 
                |      -|
                |
                |
             --------------
             --------------
            """,
            """ 
                +-------+
                |       |
                |       O 
                |      -|-
                |
                |
             --------------
             --------------
            """,
            """ 
                +-------+
                |       |
                |       O 
                |      -|-
                |      /
                |
             --------------
             --------------
            """,
            """
                +-------+
                |       |
                |       O 
                |      -|-
                |      / \
                |
             --------------
             --------------
            """]
    
    print(graphic[hangman])
    return

def start() :
    print("Let's play a game of Hangman.")
    #'game()' calls the game function and starts the actual game.
    while game() : 
        pass; #Keeps track of the scores until the game is finished.
    scores(); #Once the game is completed it'll return the scores
    
def game() :
    dictionary = ["anata", "baka", "namae", "boku", "mina"];
    
    word = choice(dictionary); #Choose random number and call word based on index number. 'choice' comes from random import
    word_length = len(word);
    clue = word_length * ["_"]; #For each letter print '_'
    
    tries = 6; #Sets the amount of tries the user gets.
    letters_tried = "";
    guesses = 0; #Guesses by default should be 0.
    letters_right = 0;
    letters_wrong = 0;
    
    global computer_score, player_score;
    
    while (letters_wrong != tries) and ("".join(clue) != word): #This basically says if the user didn't use up their tries and if there clue slot is not filled run function. 
        letter = guess_letter(); #Calls function (guess_letter) code-line[146]
        if len(letter) == 1 and letter.isalpha(): #If the length returned is equal to 1 and is alphabetical then run function.
            if letters_tried.find(letter) != -1: #If you've entered a letter more than once it'll look though the string you entered and if its there it'll return the message.
                print("You've already picked", letter);
            else:
                letters_tried = letters_tried + letter; #Adds the letters the user entered to the letters tried var.
                first_index = word.find(letter) #It looks at the first letter(the lowest value being index 0) of the returned string. If it's not the same it returns the int -1.tr
                if first_index == -1: #If the string returns the value -1 run function.
                    letters_wrong += 1; #Adds a number to the letters wrong. Remeber once the numbers add up to the same value of the guesses its game over.
                    print("Sorry,",letter,"isn't what we're looking for.");
                else:
                    print("Congradulations" ,letter, "is correct."); #Prints if the user got something correct.
                    for i in range(word_length): #Loops through the array for each letter
                        if letter == word[i]: #If the letter matches with any letter in the array 'word'(The correct word) the function runs.
                            clue[i] = letter; #The letter will replace the clue(_) so this is replaced by the index. Example (____) the correct word is (mina). Index[1] is replaced so this will return (_i__).
        else:
            print("Choose another."); #Returns if the entered value is not a string.
        hangedman(letters_wrong) #Calls the graphic array and passes the number of letters the user got wrong in it. The numbers passed are used as an index to the array.
        print("".join(clue)); #Adds the letters the user got correct to the clue(_i__).
        print("Guesses", letters_tried); #Displays the letters the user already tried.

        if letters_wrong == tries: #If the user doesn't have any turns left the function will run.
            print("Game Over.");
            print("The word was: ",word);
            computer_score += 1; #Adds 1 score to the computer total.
            break; #Breaks through the game loop.
        if "".join(clue) == word: #If the clue matches the correct word the function will run.
            print("You win!");
            print("The word was: ", word);
            player_score += 1; #Adds 1 score to the player/user total.
            break; #Adds 1 score to the computer total.
    return play_again() #Returns function that asks user if they wish to play again or not.

def guess_letter() :
    letter = input("Take a guess at our mystery word: ")
    letter.strip(); 
    letter.lower() #Makes the user input lowercase.
    return letter #returns the processed user input.

def play_again() :
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer #If a value is returned the game will continue.
    else:
        print("Thank you very much for playing our game. See you next time! \n")
        
def scores() : #Calls once game is completed.
    global player_score, computer_score #Calls vars
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ",computer_score)

if __name__ == '__main__' : #Allows thoe code to be called using cmd and if importing code won't run automatically
    start()