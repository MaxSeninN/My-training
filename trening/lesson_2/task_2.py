# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input()

new_list = list(input('Введите список элементов: '))
if len(new_list) % 2 == 0:
    new_list[::2], new_list[1::2] = new_list[1::2], new_list[::2]
print(new_list)
if len(new_list) % 2 != 0:
    new_list[:-1:2], new_list[1:-1:2] = new_list[1:-1:2], new_list[:-1:2]
print(new_list)