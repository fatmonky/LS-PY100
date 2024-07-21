my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
# print all even numbers without any for loops.

list_index = 0
elem_index = 0
while list_index < len(my_list):
    while elem_index < len(my_list[list_index]):
        if my_list[list_index][elem_index] % 2 == 0:
            print(my_list[list_index][elem_index])
        elem_index += 1
    elem_index = 0
    list_index += 1
