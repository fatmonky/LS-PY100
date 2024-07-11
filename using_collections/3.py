original = (1, 2, 3, 4, 5)
# turn this into a mutable list
modified = list(original)

# reverse this mutable list
modified.reverse()

# remove first and last elements
## calculate last element from length of collection
last_element_index = len(modified) - 1
## remove last element
modified.pop(last_element_index)
modified.pop(0)

"""
Model answer: use slice as arg for tuple i.e.tuple(modified[1:4])
Very clean!
"""

# turn this into a tuple
modified = tuple(modified)

# print result
print(modified)
