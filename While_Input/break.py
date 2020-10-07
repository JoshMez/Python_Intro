#Using break to exit a loop
#
#
#To exit a loop immediately without running ANY REAMINING CODE.
####-> use the break statement.

#Example of using a break keyword,
Intro_Message = "Hello, Please enter a city you want to vist."
Intro_Message += "\nJust pickone\n"
Intro_Message += "Enter here:  "

while True:
    city = input(Intro_Message)

    if city == 'quit':
        print("Ending the program")
        #This will stop the program from running entirely.
        break
    else:
        print(f"I want to visit this {city.title()}.\n")
