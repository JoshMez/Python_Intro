#The basics of If statments.
#If tests lets you test and respond to situations.
#Using a simple
cars = ["audi","bmw" ,"toyota", "holden"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#
print("*" * 50)
print("\n\t\t\t\t *Finished* \n")
print("*" * 50)
#Conditional Tests
#Think of the Python if statement working as True and False values.
#If something is condition meets the criteria, then the statments will run.
#If the condition is not true then the statment will not run.

#Checking for equality.
car = "bmw"
print(car == 'bmw') #Use the double == to see if value are equal to each other or not.
#Just remember that when you are comparing values : Always use ==

#Ignoring the case and checking for equality.
car = 'Audi'
#Using .title() string method.
print(car.title() == car)
#Using the .lower() string method.
print(car.upper() == car )
#The main take away is realise that
        # The ' == ' equal sign can be used to compare values.
        # You can use string methods to compare the values.
        #Python is very specific when it comes to programming.
#
print("*" * 50)
print("\n\t\t\t\t *Finished* \n")
print("*" * 50)
#
#Checking in INEQUALITY.
#The syntax for checking that two values are not NOT EQUAL is (!=)
#Either answers an if statment with Yes and no , then try to provide an answer as to why its true.

Toppings = "cheese"

if Toppings != "chicken":
    print("He does not want cheese")
else:
    print("Yep they want cheese")
#THe main take way.
    #Make sense of your code.
    #Comparing string values means dealing with (==) and (!=)
    #You can also use string methods when comparing values.
print("*" * 50)
print("\n\t\t\t\t *Finished* \n")
print("*" * 50)
#Numerical Comparisons
#Numerical values can be compared as well.
#You can use the (==), this is to test if two numbers are equal
#You can use the (!=), to test if the the numbers are not equal.
#Greater that or equal to >=
#Less thann or equal to <=

answer = 17
if answer != 42:
    print("Yes you are correct, 17 is not equal to 42.")
#
#Using greater or equal to sign .
answer = int(input(("Please enter a digit: ")))
if answer >= 17:
    print("Look like you are right")
else:
    print(f"{answer} is the number you entered and it is not greater or equal to 17")
