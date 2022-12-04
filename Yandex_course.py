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


"""# Мухи отдельно котлеты отдельно. Задача T

N = int(input())  # Общий вес котлет                       32
M = int(input())  # Стоимость за кг                        285
K1 = int(input())  # Стоимость первого вида котлет за кг   300
K2 = int(input())  # Стоимость второго вида котлет за кг   240

# Узнать вес первой и второй партии котлет

cost_1 = N * M  # 9120
cost_2 = N * K2  # 7680
weight_1 = (cost_1 - cost_2) // 60  # 24
weight_2 = N - weight_1  # 8
print(weight_1, weight_2)"""


"""color = input()
match color:
    case 'красный' | 'жёлтый':
        print('Стоп.')
    case 'зелёный':
        print('Можно ехать.')
    case _:
        print('Некорректное значение.')"""


"""a = str(input('Как Вас зовут?'))
print(f'Здравствуйте, {a}!')
b = str(input('Как дела?'))
match b:
    case 'хорошо':
        print('Я за вас рада!')
    case 'плохо':
        print('Всё наладится!')"""

"""name_1 = 7
name_1 = name_1 - 3 + 2

name_2 = 6
name_2 = name_2 + 3 + 5 - 2

N = int(input())
M = int(input())

name_1 += N
name_2 += M

if name_1 > name_2:
    print('Петя')
else:
    print('Вася')"""


"""a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    print('NO')"""


"""a = list(str(input()))
b = a[::-1]
if b == a:
    print('YES')
else:
    print('NO')"""


"""a = str(input())
if 'зайка' in a:
    print('YES')
else:
    print('NO')"""


"""i = 0
s = []
while i != 3:
    a = str(input())
    i += 1
    s.append(a)

s.sort()
print(s[0])"""


"""result = list(map(int, input()))  # 123 = 53 Так можно записать список в виде чисел
a = result[2] + result[1]
b = result[0] + result[1]
s = [a, b]
s.sort(reverse=True)
d = list(map(str, s))
print(d[0] + d[1])"""


"""a = list(map(int, input()))

s = min(a)
a.remove(min(a))

d = max(a)
a.remove(max(a))

if s + d == a[0] * 2:
    print('YES')
else:
    print('NO')"""


"""a = int(input())
b = int(input())
c = int(input())

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('YES')
else:
    print('NO')"""


"""a = list(map(int, input()))
b = list(map(int, input()))
c = list(map(int, input()))

if a[0] == b[0] == c[0]:
    print(a[0])
elif a[1] == b[1] == c[1]:
    print(a[1])"""


"""a = list(map(int, input()))

a1 = a.copy()
a1.insert(0, a[0])
result1 = list(map(str, a1))
c = [result1[0] + result1[1], result1[2] + result1[3]]
cols = list(map(int, c))
cols1 = [cols[0] + cols[1]]

a2 = a.copy()
a2.insert(3, a[0])
result2 = list(map(str, a2))
f = [result2[0] + result2[1], result2[2] + result2[3]]
mols = list(map(int, f))
mols1 = [mols[0] + mols[1]]

if cols1 < mols1:
    print(*f)
else:
    print(*c)"""


"""petya = int(input())  # 10  # 7
vasya = int(input())  # 7   # 10
tolya = int(input())  # 5   # 5

if petya > vasya > tolya:
    print('        Петя\nВася\n                Толя\n II      I      III')
elif petya > tolya > vasya:
    print('        Петя\nТоля\n                Вася\n II      I      III')

elif vasya > petya > tolya:
    print('        Вася\nПетя\n                Толя\n II      I      III')
elif vasya > tolya > petya:
    print('        Вася\nТоля\n                Петя\n II      I      III')

elif tolya > petya > vasya:
    print('        Толя\nПетя\n                Вася\n II      I      III')
elif tolya > vasya > petya:
    print('        Толя\nВася\n                Петя\n II      I      III')"""


"""a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c
print(d)
if d < 0:
    print('No solution')
elif d > 0:
    x1 = (-b + d**0.5) / 2 * a
    x2 = (-b - d**0.5) / 2 * a
    print(round(x1, 2), round(x2, 2))
elif d == 0:
    x = (-b + d**0.5) / 2 * a
    print(round(x, 2))"""


"""a = str(input())
while a != 'Три!':
    print('Режим ожидания...')
    a = str(input())
print('Ёлочка, гори!')"""


"""while (a := input()) != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')"""


# Моржовый оператор. Пример с вводом пароля!
while (a := input('Введите пароль: ')) != '123':
    print('Пароль неверный, введите еще раз!')
print('Добро пожаловать в систему!')







