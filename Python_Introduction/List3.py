#Oragnising lists.

#Using the sort method()
name_of_loved_ones = [ "Joshua",
                       "Rachel(Babes)",
                       "Christina",
                       "Savy",
                       "Brian",
                       "Belle",
                       "Brain"
                       ]

#Sorting lists Alphabetically
name_of_loved_ones.sort()
print(name_of_loved_ones)

#In a reverse order, pass an argument to the .sort() method.
name_of_loved_ones.sort(reverse=True)
print(name_of_loved_ones)
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print()
#Creating a new lists.
Sports = [ "Martial Arts", "Soccer", "Tennis", "Rugby", "Footy"]

#Display a list in Order for a particular moment.
print(sorted(Sports))

#Reversing the order of the list, but NOT, I MEAN NOT.
print(Sports.reverse()) #Looks like you need to do stage to 1st be

Sports.reverse() #Stage 1, state that you want the list to be in a reverse order.
print(Sports)
