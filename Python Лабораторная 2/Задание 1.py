money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
all_capital = salary + money_capital
month = 0
while spend < all_capital:
    all_capital -= spend
    month += 1
    spend = (spend * increase) + spend
    all_capital += salary

print("Количество месяцев, которое можно протянуть без долгов:", month)
