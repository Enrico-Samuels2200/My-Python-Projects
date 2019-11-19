# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:29:53 2019

@author: E.S
"""
#Random module is used to gain a random number.
import random
#Time module used as a timer.
import time

#Assigning a num to each option so that when called it will return that value.
rock = 1;
paper = 2;
scissors = 3;

#The names are chosen when ever the computer chooses a number.
names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
#Rules define the games rules what eats what.
rules = { rock: scissors, paper: rock, scissors: paper }

#Not with in a function so score can be kept the same instead of resetting everytime.
player_score = 0; #Keeps track of the users score.
computer_score = 0; #Keeps track of computer score.

def start() :
    print("Let's play a game of Rock, Paper, Scissors.")
    #'game()' calls the game function and starts the actual game.
    while game() : 
        pass; #Keeps track of the scores until the game is finished.
    scores(); #Once the game is completed it'll return the scores.
    
def game() :
    player = move(); #Calls on function move which records players and computer's moves.
    computer = random.randint(1, 3); #Generates random number between 1 and 3.
    result(player, computer); #Calls on the result function and passes the player and computers scores.
    return play_again(); #Returns the play_again function.
    
def move() : #Used to get value from player.
    while True: #Loop will keep repeating until acceptable value is thrown.
        player = input(" Rock = 1\n Paper = 2\n Scissors = 3\n Make a move: "); """Gets users input."""
        try:
            player = int(player); #Converts users input to string.
            #Checks if players choice is with in bounds.
            if player in (1,2,3):
                return player
            elif player > 3 or player < 1: #If player chooses num  greater than 3 or less than 1 then pass as error.
                print("Sorry enter either 1, 2 or 3")
        except ValueError: #Activates once player enters anything that can be parsed to an int(number).
                pass
                print("Oops! I didn't understand that. Please enter either 1, 2 or 3")

def result(player, computer) : #Imports users and compuer score for use.
    print("1...")
    time.sleep(1) #Uses time module allows a 1 second pause.
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer])) #{0}!".format(names[computer]) uses the value the computer got eg(rock) and calls upon that in dictionary 'names'.
    global player_score, computer_score #Allows the var to be altered outside of the var itself.
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer: #If players value is equal to that of computer from dictionary then the players wins. Example player{rock} and computer{scissors}.
            print("Your victory has been assured.")
            player_score += 1 #Appends 1 score to player score.
        else:
            print("The computer laughs as you realise you have been defeated.")
            computer_score += 1 #Appends 1 score to the computer score.

def play_again(): #Once game ends this will activate
    answer = input("Would you like to play again? y/n: ") #Request users input.
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