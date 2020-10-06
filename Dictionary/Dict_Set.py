#This following programme aims at using the set function as a means of only seeing and viewing unique values.
#
#Creating the a dictionary of peoples name and programming languages.
#
Name_Lang = {'Joshua': 'python',
             'Jason': 'c++',
             'Huey' : 'python',
             'savy': 'c#',
             'David': 'c++'
             }
##################
#################
#
print("The Programming languages are : ")
for lang in Name_Lang.values():
    print(lang)
print('**' * 50)
#######
#
#Using the set function to make sure that there are only unique values.
for lang in set( Name_Lang.values()):
    print(lang)
#Notice how the value of only type of lang has been listed.
