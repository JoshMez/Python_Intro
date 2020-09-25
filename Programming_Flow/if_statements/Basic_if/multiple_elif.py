#Using multiple if blocks.
#You can use multiple elif blocks, as many as you would like infact.
#Lets just say that you would like to give senior citizen $5 entry to an amusement park.
#Always structure your code in Logical order.
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