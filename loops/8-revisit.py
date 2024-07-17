my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

# Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

# my answer
'''
my_dict = {key: value
           for key in my_set
           if value % 2 != 0}
'''

# answer after looking at solution
my_dict = {key: len(key)
           for key in my_set
           if len(key) % 2 != 0}

print(my_dict)
