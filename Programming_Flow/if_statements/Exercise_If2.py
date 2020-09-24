#Aims: Using the if statement to see if a condtion is correct or not.
#
#
print("You have just shot down an alien ship.\nYou need to guess the color of the alien ship")
print("""The choices you have are : 
1) Red 
2) Green 
3) Yellow  
""")
alien_color = "green"
alien_red = "red"
alien_yellow = "yellow"
#
player_guess = str(input("Please input your guess: "))
#
if player_guess == alien_color:
    print("You have earned 5 points.")
elif player_guess == alien_red.casefold() or player_guess == alien_yellow:
    print("You have earned 10 points.")
else:
    print("You have to input a valid choice.\nRun the program again.")

