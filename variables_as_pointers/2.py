'''
Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)
'''

# my answer 18 Jul 24
'''
{42, 'Monty Python', ('a', 'b', 'c'), 5, 6, 7, 8, 9}
Because set2 points to set1's object, which has been mutated by line 3 with the range.
'''

# model answer:
# The order of the elements probably won't match,
# but the 4 elements shown here should all be
# present in your answer.
# {('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}

# personal note: forgot that ranges are lazy!
