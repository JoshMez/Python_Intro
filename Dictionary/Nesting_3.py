#Making an empty list.
aliens = []
#
#Making  30 aliens
for alien in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'
                 }
    aliens.append(new_alien)

#####################
######################
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
#

#SHowing the 1s 5 lines.
#
for alien in aliens[:5]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

print(aliens[0:5])
