# Write Python code to replace all the : characters in the string below with +.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

"""
Try this problem using the methods you've learned about in this chapter. Once you have that working, use the Python documentation for the str type to find an alternative solution.
"""

# my working
working_list = info.split(':')
result = '+'.join(working_list)
print(result)

# additional way using str.replace method
other_result = info.replace(':', '+')
print(other_result)
