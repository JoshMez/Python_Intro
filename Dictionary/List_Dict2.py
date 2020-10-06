#Putting a list in a dictionary
#
#You can use a list if you need to store values in your list.
#
favorite_language = { 'Jason': ['python', 'r'],
                      'Mason': ['java' , 'C#'],
                      'edward': ['javascript'],
                      }




#Printing keys and value in a list.
for name, lang in favorite_language.items():
    if len(lang) >= 2:
        print(f"Hi {name}, your favorite programming languages are:")
        for langs in lang:
            print('\t*'+langs)
################
#########################
################
#########################


