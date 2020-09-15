#Using the range function.
#Think of the range function of being, up to but not including as in, the last number stated is not used.
#When using the range function, by default the count starts at 0 if not stated.

#Create a variable using the range function.
values = range(1, 20) #The range will start at 1 and end at 20, but 19 will be printed.

values2 = range(0,21,2) #Creating a range that will be counted in two.

#Using a for loop to print all the numbers in the value range.
for value in values:
    print(f"{value}")
print("Print numbers in order from 1 to 20")
print()
#
print()
for values2 in values2:
    print(f"{values2}")
print("The even numbers from 0 to 20 have been printed. ")
print()
