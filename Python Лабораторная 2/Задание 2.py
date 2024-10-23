salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0
for month in range(months):
    ost = salary - spend
    spend = spend * increase + spend
    money_capital = (ost * -1) + money_capital
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
