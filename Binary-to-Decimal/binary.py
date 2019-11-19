#Task 23
#Compulsory exercise
#The program request a user enter a binary code.
#It then converts the entered binary code into decimal code.
import math #Allows the program to use the math module 

user_input = list(input("Enter a binary number: ")) #Adds user's binary code to a list to convert it to decimal numbers.
decimal = 0
 
#For every value in user_input it converts the binary to decimal.
for num in range(len(user_input)):
  digit = user_input.pop()
  if digit == "1":                            
   decimal = decimal + pow(2,num) #Formula which converts binary to decimal.
binary = "".join(user_input) #Adds the converted numbers together.
print("The decimal code of {} is".format(binary),decimal)