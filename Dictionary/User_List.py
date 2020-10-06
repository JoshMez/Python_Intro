#Creating a dictionary within a dictionary.
###
#
# Creating a dictionary with mulitiple users.
users = { 'Eean': {
    'First_Name': "Rina",
    'Last_Name': "Seena",
    'location': "Perth"
}, #When you start a second dictionary, start a of with a comma.
    #Creating the second dictionary put a semi-colon.
    'Jason': {
        'First_Name': "Jason",
        'Last_Name': "Lang",
        'location': "Tsu"
    }  , #Put a comma at the end.
}
##################################################
##################################################
##################################################
#Want to print out user info.
#
for user,Userinfo in users.items():
    print(f"Your user name is {user}")
    location= Userinfo['location']
    print(f'Your current location is {location}')
    print()
