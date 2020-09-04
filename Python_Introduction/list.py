#This just contains basic Information of lists. 
#Creating lists
#You can store any item in a list.
#You can create lists with square brackets.
#Gives your lists a plural name.

computer_parts = ["Computer",
                  "Mouse",
                  "CPU",
                  "Graphics card",
                  "Monitor"
                  ]
print(computer_parts)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Getting items from a list.
#Lists always start at position 0.

print(computer_parts[0])
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Using accessing lists and using methods.
print(computer_parts[0].upper())
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Accessing the last element in a lists by using -1
print(computer_parts[-1])
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Can you use individual values in a list.
#Using individual values from a list, with in a string, notice how you embrace the variable in curly braces.
print(f"Please by a {computer_parts[2].lower()} when you go to the computer store please.")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#Modifying elements to a lists.
#Replacing an option on a lists, use indexing to replace elements in a list.
computer_parts[0] = "RAM"
print(computer_parts)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#Adding Elements to the end of the lists a list.
computer_parts.append("Mother Board")
print(computer_parts)
