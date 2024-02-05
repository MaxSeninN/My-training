# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

# numbers = list(map(int, input('Введите числа: ').split()))
# print(numbers)
exit_prog = '-'
sum_of_numbers = 0
# if exit_prog in numbers:
#     print('вышел')
numbers = []
while True:
    numbers = list(input('Введите числа: ').split())  # запрос у пользователя
    print(numbers)
    if exit_prog in numbers:
        numbers = map(int, numbers[:-1])
        print(numbers)
        sum_of_numbers = sum_of_numbers + sum(numbers)
        print(sum_of_numbers)
        print('Программа завершена')
        break
    numbers = map(int, numbers)
    sum_of_numbers = sum_of_numbers + sum(numbers)
    print(sum_of_numbers)
