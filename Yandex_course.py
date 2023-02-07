


"""numbers = sorted(numbers, key=mid_sort)


print(numbers)"""

"""athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

index = int(input())
def name_sort(x):
    return x[index - 1]

a = (sorted(athletes, key=name_sort))
for i in a:
    print(*i)"""

"""from math import sin

integer = int(input())
definition = str(input())

dict_def = {'квадрат': integer**2,
            'куб': integer**3,
            'корень': integer**0.5,
            'модуль': abs(integer),
            'синус': sin(integer)
            }

print(dict_def[definition])"""

# a = input().split()

# 12 14 79 7 4 123 45 90 111

"""a = (sorted(list(map(int, input().split())), key=lambda x: sum(list(map(int, list(str(x)))))))
print(*a)"""

"""z1 = []
for i in a:
    z = []
    for j in i:
        z.append(int(j))
    z1.append(sum(z))

print(a)
print(z1)
print()
comb_dict = {}
l = 0
for k in z1:
    comb_dict[k] = a[l]
    l += 1
print(comb_dict)"""

"""def sqr_f(x):
    return x**2     # тело функции, которая преобразует аргумент x


old_list = [1, 2, 4, 9, 10, 25]
new_list = []
for item in old_list:
    new_item = sqr_f(item)
    new_list.append(new_item)

print(old_list)
print(new_list)"""

"""def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result
def predicate(word):
    return word == word[::-1]


words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
filtered = filter(predicate, words)
print(len(filtered))"""

"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

z = []
for i in numbers:
    z.append(round(i, 2))
print(*z, sep='\n')"""

"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

def rnd_item(x):
    return round(x, 2)

numbers = map(rnd_item, numbers)
print(*numbers, sep='\n')"""



"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
           1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
           1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
           898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336,
           1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

def num_3(num):
    return 99 < num < 1000 and num % 5 == 2

def cube(num):
    return num**3

print(*map(cube, filter(num_3, numbers)), sep='\n')"""


"""def reduce(operation, items, initial_value):
    z = []
    for item in items:
        z.append(operation(item))
    return sum(z)


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
           11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
           72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
           7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

def sqr(num):
    return num**2

print(reduce(sqr, numbers, 0))"""


"""def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
           219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
           152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
           187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
           211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
           79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
           10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

def big_or2(num):
    return num**2 if len(str(abs(num))) == 2 and num % 7 == 0 else False

def nums_fil(num):
    return filter(big_or2, numbers)

def num_to_sqr(num):
    return map(big_or2, numbers)


print(sum(num_to_sqr(numbers)))"""




"""def func_apply(func, items):
    z = []
    for i in items:
        z.append(func(i))
    return z


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))"""


"""def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = list(map(increase, numbers))
print(*new_numbers)"""



"""def func(elem):
    return elem >= 0


numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список

print(positive_numbers)"""

"""from functools import reduce

numbers = range(10)
obj = map(lambda x: x + 1, numbers)
obj = filter(lambda x: x % 2 == 1, obj)
result = reduce(lambda x, y: x + y, obj, 0)

print(result)

"""


"""from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: name if name == name[::-1] and len(name) > 4 else None, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)"""


from functools import reduce

"""data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]



from functools import reduce
def check10mil(x):
    z = []
    for i in x:
       if i[1] > 10000000:
           z.append(i[0])
    print(*z, sep=', ')


print("Cities: "), check10mil(data)"""

# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False


"""func = lambda x: True if x[0].upper() == 'a'.upper() and x[-1].upper() == 'a'.upper() else False
print(func("abcd"))
print(func("abca"))"""


"""is_non_negative_num = lambda x: True if x.replace('.', '').isdigit() and x.count('.') < 2 else False
print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.34'))"""


"""words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

check_6 = list(filter(lambda x: x if len(x) == 6 else False, words))
a = sorted(check_6)
print(*a, sep=' ')"""


"""numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
           93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
           53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88,
           94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

a = list(filter(lambda x: False if x > 47 and x % 2 != 0 else x, numbers))
b = list(map(lambda q: q // 2 if q % 2 == 0 else q, a))
print(*b, sep=' ')"""


"""data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

a = sorted(data, key=lambda x: x[1][-1], reverse=True)
for i in a:
    print(f"{i[1]}: {i[0]}")"""


