from math import sqrt

#1
print(sqrt(37))

#2
def root(num):
    return sqrt(num)

print(root(37))

#3
def int_root(num):
    return int(sqrt(num))

print(root(37))

# the question isn't very clear! "Try to write the code inthree different ways" is very vague.

# model answers
#Using the import statement 
import math

print(math.sqrt(37))         # 6.082762530298219

#Using an import alias 
import math as m

print(m.sqrt(37))            # 6.082762530298219
#Using the from statement 
from math import sqrt

print(sqrt(37))              # 6.082762530298219
