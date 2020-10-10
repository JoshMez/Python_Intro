#Using Key_Word Aruguments.
#
#
#Name-value pair when you write a function.
##Creating a variable of my fav Marvel, DC/
#
def Marvel_DC(studio, charecter ):
    """Seeing if a character is Marvel or DC"""
    print(f"Charecter name: {charecter}")
    print(f"\nStudio name: {studio}\n\n")
#Calling the function
Marvel_DC('Black Panther','Marvel')
#####
#We can do this if you know the paramter you have provided.
#
########
############
Marvel_DC(studio='DC', charecter='Batman')
#################
#Notice that how you did not have to worry about the positions.
#
Marvel_DC(charecter='Huey', studio= 'Adult Swim')
###
