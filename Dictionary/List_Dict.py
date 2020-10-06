#Sometimes if can be useful to store a list in a dictionary.
#
#
#We want to store information about a type of pizza that is being stored.
#
#Creating a dictionary
pizza = { 'Crust': 'thick',
          #Take note how a list is being created in a the dictionary.
          #The list has become the key value in this scenario.
          'toppings': ['mushrooms', 'Ham']
          }
#Summarising the pizza value.
print(f"The crust you ordered is {pizza['Crust']}.")
print("You ordereed the following toppings: ")

for topping in pizza['toppings']:
    print("*" + topping)