#if-else
#Aim: Using the else statement if the condtion you are testing fails.
#
#
print("Simple programming to see if you are old enough to vote.\n")
age = int(input("Enter your age (numbers please): "))
print()
if age >= 18:
    print("You are old enough to vote.")
    print("Please remember to register.")
#Else is used when the conditon you are testing for does not meet the criteria.
else:
    print(f"You are not old enough to vote\nYou can vote in {18 - age } years")
    
print("\n", "*" * 50,
      "\n",
      "\t\t\t\t\t3Finished",
      "\n",
      "*" * 50,
      )
