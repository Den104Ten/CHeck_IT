
"""s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana ' \
    'banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes ' \
    'melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince ' \
    'grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince ' \
    'lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana ' \
    'banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate ' \
    'barley plum banana quince barley lime grapefruit pomegranate barley'

number = [x for x in s.split()]
result = {}
for i in number:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

z = []
maxt = max(result.values())
for j in result:
    if result[j] == maxt:
        z.append(j)
print(min(z))

# Нужно вывести слово которое повторяется чаще всего, количество его повторений я уже вывел, но не знаю как вывести само слово
# Сохранить наибольшее значение в переменной и с помощью цикла по словарю сравнивать его с значениями других ключей"""

"""pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in pets:
    result.setdefault((i[1], i[2], i[3]), []).append(i[0])
print(result)"""

# f"{i[1]}, {i[2]}, {i[3]}"


"""res = [a.strip('.,!?:;-') for a in input().lower().split()]

result = {}
for i in res:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

z = []
mint = min(result.values())
for j in result:
    if result[j] == mint:
        z.append(j)
print(min(z))"""

"""
index = int(input())
i = 0
info = {}
while i != index:
    key, value = input().split(': ')
    val = info.setdefault(key.lower(), value)
    i += 1
index_2 = int(input())
j = 0
z = []
while j != index_2:
    key_val = str(input().lower())
    j += 1
    if key_val in info:
        # print(info[key_val])
        z.append(info[key_val])
    else:
        z.append("Не найдено")
print(*z, sep='\n')"""

"""
word_1 = str(input())
word_2 = str(input())
result = {}
result_2 = {}
for i in word_1:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1
for j in word_2:
    if j not in result_2:
        result_2[j] = 1
    else:
        result_2[j] += 1
if result == result_2:
    print('Yes')
else:
    print('NO')"""

"""a = str(input().strip(".,!?:;-").replace(' ', '').lower())
b = str(input().strip(".,!?:;-").replace(' ', '').lower())
z = ['.', ',', '!', '?', ':', ';', '-']
result_1 = {}
result_2 = {}
for i in a:
    if i not in result_1 and i not in z:
        result_1[i] = 1
    elif i not in z:
        result_1[i] += 1
    else:
        pass

for j in b:
    if j not in result_2 and j not in z:
        result_2[j] = 1
    elif j not in z:
        result_2[j] += 1
    else:
        pass

if result_1 == result_2:
    print("YES")
else:
    print("NO")"""

"""index = int(input())
i = 0
info = {}
while i != index:
    key, value = input().lower().split()

    val = info.setdefault(key, value)
    i += 1
word = str(input().lower())
if word in info:
    print(info[word].title())
elif word not in info:
    for k, v in info.items():
        if v == word:
            print(k.title())"""

"""index = int(input())
i = 0
result = {}
while i != index:
    key_val = input().split()
    result.setdefault(key_val[0], key_val[1:])
    i += 1

city_num = int(input())
j = 0
z = []
while j != city_num:
    city = str(input())
    for k in result:
        if city in result[k]:
            z.append(k)
    j += 1
print(*z, sep='\n')"""

"""index = int(input())
i = 0
info = {}
while i != index:
    key, val = input().split()
    info.setdefault(key, val)
    i += 1
print(info)
index_2 = int(input())
j = 0
z = []
while j != index_2:
    name = str(input())
    for i in info:
        if name in info[i]:
            z.append(i)
        else:
            z.append('абонент не найден')
    j += 1
print(*z, sep='\n')"""

"""squares = {i: i**2 for i in range(6)}
print(squares)"""

"""numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]

result = {i: numbers[i]**2 for i in range(len(numbers))}
print(result)"""

"""colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

result = {i: colors[i] for i in colors if colors[i] != None}
print(result)"""

"""favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}

result = {i: favorite_numbers[i] for i in favorite_numbers if 10 <= favorite_numbers[i] <= 99 }
print(result)"""

"""months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {months[i]: i for i in months}
print(result)"""

"""s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

info = [x for x in s.split()]

result = {}
for i in info:
    top = i.split(':')
    result.setdefault(int(top[0]), top[1])
print(result)"""

"""numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {}
for i in numbers:
    z = []
    for j in range(1, i + 1):
        if i % j == 0:
            z.append(j)
        else:
            pass
    result.setdefault(i, z)
print(result)"""

"""words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {}
for i in words:
    z = []
    for j in i:
        z.append(ord(j))
    result.setdefault(i, z)
print(result)"""

"""letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}

remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]

result = {}
for i in letters:
    if i in remove_keys:
        pass
    else:
        result.setdefault(i, letters[i])
print(result)"""

"""students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

result = {}
for i in students:
    if students[i][0] > 167 and students[i][1] < 75:
        result.setdefault(i, students[i])
print(result)"""

"""tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

result = {}
for i in tuples:
    result.setdefault(i[0], i[1:])
print(result)"""

"""student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]


result = []
for key, key_1, value in zip(student_ids, student_names, student_grades):
    result.append({key: {key_1: value}})
print(result)"""

"""import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)
print(num1)
print(num2)"""

"""import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))"""

"""import random as r
print(r.randint(0, 10))"""

"""from random import *
n = int(input())
i = 0
while i != n:
    rand = randint(1, 2)
    if rand == 1:
        print('Орел')
    else:
        print('Решка')
    i += 1"""

"""from random import *
n = int(input())
i = 0
while i != n:
    rand = randint(1, 6)
    print(rand)
    i += 1"""

