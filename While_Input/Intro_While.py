#Aim: Asking the user to enter an input.
#Using the input fucntion.
#How to keep program running as long as users want them to.
#So they can enter as much information as they need to.
#######
#######
#Use Pythons while loop to keep programs running as long as certain conditions remain true.
####
###
##########
########
####################### How does the Input function work #############
#Pauses your program. Wait for the user to enter some text.
#Once typed, the input written in assigned to a variable.
####
#Example of using the input function.
message = input("Type a message and i will repeat back to you :D: ")
#
print(message)

##Keep in mind, alway write clear prompts that tell the user what they have to do. Just always add a semi:colon.
#
#Look at how we use to one variable to create a prompt and one to create the user input.
#the Plus input. Uses the += sign, just think about it as being a an add on the prompt.
#We can use a variable to create a prompt to the user to get info from the user.
prompt = "Please can you tell us you name so that we can personalise your name tag"
prompt += "\nWhat is you first name: "
#Interesting.
name = input(prompt)
#
print(f"Hi {name.title().strip()}, thank you for taking the time to get to know and understand the concept at hand. ")

