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

"""a = list(map(int, input()))\n"
 "\n"
 "a1 = a.copy()\n"
 "a1.insert(0, a[0])\n"
 "result1 = list(map(str, a1))\n"
 "c = [result1[0] + result1[1], result1[2] + result1[3]]\n"
 "cols = list(map(int, c))\n"
 "cols1 = [cols[0] + cols[1]]\n"
 "\n"
 "a2 = a.copy()\n"
 "a2.insert(3, a[0])\n"
 "result2 = list(map(str, a2))\n"
 "f = [result2[0] + result2[1], result2[2] + result2[3]]\n"
 "mols = list(map(int, f))\n"
 "mols1 = [mols[0] + mols[1]]\n"
 "\n"
 "if cols1 < mols1:\n"
 "    print(*f)\n"
 "else:\n"
 "    print(*c)"""

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
"""while (a := input('Введите пароль: ')) != '123':
    print('Пароль неверный, введите еще раз!')
print('Добро пожаловать в систему!')"""

"""zaika = 0
while (a := input()) != 'Приехали!':
    if 'зайка' in a:
        zaika += 1
print(zaika)"""

"""a = int(input())
b = int(input())
if b < 0:
    for i in range(a, b - 1, -1):
        print(i, end=' ')
elif a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')"""

"""f = 0
while (a := float(input())) != 0:
    if a >= 500:
        d = (a * 90) / 100
        f += d
    else:
        f += a
print(f)"""

"""a = int(input())
b = int(input())
a1 = a
b1 = b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

c = a + b
print(a1 * b1 // c)"""

"""a = str(input())
b = int(input())

i = 0
while i != b:
    print(a)
    i += 1"""

"""import numpy as np
a = int(input())

i = 1
z = []
for i in range(a):
    c = (i + 1)
    z.append(c)
print(np.prod(z))"""

"""while (a := str(input())) != 'СТОП':
    b = int(input())
    if a == 'СЕВЕР':
        pass
    elif a == 'ВОСТОК':
        pass
    elif a == 'ЮГ':
        pass
    elif a == 'ЗАПАД':
        pass"""

# Ввод в одну строку списка
"""a = list(map(int, input()))
print(sum(a))"""

"""det = int(input())
i = 0
z = []
while i != det:
    a = str(input())
    z.append(a)
    i += 1
print(max(z))"""

"""a = int(input())
if a % 2 == 0:
    print('NO')
elif a % 1 == 0 and a % a == 0:
    print('YES')"""

"""a = int(input())
g = 0
i = 0
while i != a:
    f = str(input())
    i += 1
    if 'зайка' in f:
        g += 1
print(g)"""

"""a = list(map(int, input()))
if a == a[::-1]:
    print('YES')
else:
    print('NO')"""

"""a = list(map(int, input()))
for i in a:
    if i % 2 == 0:
        a.remove(i)
    else:
        pass
print(*a, sep='')"""

"""import random
print('Привет, я загадал число от 1 до 30. У тебя 6 попыток чтобы отгадать его')
number = random.randint(1, 30)
made = 0
while made != 6:
    guess = int(input('Введи число: '))
    if guess > number:
        print('Я загадал число меньше!')
    elif guess < number:
        print('Я загадал число больше!')
    elif guess == number:
        print(f'Молодец, загаданное число было: {number}!')
        break
    else:
        print(f'Ты не справился( Число было: {number}')"""

# m - полезная информация(цифры блока)
# t - случайное число от 0 до 255
# h - хэш(целое число от 0 до 255)
import random

"""a = int(input())
blockchain_right = True
for i in range(a):
    if i == 0:
        h1 = 0
    else:
        h1 = h
    b = int(input())
    h = b % 256
    b //= 256
    r = b % 256
    b //= 256
    m = b
    if ((h != 37 * (m + r + h1) % 256) or (h >= 100)) and blockchain_right:
        print(i)
        blockchain_right = False
if blockchain_right:
    print('-1')"""

"""n = int(input())  # 2
m = int(input())  # 4
for i in range(n):
    for j in range(m):  # вложенный цикл
        print('*', end='')
    print()"""

"""a = int(input())
for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(f'{j} * {i} = {i * j}')"""

"""z = []
a = int(input())
for i in range(a):
    b = int(input())
    z.append(b)
print(sum(z))"""

"""a = int(input())
f = 0
zaika = 0
while f != a:
    d = str(input())
    if d == 'ВСЁ':
        f += 1
    elif d == 'зайка':
        zaika += 1
print(zaika)"""

"""a = int(input())
b = int(input())
c = a % b
while c != 0:
    b = b % c
print(b)"""

"""a = int(input())
b = int(input())

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)"""

"""name, surname = input().split()

def hello_name():
    print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")


hello_name()"""

"""a = float(input())
def weight():
    print(f"Предмет имеет вес: {a} кг.")


weight()"""

"""def list_size():
    c = list(map(int, input().split()))
    v_min = min(c)
    v_max = max(c)
    v_sum = sum(c)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")


list_size()"""


"""def perimeter(width, height):
    print(f'Периметр прямоугольника, равен {2 * (width + height)}')


a, b = map(int, input().split())
perimeter(width=a, height=b)"""

# Решить это завтра!!!
"""def mail_correct():
    mail = str(input().upper())
    if "@" and '.' in mail:
        print('ДА')
    else:
        print('НЕТ')


mail_correct()
print()"""



"""a = {0: 'А', 1: 'Г', 2: 'И', 3: 'Л', 4: 'М', 5: 'О', 6: 'Р', 7: 'Т'}
z = 1
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                z += 1
                if a[i] == 'Г' and a[j] == 'О':
                    print(z)"""


"""def str_min(*args):
    return min(args)


def str_min3(*args):
    return min(args)


def str_min4(*args):
    return min(args)"""


"""a = input().split()
lst_c = tuple(a)
print(lst_c)"""


"""a, b = list(map(int, input().split()))
i = a
lst = []
while i != b + 1:
    lst.append(i)
    i += 1
print(*lst)"""


a = list(map(float, input().split()))
b = list(map(str, input().split()))
lst = [*a, *b]
print(*lst)
# Just check how it work







