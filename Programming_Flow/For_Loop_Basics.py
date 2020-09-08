#Looping through an entire lists.
#When you want to do the same thing with every item in list you can use the for the loop.
#Why you a for loop, cauese it will save us time

#Creating a list of hereos.
Heroes = [ "iron man", "black panther", "mandela", "muhammed ali"]

#For loop.
#Creating the for loop .
#Basically telling Python than every hero in the heroes list
for Hero in Heroes:
    print(Hero) #Stating what we want the for loop to do.
    print()
#Breaking down the for loop.
    #Telling Python,  that we want to take the 1st item from the Heroes lists.
    #Then store it in the variable Hero.
    #The for will then print that value, only because we have stated that it should be printed.
    #These items from the lists are temporarly stored in the variable, you have provided.
    #Better to use singular names in the for loop.

#Doing more work in the for loop
for Hero in Heroes:
    print(f"{Hero.title()}, really helps me to be a great and better person")
    print()
    #Take notes that indentation plays a really big roll here.




#Show a bit of favoritism
for Hero in Heroes:
    print(f"{Hero.title()}, really helps me to be a great and better person")
    if Hero.casefold() == "black panther":
        print("RIP Chadbosman\n\n")
        print()
