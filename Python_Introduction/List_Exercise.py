#Execise list.
#Create a guest list of people who you would like to come to dinner with you.
#But also add an options remove and add people who want to come to party as well.
#Just creating a 
print("This is a simple program to add and delete users of your guest list. ")
print("You current guess are Athena", "Lucifer", "Angel") 
print("Please type quit if you want to quit the program ") 
print()
Guest_List = ["Athena", "Lucifer", "Angel"]


#Adding people in the lists.
for i in Guest_List:
    extra = input(str("Who is else is coming: "))
    if extra == "quit":
        print("Thank you for adding")
        print(f"You current guests are {Guest_List}")
        break
    else:
        extra = Guest_List.append(extra)
        print(Guest_List)
