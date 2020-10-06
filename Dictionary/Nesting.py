#Nesting.
#
#This implies that you can:
    #Store dictionaris in a list.
    #List items in a dictionary.
    #Dictionary in another dictionary.

#
#
#Making a list of dictionaries.
#Creating a multiple lists about the type of aliens.
#
alien_0 = {'color': 'green',
           'points': 5
           }
#
#Creating alien_1
alien_1 = {'color': 'yellow',
           'point': 10
           }
#
#Creating alien_2
alien_2 = { 'color': 'red',
            'points': 15
            }
#############
#Creating a dictionary and storing all the dictionary values.
#Want to store all the Info about aliens in a general aliens list.
aliens = [alien_0,
         alien_1,
         alien_2
         ]
########
########

for alien in aliens:
    print(alien)
################
    #########
#
