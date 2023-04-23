# AtlantaPizza.py - a simple pizza cost calculator

#Ask the person how many pizzas they want, get the number with eval()
number_of_pizzas  = eval(input("How many pizzas do you want?"))
#Ask for the menu cost of each pizza
cost_of_pizzas = eval(input("How much does each pizza cost?"))
#Calculate the total cost of the pizzas  as a subtotal
subtotal =  number_of_pizzas * cost_of_pizzas

#Calculate the sales tax owed at 8% of the subtotal
sales_tax = 0.08

#Store tax rate as a variable
tax_rate = subtotal * sales_tax

#Calculate the total cost of the  pizza  with sales tax.
total = subtotal + tax_rate

#Print the Subtotal, Sales Tax, and Total Cost of the pizza.
print ("Subtotal =", subtotal)
print ("Sales Tax =", tax_rate)
print("Total =", total)