"""from random import *
n = int(input())
i = 0
z = []
while i != n:
    rand = randint(1, 2)
    if rand == 1:
        low_d = randint(65, 90)
        z.append(chr(low_d))
    else:
        up_d = randint(97, 122)
        z.append(chr(up_d))
    i += 1
print(*z, sep='')"""

"""from random import *
i = 0
z = []
s = set
while i != 7:
    rand = randint(1, 49)
    if rand in z:
        pass
    else:
        z.append(rand)
        i += 1
a = sorted(z)
print(*a)"""

"""from random import *
def generate_index():
    up_d = randint(97, 122)
    up_d2 = randint(97, 122)
    up_d3 = randint(97, 122)
    up_d4 = randint(97, 122)
    print(f'{chr(up_d).upper()}{chr(up_d2).upper()}{randint(0, 99)}_{randint(0, 99)}{chr(up_d3).upper()}{chr(up_d4).upper()}')

generate_index()"""

"""from random import *
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
for i in matrix:
    shuffle(i)"""

"""from random import *
for i in range(100):
    j = 0
    z = []
    while j != 7:
        rand = randint(1, 9)
        j += 1
        z.append(rand)
    print(*z, sep='')"""

"""from random import *
a = str(input())
z = []
for i in a:
    z.append(i)
shuffle(z)
print(*z, sep='')"""

"""from random import *
for j in range(5):
    z = []
    i = 0
    while i != 5:
        rand = randrange(1, 75)
        if j == 2:
            if i == 2:
                z.append(0)
            else:
                z.append(rand)
        else:
            z.append(rand)
        i += 1
    j += 1
    print(*z)"""

"""from random import *
z = []
for i in range(1, 76):
    z.append(i)
lst = sample(z, 25)
lst.insert(12, 0)
print(*lst[:5])
print(*lst[5:10])
print(*lst[10:15])
print(*lst[15:20])
print(*lst[20:25])"""

"""from random import *
n = int(input())  # length
m = int(input())  # count
for i in range(n):
    j = 0
    z = []
    while j != m:  # Счетчик символов
        rand = randint(1, 3)  # Если low_d равен l, I, 1, 0, o, O то нужно не добавлять этот символ и пропустить счетчик
        if rand == 1:
            up_d = randint(65, 90)
            res_to_str = chr(up_d)  # ИСПРАВИТЬ НА UP ЕСЛИ НЕ ПРАВИЛЬНО
            if res_to_str == 'I' or res_to_str == 'O':  # Только большие буквы, без цифр # or O
                j -= 1
                pass
            else:
                z.append(res_to_str)
        elif rand == 2:
            int_d = randint(2, 9)
            z.append(int_d)
        else:
            low_d = randint(97, 122)  # Поменять чтобы исключения не выводились
            res_to_str_2 = chr(low_d)
            if res_to_str_2 == 'l' or res_to_str_2 == 'o':
                j -= 1
                pass
            else:
                z.append(chr(low_d))
        j += 1
    print(*z, sep='')"""

"""def sum(x, y):
    return x + y


print(sum(1, 10))"""

"""def sum_3(a, b, c=2): # c - именнованный параметр, он необязателен
    return a + b + c


print(sum_3(a=2, b=4, c=4))"""

"""def hello_name():
    name = str(input())
    second_name = str(input())
    return (f'Уважаемый, {name} {second_name}! Вы верно выролнили это задание!')


print(hello_name())"""

"""def print_weight(weight):
    return (f'Предмет имеет вес: {x} кг.')

x = float(input())
print(print_weight(weight=x))"""




"""def min_max_lst():
    lst = list(map(int, input().split()))
    return (f'Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}')


print(min_max_lst())"""


"""def p_pryamougol(width, height):
    return (f'Периметр прямоугольника, равен {width * height}')


a = int(input())
b = int(input())
print(p_pryamougol(width=a, height=b))"""


"""def check_email(email):
    z = []
    for i in range(65, 91):
        z.append(chr(i))
    for j in range(97, 123):
        z.append(chr(j))
    for k in range(0, 10):
        z.append(k)
    for l in '@._':
        z.append(l)
    for m in email:
        if m in z:
            res = 'ДА'
        elif m not in z:
            res = 'НЕТ'
    return res

e_email = input()
print(check_email(email=e_email))"""


"""def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(char2='$', length=3))"""


"""def matrix(n=1, m=None, value=0):
    if n == 1 and m == None:
        m = 1
    elif n != 1 and m == None:
        m = n
    return [[value] * m for _ in range(n)]

print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9"""



"""def my_func(*args):
    print(type(args))
    print(args)


my_func()
my_func(1, 2, 3)
my_func('a', 'b')"""


# Выводит сумму квадратов всех введенных чисел
"""def sq_sum(*args):
    z = []
    for i in args:
        sqr = i**2
        z.append(sqr)
    return sum(z)


print(sq_sum(1, 2, 3))"""


"""def mean(*args):
    z = []
    for i in args:
        if len(args) <= 1:
            return float(i)
        elif len(args) >= 2:
            if type(i) == int or type(i) == float:
                z.append(i)
                continue
            else:
                continue
    if args == ():
        return float(0)
    elif z == []:
        return float(0)
    else:
        return float(sum(z) / len(z))


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))"""


def greet(name, *args):
    if name and not args:
        return f'Hello, {name}!'
    else:
        return f'Hello, {name} and {" and ".join(args)}!'



print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))





