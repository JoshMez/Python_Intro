#When you write a function you can assign a default value to a parameter.
#
#
#Dont think of think of the default value of being set in stone.
#It will only be used when you have not see anything else.
############################################################
#
def Charecter(charecters, studio='Marvel' ):
    """Seeing my fav charecter."""
    print(f"Studio type: {studio}")
    print(f"Charecter: {charecters}")




#Changing the default agurment
#Notice how the default variable has not been used.

Charecter(studio='DC', charecters='Batman')
###############################################################
#
#Avoiding errors.
#Sometimes you may have errors on in your functions.
#
#Soemtimes you can provide more or less arugments than the functions needs.
#But you ne