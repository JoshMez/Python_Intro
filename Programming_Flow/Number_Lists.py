#Creating lists that contain number in Python is very important. 

#Making a list with even numbers in it. 
even_numbers = list(range(0,11,2)) #The list function has been used to say that a lists is being created. #Passing the range arguments in that , stating arugments in that. 
print(even_numbers)  

#Creating a list , with a range of number in them.

#Creating a list of numbers.
numbers = list(range(1, 20+1))

#Printing the list that was created.
print(numbers)

lists = []  #Do not give you variable key definitions.

#Want to create a list of all square numbers, in the given range.
for number in numbers:
    lists.append(number ** 2 ) #Number is our temporary variable.
print(list)


print( "*" * 100)
print()
print("This part will focus on functions that are useful when working with lists.")

#Using the min function in A LIST OF numbers.
numbers2 = list(range(1 ,30 + 1 ))
print(numbers2)
min_numbers = min(numbers2)
print(min_numbers)

#Using the max function to find the maximum amount of numbers in a lists.
numbers3 = list(range(1,21))
print(numbers3)
print(max(numbers3))

#Calculating the sum of number in a lists.
numbers4 = list(range(1, 25))
print(numbers4)
print(sum(numbers4))
