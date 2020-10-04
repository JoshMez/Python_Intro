#Looping through keys ONLY in a dictionary.
#.keys() methods along with dictionary.
#
#
#Creating a dictionary: Name and Colors.
#
Name_Color = {'Joshua' : 'Black',
              'Jason' : 'Pink',
              'Brian' : 'Red'
              }

#To loop through the keys you need to use the .keys() methods
#Using a for loop to dislplay the keys only.
for Name in Name_Color.keys():
    print(f"The following key in the dictionary is {Name}")
###
#Alternatively you dont have to use it because it is the default one at times .
for Name in Name_Color:
    print(f"The following key in the dictionary is {Name}")
#Notice that 