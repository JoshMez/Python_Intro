#Using basic if statements.

#Simple if statement.
#Basic structure of an if statement.
#if conditional_test:
    #do_something
#In Python there is no need to close of the if statement,
#
#Prompting the user to enter their age.
age =int(input("Please state you age: "))
#
#Using a simple if statement to see if someeone is old enough to vote
#Basically will print the statement if the votes is above the age of 18.
#if the condition is not met, the statement will not be printed.
if age >= 18:
    print( "You are old enough to vote.")
    #Can print multiple statement if a conidtion is met
    #Ensure same indetation.
    print("Please remember to vote")