"""data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']


data.sort()
a = (sorted(data, key=len))
print(*a, sep=' ')"""


"""mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

a = list(filter(lambda x: x if type(x) == int else False, mixed_list))
print(max(a))"""


"""mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

a = list(filter(lambda x: x if type(x) == int else False, mixed_list))
a1 = sorted(a)
z = []
for i in mixed_list:
    if type(i) == str:
        z.append(i)
z1 = sorted(z)
b = list(filter(lambda x: a1.append(x) if type(x) == str else False, z1))
print(*a1, sep=' ')"""


"""a = list(map(int, input().split()))
print(255 - a[0], 255 - a[1], 255 - a[2])"""


"""def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: True if x in command else False, ignore))

print(ignore_command('get ip'))
print(ignore_command('w'))"""


"""countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

a = list(zip(countries, capitals, population))
for i in a:
    print(f"{i[1]} is the capital of {i[0]}, population equal {i[2]} people.")
"""



"""# 4 Задача - решена
year = int(input('Введите год: '))
month = int(input('Введите месяц: '))
day = int(input('Введите день: '))
print(f'0{day}:0{month}:{year}')


# 5 Задача - решена
year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0:
    print('YES')
elif year % 400 == 0:
    print('YES')
else:
    print('NO')


# 8 Задача - решена
mil_year = int(input('Введите количество миллионов лет: '))
if mil_year in range(2500, 4601):
    print(f'{mil_year} millions years ago was Archean era.')
elif mil_year in range(540, 2500):
    print(f'{mil_year} millions years ago was Proterozoic era.')
elif mil_year in range(248, 540):
    print(f'{mil_year} millions years ago was Paleozoic era.')
else:
    print('No era like this in the task!')


# 10 Задача - решена
i = 0
while i != 1:
    words = str(input('Введите слово: '))
    if len(words) < 4:
        continue
    else:
        break"""


"""ip = str(input())
ip_list = ip.split('.')
print(ip_list)
check = list(map(lambda x: True if x.isdigit() and 0 <= int(x) <= 255 else False, ip_list))
print(all(check))"""


"""a = str(input())
b = str(input())
a1 = int(a)
b1 = int(b)
z = []
for i in range(a1, b1 + 1):
    if '0' not in str(i):
        z.append(str(i))
x = []
for j in z:
    if len(str(j)) == 1 and int(j) % int(j) == 0:
        x.append(j)
    elif int(j) % int(j[0]) == 0 and int(j) % int(j[1]) == 0:
        x.append(j)
    elif len(str(j)) == 3 and int(j) % int(j[0]) == 0 and int(j) % int(j[1]) == 0 and int(j) % int(j[2]) == 0:
        x.append(j)
print(*x)"""


"""def any_isdigit(iterable):
    for element in iterable:
        if element.isdigit():
            return True
    return False

def any_lower(iterable):
    for element in iterable:
        if element == element.lower() and not element.isdigit():
            return True
    return False

def any_upper(iterable):
    for element in iterable:
        if element == element.upper() and not element.isdigit():
            return True
    return False

password = str(input())
if len(password) >= 7 and any_isdigit(password) and any_upper(password) and any_lower(password):
    print('YES')
else:
    print('NO')"""


"""def any_5(iterable):
    for element in iterable:
        if element == '5':
            return True
    return False


num_classes = int(input())
k = 0
der = []
while k != num_classes:
    num_students = int(input())
    names = []
    grades = []
    z = []
    for i in range(num_students):
        name = list(map(str, input().split()))
        z.append(name[1])
    k += 1
    if any_5(z):
        der.append(True)
    else:
        der.append(False)

print('YES' if all(der) else 'NO')"""


"""king_stolb = int(input())
king_stroka = int(input())
king_stolb_move = int(input())
king_stroka_move = int(input())

if 0 < king_stolb_move <= 8 and king_stolb_move - king_stolb == 1 or king_stolb_move + 1 == king_stolb or king_stolb_move == king_stolb:
    if 0 < king_stroka_move <= 8 and king_stroka_move - king_stroka == 1 or king_stroka_move + 1 == king_stroka or king_stroka_move == king_stroka:
        print('YES')
    else:
        print('NO')
else:
    print('NO')"""










