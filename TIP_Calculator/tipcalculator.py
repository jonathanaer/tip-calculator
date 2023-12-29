#Tips calculator
#Enter charger for food
food_price = input("Please enter food price: ")
#print(type(food_price))
food_price = float(food_price)
#print(type(food_price))

##Calculate 18% tip
tip = food_price*(18/100)

##Calculater 7% Sales tax
sales_tax = food_price*(7/100)

##Calculate total bill
total_bill=food_price + tip + sales_tax

#Print Receipt
print("Food Price: ", str(food_price),"$")
print("Tip Amount: ", str(tip),"$")
print("Sales Tax: " , str(sales_tax),"$")
print("Total Bill: " , str(total_bill),"$")