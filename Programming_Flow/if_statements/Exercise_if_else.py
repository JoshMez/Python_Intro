#Aim to use an if-else staements to print the name scores in a game.
#
print("You have just shot down a alien ship.\nGuess which color it is")
print("""The choices are 
1)Red 
2)Yellow 
3)Green 
""")
print()
#Creating a variable for the players guess.
Player_Guess = str(input("Please input your guess: "))
#
#Creating variables for alien colors.
alien_red = "Red"
alien_yellow = "Yellow"
alien_green = "Green"
#
#Using an if statment to test out the players guesses.
#
if Player_Guess == alien_red.casefold():
    print("You have earned 15 points")
elif Player_Guess == alien_green.casefold():
    print("You have earned 10 points")
elif Player_Guess == alien_yellow.casefold():
    print("You have earned 5 points")
else:
    print("Please enter a valid choice") 