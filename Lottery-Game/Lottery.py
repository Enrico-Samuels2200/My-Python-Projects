#Task 12
#Optional task
#Program is a lottery game that request user enters a double digit and compare it to a randomly generated number.
#If user has the correct digits regardless of order he/she wins prize money.
 
from random import randint #Allows for function 'randint' to be imported.
 
user_guess = "1"
 
#Generates random double digit number.
wining_number = randint(10,99)
lucky_list = list(str(wining_number)) #Adds the random generated number to a list 'lucky_list'.
 
print("Please enter a digit between 10 and 99.")
 
#Keeps requesting the user enters a number until a double digit is entered.
while len(user_guess) == 1:
 user_guess = str(input("Enter your lucky wining number: "))
 lucky_guess = list(str(user_guess)) #Adds the users input into a list 'lucky_guess'.
 
if lucky_list[0] == lucky_guess[0] and lucky_list[1] == lucky_guess[1]: #Activates if user number matches that of the generated number and is in correct order..
    print("Congratulations you have an exact match, you win R10 000.00")
elif lucky_list[0] == lucky_guess[1] and lucky_list[1] == lucky_guess[0]: #Activates if the user got the correct number but not in the correct order.
    print("Congratulations you have all digits, you win R5 000.00")
elif lucky_list[0] == lucky_guess[0] or lucky_list[1] == lucky_guess[1]: #Activate if the user got at least one correct number.  
    print("Congratulations you have one correct digit, you win R1 000.00")
else:                                                                    #Activates if user doesn't have any digits that matches that of the generated number.
    print("Sorry no match.")    