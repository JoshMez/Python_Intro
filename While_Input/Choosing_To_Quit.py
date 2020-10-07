#Aim: Letting the user choose when they want to quit,.
#
#
Intro_Message = "Tell me something and i will repeat it back to you ?"
Intro_Message += "\nTrust me, i really will repeat what you say: "
#
#Creating an empty string
message = ""

#Creating a quit message.
cancel ="quit"

while message != cancel.casefold() :
    message = input(Intro_Message)

    if message == cancel.casefold():
        print("You can successfully quit the program.")
