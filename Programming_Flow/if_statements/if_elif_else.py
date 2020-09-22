#Aim: Illustrate how the if-elif-else statement works.
#Python can only execute one if-else statement at a time.
#Many real world examples do not allow you to have only 2 options.

print("Please enter your age to see age prices for each age group.\n")
#
age = int(input("Enter age in digits: "))
#
if age < 4:
    price = 0
elif age > 4 and age < 18:
    price = 4
else:
    price = 10
#The variable has been called from the price variable.
#This can make our code easier to modify.
print(f"You admissions price is ${price}.")
#
print("*" * 50, "Finished", "*" * 50, "\n\n")
#
#Using multiple if blocks.
#You can use multiple elif blocks, as many as you would like infact.
#Lets just say that you would like to give senior citizen free entry to an amusement park.

print("Please enter you age. ")
#
age = int(input("Please input your age: "))
#
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 0

print(f"You entry fee is ${price}")