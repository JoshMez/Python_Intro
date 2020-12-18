#Putting the text file in a variable
file_name = "Hello.txt"

#with keyword, used to close a text file when it is not being used.
#open, used to open a file.
#as text_file, ---- > Giving the file that name so that it is processed, with the name its given.

with open(file_name) as text_file:
    lines = text_file.readlines()

#empty string variable.
text_sting = ""
for line in lines:
#Lines from the text file are being
    text_sting += line.rstrip() + "\n"

print(text_sting)
print(len(text_sting))