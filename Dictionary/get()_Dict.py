#Using the .get method.
#Used specifically for dictionaries.
#
#
#Sometimes you need to use the .get() to see if a value exits.
#So it goes like this.
#
Car_Colors = {'Honda': 'Black',
              'Toyota' : 'Pink',
              'Audi': 'Ruby Red'}
#Want to see if there is a value for Honda.
V_H = Car_Colors.get('Honda', 'No value assigned')
#
print(V_H)
#Want to see if there is a value for Mercedes
#Notice how the 1st argument taken is the Key of the value you are looking for.
#Then: You put a default statement that goes with it at times.
#
V_M = Car_Colors.get('Mercedes', 'No point value assigned.')
print(V_M)
#
#
