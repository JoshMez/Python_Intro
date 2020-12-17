#Passing a number of Arbitrary of Arguments.
#
#Function will allow users to store their favorite Shiraz sold at BWS.
#
def bws_shiraz(*shirazzy):
    """Favorite Shiraz"""
    print("You favorite shiraz of choice is: ")
    for shiraz in shirazzy:
        print(f"{shiraz.title()}")
    print("\n")
bws_shiraz("Saint Hugo Shiraz", "Young and Co", "Annies Lane", "Hardy's")
bws_shiraz("Gentleman's Collection Shiraz","Red Knot" )


#############
def shiraz_time(time, *shirrazy):
    """Tell customers what time they can come collect their Shiraz."""
    print(f"You can come and collect your Shiraz at: {time.strip()}\nYou order of Shiraz is:")
    for s in shirrazy:
        print(f"{s}")

#Calling shiraz_time.
shiraz_time("16:00", "Hardys","Pepper Jack", "Yellow Tail" )
