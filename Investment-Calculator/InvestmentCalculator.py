#Task 12
#Compulsory task
#Program ask user to input their amount they're depositing, the number of years and their interest percentage.
#It then ask the user if he/she wants simple or compound interest, and finally it calculates the amount they'll receive.
 
#Imports math module.
import math
  
P = int(input("Enter the amount of money you want to deposit: R"))
i = int(input("Enter the interest percentage amount: "))
t = int(input("Enter the number of years you would like to invest for: "))
interest = str(input("Would you like 'simple' or 'compound' interest? "))
 
#Converts int percentage to a float.
interest_percentage = i / 100

#Formula for simple interest. 
if interest == "simple":
 A = int(P*(1 + interest_percentage * t))
 print("You have selected simple interest. After",t , "years you would accumulate R{:,.2f}".format(A))
   
#Formula for compound interest.  
elif interest == "compound":
    A = int(P* math.pow((1 + interest_percentage),t))
    print("You have selected compound interest. After",t , "years you would accumulate R{:,.2f}".format(A))