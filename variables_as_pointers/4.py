'''
Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])
'''

# my answer:
'''
42.
because dict2 was constructed with the constructor, it's a shallow copy of dict1. the value of key 'a' is thus a pointer to the original dict1['a'] value, and any mutation to the list will be reflected in dict2.
both dict1['a'] and dict2['a'] are pointing to the same object. 
'''

# model answer:
'''

'''
