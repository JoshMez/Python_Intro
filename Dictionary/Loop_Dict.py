#Aim: Explain Loop and Dictionaries.
#
#
#There are several ways to loop through a dictionary.
    #Loop through all of Key-pair values.
    #Loop through keys only.
    #Loop though values only.
#
#
############Example of looping through all dictionary key-pair values####################
#
#Creating a dictionary of a User information.
User_0 = {'username': 'jmez',
          'first name' : 'Josh',
          'Last name' : 'Mezieres'
          }
#Loop through all key-value pair info
#The for loop will contain 2 variable.
#One variable --- The one which comes first represent the Key
#after 1st varaible stated, a comma comes in straight afterwards.
#Then a second variable will be used to define the key.
#Seeing as loop is going through 2 variables. - Add .items(), after the dictionary.
#
for user_cat, info in User_0.items():
    print(f"Key: {user_cat.title()}")
    print(f"Info: {info}\n\n")
#
#
#
#Think about dictionaries working well for working well with pairs.
#Creating a dictionary with peoples name and programming languages.
Names_Lang = {'jane': 'c',
              'arkus': 'python',
              'allistair': 'ruby'
              }
#
for Name, lang in Names_Lang.items():
    print(f"{Name.title()}'s favourite programming language is {lang.title()}\n")
###############

