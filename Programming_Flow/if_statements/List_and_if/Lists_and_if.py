#Using if statement with lists.
#
print("""A customer has ordered 3 pizza toppings. 
But the pizzeria does not have green peppers anymore. 
""")
print("Display to the customer that there are no green peppers")
print()
List_Of_Toppings = [ "Chicken",
                     "Cheese",
                     "Green Peppers"]
#
for toppings in List_Of_Toppings:
    if toppings == List_Of_Toppings[2]:
        print(f"We have run out of {List_Of_Toppings[2]}")
    else:
        print(f"Adding {toppings}")
