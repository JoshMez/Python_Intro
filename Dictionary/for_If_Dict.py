#Using the for, if, and list, and dictionary all in one script.

##
#Creating a list of everyones favorite programming languages.
#
Name_Lang = { 'Sam': 'c' ,
              'Jason': 'python',
              'Belle': 'Ruby',
              'Brian': 'java'
}
############
friends = ['Sam',
           'Jason']
#############
#Creating a for loop to print out the keys only in the dictionary.
#
for Name in Name_Lang.keys():
    print(f"Hi {Name}")
    if Name in friends:
        #Because its a variable, you dont have to put it in double quotes.
        langauge = Name_Lang[Name]
        print(f'Hi {Name} you favorite programming language is {langauge}\n')