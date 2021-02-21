current_choice = "-"
computer_list = []
#
while current_choice != 0:
    if current_choice in "12345":
        print(f"Adding {current_choice}")

    else:
        print("Please add an option from the list below")
    print("1: Computer")
    print("2: monitor")
    print("3: Keyboard")
    print("4: Mouse")
    print("5: Mouse Mat")

    current_choice = input("Please add the option you would like ?")
