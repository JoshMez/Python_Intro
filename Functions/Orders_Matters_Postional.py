#Creating a function where indication of displaying the order matters.
#
#creating a definiton.
def pet_name(animal_type, animal_name):
    """Function will display pet name and type."""
    print(f"Pet type: {animal_type}")
    print(f"Animal type: {animal_name}")
#Calling the function
pet_name("Dog", "Kush")
#######
######
#Look at the difference of the outcome.
#Postitional parameter matter.
pet_name('Kush', 'Dog')
