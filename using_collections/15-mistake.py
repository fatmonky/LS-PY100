"""
Without running the following code, what values will be printed by line 10?
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# My answer: there should be an error, due to line 26 not properly done.

"""

# Running the code in command line to see if answers above are right
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

#model answer:
# dict_keys(['Cat', 'Bird', 'Snake'])
