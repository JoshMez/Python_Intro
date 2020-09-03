#You can used either single or double quotes in a string.

#Using a single quote
print('Hello, my name is Josh')

#Using double quotes, Just remember: Only use one quotation mark when starting your string.
print("Hello, my name is Josh")

print(" * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * ")
print()
print("The following string below used string conacatination")
#String concatination was used to accomplish this, with string cancatination, + is used to join strings.
print("Hello" + " my" + " name " + " is" + "  Josh")
print()
print(" * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * ")
print()
#The sole focus of this code, is to show how strings can be assigned to variables.
#Notice how the variable name is on the left hand side and the object assigned to it comes on the right hand side.
greeting = "Hello"
name = "Josh"

#Printing a variable using string concatination.
#When passing the variable into the function, we did not have to put the variable in double quotes.
print(greeting + " " + name)

print(" * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * ")
print()
#You can use the Input fucntion to get information for the user, the information type will be type from the variable.
name = input("What is you name ? ") #Take note: The structure of the input function.
print(name)
