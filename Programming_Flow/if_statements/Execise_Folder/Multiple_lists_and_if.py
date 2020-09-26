#Using multiple lists.
#Lesson learned:
#You can use multple lists in programme.
#You can use them together.

requested_toppings = ["French fries",
                      "Chicken",
                      "Feta"]

Avaliable_toppings = [ "French fries",
                       "Chicken",
                       "chillies"
                       ]
print("The Avaliable toppings from your choice are: " )
for Avaliable_topping in Avaliable_toppings:
   if Avaliable_topping in requested_toppings:
       print ( f"{Avaliable_topping}" )
   else:
       print(f"We do not have the topping {Avaliable_topping}")