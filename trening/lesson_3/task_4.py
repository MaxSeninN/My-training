# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func_2(x=0.1, y=-1):
    x = float(input('Введите действительное положительное цисло: '))
    y = int(input('Введите целое отрицательное число: '))
    return x ** y


print(my_func_2())


def my_func_3(x=0.1, y=-1):
    x = float(input('Введите действительное положительное цисло: '))
    y = abs(int(input('Введите целое отрицательное число: ')))
    x_1 = x
    n = 1
    res = 0
    while n != y:
        res = 1 / (x_1 * x)
        n += 1
        x_1 = (x * x_1)
    return res


print(my_func_3())
