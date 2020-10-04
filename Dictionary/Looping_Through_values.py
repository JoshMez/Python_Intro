#Looping to only show the key values.
#Aim: To Only show value values.
#
#
Name_lang = {'Jason' : 'Python',
             'Kenny' : 'Bash',
             'Kevin' : 'C'
           }
###
print("The following languages which have been mentioned are : ")
print()
for lang in Name_lang.values():
    print("*"+ lang)