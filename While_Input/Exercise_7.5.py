#7-5. Movie Tickets: A movie theater charges different ticket prices depending on
#a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#$15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket.
#(continued)
#########
#########
#

#Creating a message.
message = "Please enter your age: "

#Flags
flag = True
#Creating a varaible called age.


while flag:
    age = input(message)
    age = int(age)
    if age < 3:
        print("Entry: Free")
        flag = False
    elif age >=3 and age <= 12:
        print("Entry: $10")
        flag = False
    elif age >= 12 and age <= 60:
        print("Entry: $15")
        flag = False
    else:
        print('Entry: Free')
        flag = False
