#Return dictionary.

#Creating a function.
def build_person(first_name, last_name):
    """Returning a dictionary"""
    person = {
        "First_name": first_name,
        "Last_Name:": last_name,
    }

    return person
#######
musician = build_person("Jimi", "Hendrix")
print(musician)