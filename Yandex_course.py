

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

"""
# Программа соединяющаяя два словаря в один
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict2.copy()

sert = {}
for i in dict1:
    for j in dict2:
        if i == j:
            sert.setdefault(i, dict1[i] + dict2[j])
        else:
            sert.setdefault(i, dict1[i])

result.update(sert)
print(result)"""

"""numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1
print(result)"""

"""
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for i in text:
    if i not in result:
        result[i] = 1  # С помощью этой программы можно вычислить сколько раз было произведено вхождение всех символов
    else:
        result[i] += 1
print(result)"""

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


index = int(input())
i = 0
result = {}
while i != index:
    key_val = input().split()
    result.setdefault(key_val[0], key_val[1:])
    i += 1
print(result)
#for k in result:
#    print(k)  # Выводит ключи словаря

city_num = int(input())
j = 0
while j != city_num:
    city = str(input())
    for k in result:
        if city in k:
            print(k)
        else:
            print('NO')
    j += 1


# Сделать переменную и ввести в нее и ключ и значения после разделить их срезом строк и добавить в словарь
