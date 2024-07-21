'''
original code:
import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
'''

# refactored code 17 Jul 24
'''
import random

highest = 10
number = 1

while number != highest: 
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break
'''
# model answer:
import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break
