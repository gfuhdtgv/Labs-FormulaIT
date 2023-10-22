money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget = salary+money_capital
nodebt = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    budget -= spend
    spend *= 1+increase
    if budget < 0:
        break
    nodebt += 1
    budget += salary

print("Количество месяцев, которое можно протянуть без долгов:", nodebt)
