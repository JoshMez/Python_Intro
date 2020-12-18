files_name = "Hello.txt"
#
with open(files_name) as file_objects:
    for line in file_objects:
        print(line.rstrip())

#Breaking down and analysing the code.
#Variable file name has been given, to store the file name.
#with, used to close the file when it is not needed.

"""Note how: there is not .read() used here. 
We are reading line by line and not the entire file"""
