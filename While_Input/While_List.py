#Using lists and Dictionaries in our while loops.
#
#To modify a list, as you work through it, use a while loop.
# Allows you to
    #Store
    #Collect
    #Organise lots of input to examine and store later.
#####
####
#Aim : To move one list from one to another.
#

#Creating a list of users that need to be verified.
unconfirmed_alias = ["Lisa",
                     "Marge",
                     "Bart"
                     ]
#Creating an empty list.
confirmed_alias = []
####
#
#Using a while loop.
#Using pop until nothing remains in the loop.

while unconfirmed_alias:
    #Remeber the .pop removes that the last item on the list.
    current_user = unconfirmed_alias.pop()
    print(f'Verifying users:{current_user.title()}')
    confirmed_alias.append(current_user)

print()
print("We have verified the following users: ")
#Verifying the the Users have been confirmed
for current in confirmed_alias:
    print(f"+{current}")

