#Aim: How to use the flag.
#
#You can define a variable, that determine whether or not THE ENTIRE PROGRAM IS ACTIVE OR NOT.
#Varaible is called a flag- Acts as signal toward the prgrom as to whehter

prompt = "Tell me something and i will repeat back to you. "
prompt += "\nI really do work"
prompt += "\nType 'quit' to stop the program: "
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        print("You have successfully quit the program.")
        active = False
    else:
        print(message)