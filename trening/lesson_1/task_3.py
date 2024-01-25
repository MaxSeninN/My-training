# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Введите целое положительное цисло: '))
result = 0  # самое большое число в переменой num
if num == 0:
    print(num)
elif num < 10:
    print(num)
elif num >= 10:
    while num != 0:
        if result <= num % 10:
            result = num % 10
            num = num // 10
        else:
            num = num // 10
    print(result)
