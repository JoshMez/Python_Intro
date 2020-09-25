#Aim: Using an if-elif-else statemen.
print("""This programme will decide at which stage of life you are in. 
A user input prompt will be provide you to type in your age. 
""")
print()
#
age = int((input("Please enter your age (Number only): ")))
#
if age < 2:
    print("You are a baby")
elif (age >= 2) and (age < 4):
    print("You are a toddler")
elif (age >= 4) and age < 13 :
    print("You are a kid")
elif (age >= 13) and age < 20:
    print("You are a teenager")
elif (age >= 20) and age < 65:
    print("You are an adult")
elif age >= 65 and age < 150:
    print("You are elder")
elif age <= 900:
    print("You are Master Yoda")

