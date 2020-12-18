#Writing to an an empty file.

file_name = "write.txt"

with open(file_name, 'w') as write_object:
    write_object.write("I love programming")

#Reading the file line by line.
with open(file_name) as read:
    for reading in read:
        print(reading)


#You can open a file in 'w' - write mode, 'r'-read mode, 'a' - append mode.  r+ --- this is to read and write to a file.



