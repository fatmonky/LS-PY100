def find_integers(tup):
    int_list = []
    index = 0
    while index < len(tup):
        if type(tup[index]) is int:
            int_list.append(tup[index])
        index += 1
    return int_list

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
