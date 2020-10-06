#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.
#
#
People = { 'Person_1' : { 'First Name': 'Joshua',
                          'Last Name': 'Mez',
                          'age': 24,
                          'City': 'Perth'
                        },

           'Person_2' : {'First Name': 'Rachel',
                         'Last Name': 'Mos',
                         'age': 26,
                         'City': 'Perth'},

           'Person_3': {'First Name':'Phil',
                        'Last Name': 'Lawerenc',
                        'age': 56
                        'City': 'Mels'},

}

#
for people, Person_Info in People.items():
    print(f"Your first name is {Person_Info['First Name']} ")
    print(f"Your last name is {Person_Info['Last Name']} ")
    print(f"You are were born in {Person_Info['City']}")
    print()