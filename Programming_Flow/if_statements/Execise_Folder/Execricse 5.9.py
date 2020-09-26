#5.9) Add an if statment to hello_admin to make sure that the list of users is not empty.
#

#Creating an empty lists.
Lists_of_users = []

#Test to see if the lists of user exits.
if Lists_of_users:
    for User in Lists_of_users:
        print(f"Hello: {User}")
else:
    print("You need to add users.")