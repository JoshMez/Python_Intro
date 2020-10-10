#Passing Arguments.
#
#Functions can define various multiple
#Functions can call multiple arguments.
#

######
#Arguemtnets can be passed in a varitey ways.
##### Positional Arugment ###########
#When you call a function:
    #Python must match each ARGUMENT IN THE FUNCTIONS call with a parameter in the function definition.

#Creating a fucntion of everyone favorite pets
#
#
def describe_pets(animal_type, pet_name):
    """The will just be show a type and name of your pet"""
    print(f"Animal type: {animal_type}")
    print(f"My {animal_type} is called {pet_name}")

#Passing on the argument to the function.
describe_pets('Dog','Kush')
################################################################
################################################################
#Remeber that you can call a funtion as many times as you need.
describe_pets('hamster', 'Bobby')
#
