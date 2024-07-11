# My answer:
"""
range(5) cannot be used as a dict key, because it's not hashable: it's lazy.
"""

""" Model answer:
['a', 'b']
{'a': 1, 'b': 2}
{1, 4, 9, 16, 25}

Mutable objects can't be used as dict keys. All three are mutable, so can't be used. 

"""
