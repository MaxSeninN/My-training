# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

name = 'Max'
print(name)

var = int(input('Введите время в секундах: '))
hour = var // 3600
minute = var // 60 % 60
sec = var % 60

print(minute)
print(hour)
print(sec)
print(f'{hour:02d}:{minute:02d}:{sec:02d}')