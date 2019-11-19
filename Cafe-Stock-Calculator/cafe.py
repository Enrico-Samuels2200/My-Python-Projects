#task 22
#Compulsory exercise 1
#The program takes the price of each item and multipliies it by the stock amount.
#This then displays the cafes total worth of stock.

#Function to calculate the total worth of stock.
def total_stock(stock,price):
  totalStock = 0
  for item in stock:                                          
    totalItem = price[item] * stock[item] #Multiply the price by the stock.                       
    totalStock += totalItem                                       
  print("The total worth of stock in the cafe is R{:,.2f}".format((totalStock)))


menu = ['Tea','Coffee','Choc-cake','Grilled cheese']
price = {'Tea': 5,'Coffee': 8,'Choc-cake': 10,'Grilled cheese': 12}
stock = {'Tea': 45,'Coffee': 35,'Choc-cake': 20,'Grilled cheese': 59}

print(menu,"\n")
print("Price in rands: ",price)
print("Amount of stock left: ",stock,"\n")

#Calls on function "total_stock".
total_stock(stock,price)