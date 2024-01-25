#Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
#финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
#или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
#прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
#фирмы в расчёте на одного сотрудника.

revenue = float(input('Укажите прибыль компании: '))
costs = float(input('Укажите издержки компании: '))
profit = revenue - costs
if profit > 0:
    print(f'Прибыль компании составила: {profit}')
    profitability = revenue / profit
    profitability = round(profitability, 2)
    print(f'Рентабельность компании: {profitability}')
    employee = int(input('Укажите количество сотрудников: '))
    profitability_one_emloyee = profit / employee
    profitability_one_emloyee = round(profitability_one_emloyee, 2)
    print(f'Прибыль компании на каждого сотрудника составила: {profitability_one_emloyee}')
elif profit < 0:
    profit = profit * (-1)
    print(f'Убыток компании составил: {profit}')

