#Aim: Sometimes its useful to check if a list is empty.
#
#Creating an empty list.
requested_topping = []
#
#Lessons learned.
#1)A for loop can be in an if statement.
#2)if statments are used to check wheter a specific condition is true or not.
#3)
#We are checking to see if the lists requested topping does exist.
if requested_topping:
    #We are checking if the there is anyting within the list.
    for requested_topping in requested_topping:
        print(f"Adding {requested_topping}")
    print("\n,We finished making your Pizza")
else:
    print("Are you sure you want a Plain Pizza ?. ")
