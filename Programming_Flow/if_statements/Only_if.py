#You can omit the else block if you want specific condition to be met.
#
#This can be a good way to stop malicious code.
#
#Sometimes using an if statement by itself is beneficial if you wish to test for ONLY ONE CONDITION.
#
#Looking at a pizza request.
#
Pizza_Toppings = [ "Mushrooms",
                   "Extra Cheese"]

if "Mushrooms" in Pizza_Toppings:
    print("Adding Mushrooms.\n")

if "Extra Cheese" in Pizza_Toppings:
    print("Adding Extra cheese.\n")

if "Pepporoni" in Pizza_Toppings:
    print("Adding Pepporoni.\n")
print("We are done making your Pizza :D")