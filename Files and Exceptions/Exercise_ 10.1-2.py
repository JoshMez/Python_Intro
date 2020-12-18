#Storing the Python text files in a variable.
file_name = "Python.txt"
#
#Reading the entire files using .read()
with open(file_name) as text_file:
    text = text_file.read()
print(text)
#####
#Looping over the lines.
with open(file_name) as text_file:
    for text in text_file:
        print(text.strip())
#
#.readlines()
with open(file_name) as file:
    content = file.readlines()

for contents in content:
    print(contents)
"""Completed."""
print(str("*" * 50 + " Exercise 10.1 completed " + "*" * 50) )
#
#Using the replace function.
#The aim in is to replace Python with C

with open(file_name) as python:
    for py in python:
        if "Python" in py:
            #Replacing all instances of Python with C.
            print(py.replace("Python", "C"))