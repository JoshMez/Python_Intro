#Checking for Mutiple Conditions.
#How to we check if multiple conditions are true at the same time.
#How we do we check if two conditions are true or not.
#TO check if two conditons are true: Use Keyword (and)
#When using the keyword and both conditons must be true.

#Setting variables
age_0 = 22
age_1 = 18
#Using the print statment to check if the variables are true.
print( age_0 >= 22 and age_1 == 18 )
#
#What if we want to improve readablity.
#We are putting each condition to be tested in Parenthesis.
print( ( age_0 >= 22 ) and ( age_1 == 18 ) )
#
print("*" * 50, "Finished", "*" * 50 , "\n")
#
#We can use the or keyword as well, if at least one of the condtions are true then statment will be true.
#Ensuring that one of the values are only true.
print( (age_1 == 20)  or (age_0 == 22) )
#
print("*" * 50, "Finished", "*" * 50 , "\n")
#
#Checking if a value is in the list.
#
#Creating a lists of cars
cars = [ "Audi", "BMW", "Holden"]
#Using the print statement to check if Audi is in the list of cars.
#Keyword to used (in)
print(("Audi" in cars))
#
#Checking to see if Honda is not in car.
#
print("Honda" not in cars)
#
#Using the print statemnent to check if honda is in cars.
#
print("Honda" in cars)
#
print("*" * 50, "Finished", "*" * 50 , "\n")
#
#Using the if statment to check if along with keyword if and in.
#
#Creating a lists users who are banned from entering the chat room
Banned_Names = [ "Jason", "Ral", "Steph", "Savy" ]
user = "Josh"
if user not in Banned_Names:
    print(f"{user.upper()} is allowed to enter the chat room")   
# You dont have to supply a finished statement in Python. 
# 
#Boolean Expressions. 
#Boolean is either true or false. 
#Boolean can be great to track a state of the program.
game_active = True 
can_edit = False
