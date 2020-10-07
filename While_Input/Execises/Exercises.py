#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
#pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.

#Creating a variable that will show a message.
print("When you are done typing your toppings, type done.")
message = "Please enter your pizza topping: "

#Creating the an empty string.
choice = ''

#
while choice != "done":
    if choice == 'done':
        print("You have successfully exited the program. ")
    choice = input(message)
    print(f"You have chosen {choice}")


