#This is to read the whole text file.
with open("Hello.txt") as file_object:
    contents = file_object.read()
print(contents)

#Breaking down and analysing the code.
#open function, this is used to open files.
#Open function needs one arugment, this the name of the file you want to open.
#as -- Keyword, this will ASSINN it as file_object.
#with closes, the file when it is no longer needed.
#The .read() method is used to read the entire contents of a file.
#There is a difference between .read() and .readlines()
