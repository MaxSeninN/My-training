def my_func(ar_1, ar_2, ar_3):
    my_list = [ar_1, ar_2, ar_3]
    my_list.sort()
    return my_list[1] + my_list[2]
print(my_func(1, 1, 11))