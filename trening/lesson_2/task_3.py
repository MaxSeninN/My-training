# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month = input('Введите число от 1 до  12: ')
month_dict = {1: 'Зима',
              2: 'Весна',
              3: 'Лето',
              4: 'Осень'}
if month in [1, 2, 12]:
    print(f'{month} - {month_dict[1]} ')
if month in [3, 4, 5]:
    print(f'{month} - {month_dict[2]} ')
if month in [6, 7, 8]:
    print(f'{month} - {month_dict[3]} ')
if month in [9, 10, 11]:
    print(f'{month} - {month_dict[4]} ')
