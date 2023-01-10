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

"""a = list(map(float, input().split()))
b = list(map(str, input().split()))
lst = [*a, *b]
print(*lst)"""

# Just check how it work
# and it really work why i cant


# - - - - - - - - - - - - - - - - - - -  - - - - - - - - - -  - - - - -  - - - - -  -- - - - -
# Введение в словари

"""d = {"house": 'дом', "car": 'машина',
     "tree": 'дерево', "road": 'дорога',
     "river": 'река'}

print(d["car"])"""

"""lst = input().split()
lst1 = [lst[i].split('=') for i in range(len(lst))]
d = dict(lst1)
for key in d:
    d[key] = int(d[key])
print(*sorted(d.items()))"""

"""slovar = dict({1: 'one', 2: 'two'})
slovar.clear()
print(slovar)"""

# myDict = {myList[i]: myList[i + 1] for i in range(0, len(myList), 2)}
# print(myDict)


"""def perimeter(width, height):
    print(f'Периметр прямоугольника, равен {2 * (width + height)}')


a, b = map(int, input().split())
perimeter(width=a, height=b)"""

"""def convert_minutes_2_seconds(minutes):
    print(f"Это: {minutes * 60} секунд")


time = int(input("Введите кол-во минут: "))  # Ввод минут
convert_minutes_2_seconds(minutes=time)"""

# ---- Программа для вывода словаря через список, где каждый ключ одноименен с значением словаря-----
"""def to_dict(list):
    j = 0
    for i in a:
        slovar[i] = a[j]
        j += 1
    print(slovar)

a = input().split()
slovar = {}
to_dict(list=slovar)"""

"""dict_1 = {"a": '300', "b": '400'}
dict_2 = {"c": '500', "d": '600'}
dict_1.update(dict_2)
print(dict_1)"""

"""dict_1 = {1: 10, 2: 20, 3: 30}
for i in dict_1:
    dict_1[i] = i*i
print(dict_1)"""

"""dict_1 = dict.fromkeys(['name', 'age', 'job'], 'Missed')
print(dict_1)"""

"""info = dict(name='Alex', age='23')
print(info['name'])"""

"""name = str(input('Введите ваше имя: '))
age = int(input('Введите ваш возраст: '))
city = str(input('Введите ваш город: '))
info_1 = dict(name=name,
              age=age,
              city=city)
print(info_1)"""

"""keys = ['name', 'age']
values = ['Alex', '17']

info = dict(zip(keys, values))
print(info)"""

"""my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}

print(my_dict[2][1])
# В этом случае первый аргумент это ключ словаря,
# а второй аргумент это индекс значения списка"""

"""my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

print(min(my_dict) + max(my_dict))"""

"""users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]


z = []
for i in users:
    if i['phone'][-1] == "8":
        z.append(i["name"])
f = (sorted(z))
print(*f)"""

"""
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

z = []
for i in users:
    if not i.get('email'):
        z.append(i['name'])

f = sorted(z)
print(*f)"""

"""
number = list(map(int, input()))
d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

z = []
for i in number:
    z.append(d[i])

print(*z)"""

"""info = {
    "CS101": "CS101: 3004, Хайнс, 8:00",
    "CS102": "CS102: 4501, Альварадо, 9:00",
    "CS103": "CS103: 6755, Рич, 10:00",
    "NT110": "NT110: 1244, Берк, 11:00",
    "CM241": "CM241: 1411, Ли, 13:00"
}

a = str(input())
print(info[a])"""

"""words = {
    # Если не получится решить, то поменять местами ключи и значения
    "1": ".",
    "11": ",",
    "111": "?",
    "1111": "!",
    "11111": ":",
    "2": "A",
    "22": "B",
    "222": "C",
    "3": "D",
    "33": "E",
    "333": "F",
    "4": "G",
    "44": "H",
    "444": "I",
    "5": "J",
    "55": "K",
    "555": "L",
    "6": "M",
    "66": "N",
    "666": "O",
    "7": "P",
    "77": "Q",
    "777": "R",
    "7777": "S",
    "8": "T",
    "88": "U",
    "888": "V",
    "9": "W",
    "99": "X",
    "999": "Y",
    "9999": "Z",
    "0": " "
}

z = []
a = input().upper()
for i in a:
    for key, value in words.items():
        if i in value:
            z.append(key)
print(*z, sep='')"""


"""keys_mapping = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

z = []
a = str(input().upper())
for i in a:
    for key, value in keys_mapping.items():
        if i in key:
            z.append(value)
print(*z, sep=' ')"""



"""numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1
print(result)"""


"""result = {}
for num in range(1, 16):
    result[num] = result.get(num, num) ** 2
print(result)"""


dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict2.copy()

sert = {}
for i in dict1:
    print(dict1[i])
    for j in dict2: #f"{i} - {dict1[i] + dict2[j]}"
        if i == j:
            sert.setdefault(i, dict1[i] + dict2[j])

print(sert)
result.update(sert)
print(result)


"""sert = []
for i in dict1:
    print(dict1[i])
    for j in dict2:
        if i == j:
            sert.append(f"{i} - {dict1[i] + dict2[j]}")
print(sert)"""



