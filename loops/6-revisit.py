my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for num in my_list:
    if num % 2 == 0:
        new_list.append('even')
    elif num % 2 != 0:
        new_list.append('odd')

print(new_list)

# model answers:
# using ternary operator with list comprehension.
result = ['even' if number % 2 == 0 else 'odd'
          for number in my_list]

# using helper function
def odd_or_even(num):
    return 'even' if number % 2 == 0 else 'odd'

result = [odd_or_even(number)
          for number in my_list]
print(result)
