#Printing variables or using them within strings, can be done in 2 methods.
#f string {}
#.format() method

name ="Josh"
surname ="Mezieres"

#Using the f string method. #Basically using the f string means enclosing the variable in curly braces.
print(f"Hi, my name is {name.upper()} {surname.lower()}")
print("#####################################################")
#Using the .format method.
print("Hi my name is {0} {1}".format(name,surname))
print("#####################################################")
print("#####################################################")

#How can we remove white space from our lines.
#Sometime people my add spaces and we may not want that to be printed you can always use the .strip() .lstrip() .rstrip()
#Dont forget about the parenthesis.
Bestie_Name = input("Name of your best friend: ")
print(Bestie_Name.strip())
print("#####################################################")
print("#####################################################")
print()
#Note that Python sees a diffrence betweeen; white space makes a huge difference.
Lang = "Python "
Lang = "Python" 


#Multiple Assignmetns.
#You can create multiple variable in one go.
#Just make sure that each string and variable listed is seperate by a comma.

Josh, Surname = "Hello", "World "
print(Josh + " " + Surname)
print("##############################")
print()
#You can assign multiple variable to number as well, for example in
x, y, z = 10, 29, 10+30
print(f"My favorite numbers are {x}, {y} and {z}")

