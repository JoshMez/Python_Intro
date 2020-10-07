#Removing All instances of specific values from a list.
#
#what if you want to remove all instances from a list.
#
pets = ['dogs',
        'cats',
        'dog',
        'goldfish',
        'cats',
        'rabbit',
        'cats']
#
while 'cats' in pets:
    pets.remove('cats')
    continue    
print(pets)
#Note how all instances of cats have been removed.