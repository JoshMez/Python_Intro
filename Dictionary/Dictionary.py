#Aim: Create a simple dictionary.
#

#################################################################
#################################################################
#In python, think of a dictionary as a pair of key-value pairs.
#A key is connected to a value.
#Use the key to acess the value.
#A keys value can be a:
        #1)Number
        #2)String
        #3)List
        #4)Dictionary
        #5)BASICALLY you can use any object.

#Syntax for a dictonary. {}
#There must be key-pair value with-in the curly braces.
#What are key-pair values.
#There is NO LIMIT to the key pair values you can store
#Key-pair value: Values associated with each other.
#
#Every KEY PROVIDED must be provided.
#Keys and Values are CONNECTED BY A COLON.
#ONE key-values are separated by another by using COMMA's.
#################################################################
#################################################################
#Example of a dictionary.
#{} Marks a distionary.
#Printing on the key value using []
#
alien_0 = {'color': 'green',
           'points': 5
           }
#
print(alien_0['color'])
print(alien_0['points'])
print("*" * 75, "\n\n\t\t\t\t\t\tFinshed\n\n","*" * 75)
print()
print()
#
#Creating a dictionary.
People_Fav_Color = {'Josh' : 'Green',
                    'Kevin': 'Purple',
                    'Rach': 'Pink'
                    }
#
#
#Printing the key value.
Josh_Key_Value = People_Fav_Color['Josh']
#
print(Josh_Key_Value)