#More on lists. 
#You can create an empty lists and append items to it. 
#Create an empty lists. 
fav_cars = []

#appending items to an empty list.
fav_cars.append("Honda")
fav_cars.append("Lambo")
fav_cars.append("Honda Civic")

#Printing out the new list.
print(fav_cars)
print("########################")
print()
#Inserting elements into a lists at any postiion, just be mindful of the syntax and structure.
#When inserting the structure, always put the INDEX NUMBER
fav_cars.insert(0, "Tesla".upper())
print(fav_cars)

#Removing items from a lists. #When removing an item from a list, used del <list_name>[INDEX_POSITION] <-
del fav_cars[0]
print(fav_cars)
#Key word to remeber here is: "del"
del fav_cars[-1]
print(fav_cars)
