def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Qn 15:
# multiply: global
# left, right: local to multiply
# get_num: global
# prompt: local to get_num
# float, input: built in
# first_number: global
# second_number :global
# product: global
# print: built in


# Qn 16:
"""
function names: multiply (line 1, 9), get_num(line 4, 7,8)
# correction: left out built-in functions.
float, input on line 5
print on line 10.

parameters: left, right (line 1), prompt (line 4)
"""


