#8-1. Message: Write a function called display_message() that prints one sentence
#telling everyone what you are learning about in this chapter. Call the
#function, and make sure the message displays correctly.

#Creating a function.
def display_message():
    """Displaying the chapter focuses on"""
    print("In this lesson, the focus is on functions.")

#Calling the functions
display_message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one
#parameter, title. The function should print a message, such as One of my
#favorite books is Alice in Wonderland. Call the function, making sure to
#include a book title as an argument in the function call.
#
#Supplying one parameter
def favorite_book(book):
    """Showing my favorite book"""
    print(f"My fav book is {book.title()}")

#Calling the function along with an argument.
favorite_book("alice in wonderland\n\n")


#8.3
#Defining a function called make_shirt()
def make_shirt(size, message):
    """This is the size of the t-shit"""
    print(f"Size {size}")
    print(f'{message}\n')

make_shirt('M', "Being successful means SECOND BY SECOND")
######
#####
#8.4
def make_shirt(size='large', message='I love Python'):
    """New print """
    print(f"Size: {size}")
    print(f"{message}\n")

#Calling the function
make_shirt(size='M', message='One second at a time is how you build success.')
######
#8.5
#Creating a function.
def describe_city(city, country="Iceland"):
    """Tells you where you statement is """
    print(f"Josh is currently in {city} which is in the {country}")

#Using the definition.
describe_city('Gaborone', country='Botswana')
