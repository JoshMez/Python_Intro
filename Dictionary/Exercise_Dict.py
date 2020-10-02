print("""Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.""")
print()
print()
#Creating a dictionary.
Personal_Info = {'First_Name' : 'Kaneki',
                 'Last_Name' : 'Ken',
                 'City' : 'Tokyo',
                 'Age' : 25
                 }
Name = Personal_Info['First_Name']
Surname = Personal_Info['Last_Name']
Age = Personal_Info[ 'Age' ]
City = Personal_Info['City']
#
print(f"The suspects first name is : {Name}\nLast name is: {Surname}\nAge is {Age}")
print(f"City : {City}")
#
print()
print()
print()
print()
##############
##############
print("""Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.  
Think of a favorite number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program. """)
#
#Creating a dictionary with everyone's fav numbers.
#
Names_Num = {'Mikasa': 25,
             'Levi': 32,
             'Eren': 24,
             'Erwin': 34,
             'Luqui' : 28
             }
#
#
Mikasa_Num = Names_Num['Mikasa']
Levi_Num = Names_Num['Levi']
Eren_Num = Names_Num['Eren']
Luqui_Num = Names_Num['Luqui']
Erwin_Num = Names_Num['Erwin']
#
#
print()
print(f"Mikasa's fav number is {Mikasa_Num}")
print(f"Levi's number is {Levi_Num}")
print(f"Eren's fav number is {Eren_Num}")
print(f"Erwin fav number is {Erwin_Num}")
print(f"Luqui fav number is  {Luqui_Num}")
#
#
print()
print()
print("""6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output""")
print()
#Creating a dictionary(Glossary)
dict_f = {'Chapter_1': 'variable',
          'Chapter_2': 'list',
          'Chapter_3': 'if',
          'Chapter_4': 'for',
          'Chapter 5': 'Dictionary'
          }
#
#
#
chap_1 = dict_f['Chapter_1'].title()
chap_2 = dict_f['Chapter_2'].title()
chap_3 = dict_f['Chapter_3'].title()
chap_4 = dict_f['Chapter_4'].title()
chap_5 = dict_f['Chapter 5'].title()
#
#
print(chap_1 + "\nStores data.\n\n")
print(chap_2 + "\nThis can stores many types of data\n\n")
print(chap_3 + "\nUsed to test specific conditions within a programme\n\n")
print(chap_4 + "\nUsed to loop through lists, dictionaries or something else.\n\n")
print(chap_5 + "\nStores key pair values\n\n")



