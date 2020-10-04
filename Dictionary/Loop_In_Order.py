#You can use the sorted functions for sort a list
#Using the sort function with in a loop
#
#Creating the dictionary with NAmes and peoples favorite programming languages.
#
favorite_languages = {'Josh': 'python',
                      'Abella' : 'Java',
                      'Melly': 'C'
                        }
#
#Notice how everything is sorted in Alphabetical Order.
for name in sorted(favorite_languages.keys()):
    print(f"Hello {name}")
##
#
