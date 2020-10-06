aliens = []

#Basically creating the variable 30 times over.
#
#The range just tells Python how many times we want to loop and repeat.
#Each time loop occurs, we create a new alien and append it to the new alien list.
for alien in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'
                 }
    aliens.append(new_alien)
#Using slicing to get the the 1st liness of the list.
for alien in aliens[:5] :
    print(alien)
########
#How many aliens are there in the list.
print(f"The amout of alients in the list are {len(aliens)}" )
#
#

