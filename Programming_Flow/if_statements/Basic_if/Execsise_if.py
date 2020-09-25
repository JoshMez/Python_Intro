#This is just a simple program to test basic if statement skills.
#
print("Imagine an Alien was just shot down in a game.\nCreate a variable called 'alien_color'")
print("Assign the variable a value of green, blue, yellow or red.\n")
print("Write an If statememt to test if the colors of the alien is green.\nIf program fails there should be no output.\n")
print()

#Creating a variable.
alien_color = "green"
#
#Creating a variable of the users guess
print("Avaliable guess are red, blue, green, yellow")
player_guess = str(input("Please guess color: "))

if alien_color == player_guess.casefold():
    print("Well done you are right.")