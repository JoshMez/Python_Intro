#5-8. Hello Admin: Make a list of five or more usernames, including the name
#'admin'. Imagine you are writing code that will print a greeting to each user
#after they log in to a website. Loop through the list, and print a greeting to
#each user:
#• If the username is 'admin', print a special greeting, such as Hello admin,
#would you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
#   logging in again.

#Creating a list of name
names = ["admin",
         "Josh",
         "Mason",
         "Rachel",
         "James"]

for name in names:
    if name == "admin":
        print(f"Hello {name}\nWould you like a status report ?\n")
    else:
        print(f"Welcome {name}") \\\
