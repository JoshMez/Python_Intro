#Aim, Track the position of a alien that can move at different speeds,
#
#
alien0 = {'x-position': 0,
          'y-position' : 25,
          'speed' : 'medium'
          }
#Want the key value to be a variable.
origina_Pos = alien0['x-position']
#
#Original Position of the ship.
print(f"The original position of the ship is {origina_Pos}")
#
#
#ALien needs to move right.
#Depeding on speed, will determine the its increment size.
#
speed = alien0['speed']

#Using an if statment to test the speed.
#Speed tested will determing the increment.

if speed.title() == 'slow' or speed.upper() == 'slow'  or speed == 'slow':
    #Creating a variable called increment.
    increment_x = 2
elif speed == 'medium':
    increment_x = 3
else:
    increment_x = 4
#Increment is add to the original position.
print(f"The new alien speed is {origina_Pos + increment_x}")
