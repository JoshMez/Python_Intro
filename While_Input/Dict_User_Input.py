#Creating an empty dictionary.
#
#Creating an empty dictionary.
responses = {}
#
#Creating a flag.
polling_active = True
####
#
while polling_active:
    #Prompting the user for input.
    naming = input("Whats your name: ")
    response = input("Which mountain do you want to visit: ")

    #Store the responses in the dictionary
    responses[naming] = response

    #Seeing if anyone else want to add.
    repeat = input("Do you want to add another person as well, Yes or No: ")
    #
    if repeat == 'no' or repeat == 'N' or repeat == "No":
        print("Ending the program ")
        polling_active = False
    #

for name,r in responses.items():
    print(f"Hi {name}, it looks like you want to visit {r}")