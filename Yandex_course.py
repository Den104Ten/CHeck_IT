"""
# 1001001
# 100

cost = str(input())  # Цена покупки в двоичном формате
c = (int(cost, base=2))

bill = int(input())  # Номинал купюры

print(bill - c)"""


"""#  Украшение чека. Задача S

name = str(input())
cost_kg = int(input())
weight = int(input())
money = int(input())

#print(f'Товар:{" "*(29 - len(name))}{name}')
print(f'{"="*16}Чек{"="*16}')
print(f'Товар: {name}')
print(f'Цена: {weight}кг * {cost_kg}руб/кг')
print(f'Итого: {weight * cost_kg}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {money - (weight * cost_kg)}руб')
print('=' * 35)"""


# Мухи отдельно котлеты отдельно. Задача T

N = int(input())  # Общий вес котлет                       32
M = int(input())  # Стоимость за кг                        285
K1 = int(input())  # Стоимость первого вида котлет за кг   300
K2 = int(input())  # Стоимость второго вида котлет за кг   240

# Узнать вес первой и второй партии котлет

