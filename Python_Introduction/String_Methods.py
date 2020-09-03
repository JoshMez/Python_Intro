#The program just aims to explain how strings can use methods. 
#When using a string method, always be sure to put parenthesis (open and closed) after the method is used. 
#The ".tile()" method. 
#Note how the there is a parenthesis () after the string method. 

#Look at how every new word begins with a capital,when the variable is printed.
#method is an action that can be performed on a piece of data.
#Think about ".title" acting on the variable name.
#The parenthesis are empty cause there are no arguements to be taken.

name = "ada lovelace does"
print(name.title()) 

#Using the other string methods
print(name.upper()) #This will print the string in upper case.
print(name.lower()) #This will print the varible in lower case.
print("******************************************************** * * * * **************************************")
print("")
name = input("Please enter your name: ")
print("Hi {}".format(name.title()))
