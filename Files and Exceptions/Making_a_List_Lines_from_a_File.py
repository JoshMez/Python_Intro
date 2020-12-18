file_name = "Hello.txt"
#
with open(file_name) as file_object:
#reading the entire file
    lines = file_object.readlines()

#Want to work with the text files outside the with statment.
for line in lines:
    print(line.rstrip())