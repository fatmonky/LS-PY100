'''
# recursive
def factorial(num):
    if num == 1:
        return 1
    elif num >= 2:
        return num * factorial(num - 1)
# failed iterative answer:
def factorial(num):
    counter = 1
    while num > 0:
        counter = num * (num - 1)
        num -= 1
    return counter
'''
'''
# model answer
def factorial(num):
    counter = 1
    while num > 0:
        counter = num * counter
        num -= 1
    return counter

# model answer using for loop:
def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result
'''

# try 2 on 17 Jul 21
'''
def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result
'''
print('using for loop')
def factorial(num):
    result = 1
    for x in range(num, 0, -1):
        result *= x
    return result

# test
print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000
