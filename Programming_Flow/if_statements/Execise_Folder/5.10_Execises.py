#5-10. Checking Usernames: Do the following to create a program that simulates
#how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or
#two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already
#been used. If it has, print a message that the person will need to enter a
#new username. If a username has not been used, print a message saying
#that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#current_users containing the lowercase versions of all existing users.)


#Creating a variable of current users
Current_Users = ["James",
                 "Amy",
                 "David",
                 "Armin",
                 "Charles"
                 ]

#Creating lists of New Users
New_Users = [   "James",
                 "Amy",
                 "David",
                 "Charles",
                 "Damin",
                 ]
for New in New_Users:
    if New in Current_Users:
        print(f"Select another user name: {New}")
    elif New.title in Current_Users:
        print(f"Select another user name: {New}")
    elif New.casefold() in Current_Users:
        print(f"Select another user name: {New}")
    elif New.upper() in Current_Users:
        print(f"Select another user name: {New}")
    elif New.lower() in Current_Users:
        print(f"Select another user name: {New}")
    else:
        print(f"Welcome: {New}")