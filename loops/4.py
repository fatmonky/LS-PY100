my_list = [6, 3, 0, 11, 20, 4, 17]

# even numbers while loop
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

# odd numbers for loop

for element in my_list:
    if element % 2 != 0:
        print(element)
