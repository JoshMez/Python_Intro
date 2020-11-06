#Creating a function
def fav_food(item_1, item_2, item_3,bonus=''):
    """This will list your favorite food."""
    #Creatinga a list.
    foods = [
        f"{item_1}",
        f"{item_2}",
        f"{item_3}",
        f"{bonus}"
    ]
    print("Your like the following foods: ")
    for food in foods:
        print(f"*){food.capitalize()}")


fav_food("Apples", "Bananas", "Pears")

#Calling function with optional arugment
fav_food("Apples", "Bananas", "Pears", "Milk")

