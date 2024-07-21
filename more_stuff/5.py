'''
On reflection, we've decided that we don't want to rely on using a global variable in the code we wrote in the previous example. To fix this, we're going to nest the code from the previous example into an outer function:

def all_actions():
    counter = 0

    def increment_counter():
        global counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()
There's a bug in this code. Identify the bug, and fix it.
'''

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter #global causes this to search for counter as a global variable. But counter was not defined at the global level, but the next scope. So changing this to nonlocal solves the problem. 
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()
