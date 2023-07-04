"""numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
           11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
           72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
           7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

def sqr(num):
    return num**2

print(reduce(sqr, numbers, 0))"""
import datetime

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

# from functools import reduce

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

'''a = list(map(int, input().split()))
print(255 - a[0], 255 - a[1], 255 - a[2])
'''

"""file_name = str(input())

im_file = open(file_name, 'r')
content = [x.strip() for x in im_file.readlines()]
print(*content)
im_file.close()"""

"""file_name = str(input())
file = open(file_name, 'r')
info = file.readlines()
print(info[-2])
file.close()"""

"""import random
file = open('lines.txt', 'r', encoding='utf-8')
content = file.readlines()
print(random.choice(content))"""

"""file = open('numbers.txt', 'r')
ready = file.readlines()
z = []
for i in ready:
    z.append(int(i.strip()))
print(sum(z))"""

"""file = open('nums.txt', 'r')
summary = file.readlines()
z = []
c = []
for i in summary:
    z.append(i.replace(' ', '').strip())

for j in z:
    if j != '':
        c.append(int(j))
    else:
        pass
print(sum(c))
file.close()"""

'''file = open('prices.txt', 'r', encoding='utf-8')
stroki = file.readlines()
c = []
for i in stroki:
    z = (i.strip().split())
    for j in z:
        if j.isdigit():
            c.append(int(j))
kolvo = 0
cost = 1
x = 0
get = []
while x != len(c):
    get.append(c[kolvo] * c[cost])
    kolvo += 2
    cost += 2
    x += 2
print(sum(get))'''

# with open('input.txt', encoding='utf-8') as file:
"""    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')"""

# with open('text.txt', 'r') as file:
""""    for i in file:
        z = (i.split())
    z.reverse()
    c = []
    for j in z:
        c.append(j[::-1])
    print(*c)"""

# with open('data.txt', 'r') as file:
"""z = []
    for i in file:
        z.append(i.strip())
    z.reverse()
    print(*z, sep='\n')"""

# with open('lines(1).txt', 'r') as file:
"""    z = []
    for i in file:
        z.append(len(i))
    max_chislo = max(z)
    c = []
    file.seek(0)
    for j in file:
        if len(j) == max_chislo:
            c.append(j.strip())
        else:
            pass
    print(*c, sep='\n')"""

# with open('numbers.txt', 'r') as file:
"""z = []
    for i in file:
        z.append(i.strip().split())
    for j in z:
        a = list(map(int, j))
        print(sum(a))"""

# with open('file.txt', 'r') as file:
"""    letters = 0
    words_1 = 0
    lines = 0
    for i in file:
        lines += 1
        for j in i:
            if j != ' ' and j != '.' and j != '\n' and j != ',' and j != '!' and j != '"' and j.isdigit() == False:
                letters += 1
            elif j == ' ' or j == '.' and j != '\n':  # перенос строки это не слово
                words_1 += 1
    print('Input file contains:')
    print(f"{letters} letters")
    print(f"{words_1} words")
    print(f"{lines} lines")"""

"""from random import *
with open('first_names.txt', 'r') as names_file:

    # Количество имен
    z = []
    for i in names_file:
        z.append(i)
    num = len(z) - 1

    # Рандомное имя
    lst_names = []
    i = 0
    while i != 3:
        rand = (randint(0, num))
        lst_names.append(z[rand].strip())
        i += 1

with open('last_names.txt', 'r') as lastnames_file:
    s = []
    for i in lastnames_file:
        s.append(i)
    num_s = len(s) - 1

    lst_lastnames = []
    i = 0
    while i != 3:
        rand_1 = (randint(0, num_s))
        lst_lastnames.append(s[rand_1].strip())
        i += 1

d = dict(zip(lst_names, lst_lastnames))
for key in d:
    print(key, d[key])"""

# with open('population.txt', 'r') as file:
"""    z = []
    for i in file:
        z.append(i.strip().split())
    countries = []
    for j in z:
        if j[1].isdigit() and int(j[1]) > 500000:
            for k in j:
                if k[0] == 'G':
                    countries.append(k)
    for h in countries:
        print(h)"""

"""def read_csv():
    with open('data.csv', 'r') as file:
        z = (file.readline().strip().split(','))
        a = 1
        d = []
        for i in file:
            d.append((dict(zip(z, i.strip().split(',')))))
        return d

read_csv()"""

"""a = str(input())

with open('output.txt', 'w') as file:
    file.write(a)

    print(file)
"""

"""from random import *
with open('random.txt', 'w') as file:
    i = 0
    while i != 25:
        rand = randint(111, 777)
        rand_to_str = str(rand)

        if i == 24:
            file.write(rand_to_str)
        else:
            file.write(rand_to_str + '\n')
        i += 1

        print(file)"""

"""dscds
with open('input.txt', 'r') as file_input:
    with open('output.txt', 'w') as file_output:
        k = 0
        for i in file_input:
            k += 1
            file_output.write(f"{k}) {i}")"""

"""as
with open('class_scores.txt', 'r', encoding='utf-8') as file_scores:
    with open('new_scores.txt', 'w', encoding='utf-8') as file_new_scores:
        z = []
        for i in file_scores:
            z.append(i.strip().split())
        for j in z:
            if int(j[1]) == 95 or int(j[1]) == 96 or int(j[1]) == 97 or int(j[1]) == 98 or int(j[1]) == 99 or int(j[1]) == 100:
                file_new_scores.write(j[0] + ' ')
                file_new_scores.write('100' + '\n')
            else:
                a = str(int(j[1]) + 5)
                file_new_scores.write(j[0] + ' ')
                file_new_scores.write(a + '\n')"""

"""as
with open('logfile.txt', 'r', encoding='utf-8') as file_input:
    with open('output.txt', 'w', encoding='utf-8') as file_output:
        z = []
        for i in file_input:
            z.append(i.strip().split())
        print(z)
        for j in z:
            t1 = j[2]
            for k in t1:
                print(k)"""

"""def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


descending_order(8932)"""

"""def is_isogram(string):
    if string == '':
        return True
    z = []
    for i in string:
        z.append(i.lower())
    check = None
    for j in z:
        if z.count(j) > 1:
            check = False
            break
        else:
            check = True
    print(check)

is_isogram('')"""

"""def spin_words(sentence):
    z = (sentence.split())
    x = []
    for i in z:
        if len(i) >= 5:
            x.append(i[::-1])
        else:
            x.append(i)
    return " ".join(x)



spin_words('Hey fellow warriors')"""

"""def alphabet_position(text):
    z = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
         'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
         'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    x = []
    for i in text.lower():
        if i.isalpha():
            x.append(z[i])
    return ' '.join(x)


print(alphabet_position("The sunset sets at twelve o' clock."))"""

"""def find_short(s):
    z = (s.split())
    l = min(z, key=len)
    l = len(l)
    return l


print(find_short('i want to travel the world writing code one day"'))"""

"""def solution(text, ending):
    return True if text[-2] + text[-1] == ending or text[-1] == ending else False



print(solution('sensei', 'i'))"""

"""def square_digits(num):
    a = [x for x in str(num)]
    a1 = list(map(int, a))
    b = [z**2 for z in a1]
    b1 = list(map(str, b))
    a = ''.join(b1)
    return int(a)


print(square_digits(9119))"""

"""def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('sdcsdcsd'))"""

"""def accum(s):
    f = 0
    i = 1
    z = []
    while i != len(s):
        z.append(s[f] * i)
        f += 1
        i += 1
    x = []
    for k in z:
        print(k)
        x.append(k[0].upper() + k[1:].lower())
    return '-'.join(x)


print(accum('RqaEzty'))"""

"""def hide_card(card_number):
    z = ['*' * 12]
    z1 = []
    for i in card_number:
        if i != ' ':
            z1.append(i)
        else:
            pass
    a = ''.join(z1)
    z.append(a[-4:])
    return ''.join(z)"""

"""def same_parity(numbers):
    numbers = list(filter(lambda x: numbers[0] % 2 == x % 2, numbers))
    return numbers


print(same_parity([-7, 0, 67, -9, 70, -29, 90]))"""

"""a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
a.sort(key=lambda x: x % 10)
print(a)"""

"""def linear(k, b):
    return lambda x: x * k + b

graf_1 = linear(2, 5)
print(graf_1(3))
"""

"""from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
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

z = []
a = list(filter(lambda x: z.append(x[0]) if x[1] > 10_000_000 and x[2] == 'primary' else False, data))
print("Cities"", ', '.join(sorted(z)))"""

"""def is_num(x):
    try:
        float(x) or int(x)
        return True
    except ValueError:
        return False"""

"""is_num = lambda x: True if x[0] == '-' and x[1:].replace('.', '', 1).isdigit() or x[0].isdigit() and x[1:].replace('.', '', 1).isdigit() else False
is_num = lambda x: True if x[0] == '-' and x[1:].replace('.', '', 1) or x[0].isdigit() and x[1:].replace('.', '', 1).isdigit() else False

print(is_num('0'))"""

"""is_valid = lambda x: True if len(x) in range(4, 7) and x.isdigit() and x.count(' ') == 0 else False
print(is_valid('49 83'))
"""

"""def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    z = []
    x = []
    for j in kwargs:
        z.append(j)
        x.append(kwargs[j])
    a = dict(zip(z, x))
    for i in sorted(a):
        print(i, a[i], type(a[i]))

print_given(1, [1, 2, 3], 'three', two=2)"""

"""convert = lambda string: string.lower() if len(string.lower()) > len(string.upper()) or len(string.lower()) == len(string.upper()) else string.upper()
print(convert('pyTHON'))"""

"""def convert(string):
    z_lower = []
    z_upper = []
    for i in string:
        if i.islower():
            z_lower.append(i)
        elif i.isupper():
            z_upper.append(i)
    if len(z_lower) > len(z_upper):
        return string.lower()
    elif len(z_upper) > len(z_lower):
        return string.upper()
    else:
        return string.lower()

print(convert('ABCdef'))"""

"""def likes(names):
    if names == []:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'


print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))"""

"""def index_of_nearest(numbers, number):
    if numbers == []:
        return -1
    else:
        a = min(numbers, key=lambda x: abs(x-number))
        k = 0
        for i in numbers:
            if i == a:
                return k
            else:
                k += 1


print(index_of_nearest([7, 13, 3, 5, 18], 4))"""

"""def spell(*args):
    if args:
        from_keys = {}
        z = []
        x = []
        for i in args:
            from_keys = {f'{i[0].lower()}': len(i)}
            for j in from_keys:
                z.append(from_keys[j])
                x.append(from_keys)
        rop = []
        for k in x:
            for l in k:
                #print(k[l])
                if k[l] == max(z):
                    rop.append(k)
        return rop[0]
    else:
        return []


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))"""

"""def spell(*args):
    if args:
        letter_z = []
        word_z = []
        for i in args:
            letter_z.append(i[0].lower())
            word_z.append(len(i))
        result = dict(zip(letter_z, word_z))

        for j in args:
            if j[0].lower() in result:
                if result[j[0].lower()] < len(j):
                    result[j[0].lower()] = len(j)
        return result
    else:
        return {}



print(spell())"""

"""def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])


print(choose_plural(112, ('цент', 'цента', 'центов')))"""

"""d1 = int(input()) #10  # Расстояние от дома до 1-го магазина
d2 = int(input()) #10  # Расстояние от дома до 2-го магазина
d3 = int(input()) #45  # Расстояние длины дорожки соединяющей магазины

steps = 0
if d1 > d2 and d1 > d3:
    steps += d2
    if d1 > d3:
        steps += d3
        if d1 >= (d2 + d3):
            steps += (d2 + d3)
        else:
            steps += d1

elif d3 > d1 and d3 > d2:
    steps += d1
    if d3 > d2:
        steps += d2
        if d3 >= (d1 + d2):
            steps += (d1 + d2)
        else:
            steps += d3

elif d2 > d1 and d2 > d3:
    steps += d1
    if d2 > d3:
        steps += d3
        if d2 >= (d1 + d3):
            steps += (d1 + d3)
        else:
            steps += d2

elif d1 == d2 == d3:
    steps += (d1 + d2 + d3)

elif d1 == d2 and d1 > d3:
    steps += d1
    if d1 > d3:
        steps += (d3 + d2)

print(steps)"""

"""ru_letters = 'АаВСсЕеНКМОоРрТХху'
z_ru = []
for i in ru_letters:
    z_ru.append(i)

en_letters = 'AaBCcEeHKMOoPpTXxy'
z_en = []
for j in en_letters:
    z_en.append(j)


a1, b2, c3 = [str(input()) for _ in range(3)]

if a1 in ru_letters and b2 in ru_letters and c3 in ru_letters:
    print('ru')
elif a1 in en_letters and b2 in en_letters and c3 in en_letters:
    print('en')
else:
    print('mix')"""

"""a = input().split()
rot = []
for l in a:
    rot.append(str(l))

v = list(filter(lambda x: x if rot.count(x) >= 2 else False, rot))

z = []
for i in v:
    z.append(i if i not in z else False)
g = []
for j in z:
    if j:
        g.append(int(j))
k = sorted(g)
print(*k)"""

"""import math

def round_up(number, digits):
    number = str(number)
    rounded_number = number[:-digits] + str(int(number[-digits]) + 1)
    return float(rounded_number)

def round_down(number, digits):
    number = str(number)
    rounded_number = number[:-digits] + str(int(number[-digits]) - 1)
    return float(rounded_number)

s = input()  #ОКРУГЛ(1,5136;2) ОКРУГЛВВЕРХ(1,5136;2) ОКРУГЛВНИЗ(1,5136;2)
z = []
x = []
for i in s:
    if i.isalpha():
        z.append(i)
    elif i.isdigit() or i == ',':
        x.append(i)
if ''.join(z) == 'ОКРУГЛ':
    spisok = ''.join(x)
    for j in spisok:
        if j == ',':
            got = spisok.replace(',', '.')
            chislo = (got[:-1])

            f = float(chislo)
            h = int(spisok[-1])
            print(round(f, h))

if ''.join(z) == 'ОКРУГЛВВЕРХ':
    spisok_2 = ''.join(x)
    for j in spisok_2:
        if j == ',':
            got = spisok_2.replace(',', '.')
            chislo = (got[:-1])
            f = float(chislo)
            h = int(spisok_2[-1])
            print(round_up(f, h + 1))

if ''.join(z) == 'ОКРУГЛВНИЗ':
    spisok_3 = ''.join(x)
    for j in spisok_3:
        if j == ',':
            got = spisok_3.replace(',', '.')
            chislo = (got[:-1])
            f = float(chislo)
            h = int(spisok_3[-1])
            print(round_down(f, h + 1))"""

"""a with open('Super.csv', 'r') as infile:
    big_string = infile.readline()
    keys = []
    for i in big_string.split(';'):
        keys.append(i.strip('п»ї').replace('\n', ''))
    # keys словарь для ключей!!!

    len_lines = len(infile.readlines())

    infile.seek(3)
    values = []
    for j in range(len_lines):
        if j == 1:
            infile.seek(2)
        else:
            print(dict(zip(keys, infile.readline().split(';'))))"""

"""n = int(input())
z = [str(i) for i in range(1, n + 1)]
print(z)
print()

keys = []
values = []

for j in z:
    for k in z[9:]:
        if int(j) == int(k[0]) + int(k[1]):
            print(j, k)"""

"""from itertools import product

a = [1, 2020, 70]
b = [2, 4, 7, 2000]
c = [3, 70, 7]

for i, j, k in product(a, b, c):
    print(i, j, k)"""

"""peoples = int(input())
z = []
for _ in range(peoples):
    z.append(input().split(','))
print(z)

x = []
for l in z:
    for h in l:
        x.append(h)
print(x)

result = []
for j in x:
    if j in z:
        result.append(j)

print(result)
print(z)"""

"""word = str(input())
book_sum = int(input())

check_words = []  # список из введенных слов
for _ in range(book_sum):
    check_words.append(input())


glasn = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
soglasn = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь']

# функция для преобразования слов в код из 1 и 2
def word_to_num(text):
    glasn = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    soglasn = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь']
    word_num = []
    for i in text:
        if i in soglasn:
            word_num.append(1)
        else:
            word_num.append(2)
    return word_num


if word[-1] in soglasn:
    word = word[:-1]
else:
    pass

first_word_num = word_to_num(word)  # преобразование начального слова в цифры


result = []
for j in check_words:
    if word_to_num(j[:len(first_word_num)]) == first_word_num:
        result.append(j)
    else:
        pass

for k in result:
    print(k)"""

"""mail_sum = int(input())

mail_lst = []
for _ in range(mail_sum):
    mail_lst.append(input().replace('@beegeek.bzz', ''))  # создаю список из имен без обозначения почты

new_mail_lst = []
new_mail_sum = int(input())
for _ in range(new_mail_sum):
    new_mail_lst.append(input())


print(mail_lst)
print(new_mail_lst)



for i in new_mail_lst:
    if i in mail_lst:  # добавляет новый ящик, если один такой уже есть с окончанием 1
        mail_lst.append(i + '1')
    elif i and i[-1].isdigit() in mail_lst:
        mail_lst.append(i + f'{int(i[-1]) + 1}')
    else:
        mail_lst.append(i)

print(mail_lst)"""

"""import math

def f(x):
    return math.log(x) + 0.5 * x**3

a = 0.1
b = 0.5

epsilon = 0.001

while abs(b - a) > epsilon:
    c = (a + b) / 2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

x = (a + b) / 2
print(f'Корень уравнения: {x:.3f}')"""

"""numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}

print(sum([i**2 for i in numbers]))"""

"""fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

fruits_sorted = sorted(fruits, reverse=True)
for i in fruits_sorted:
    print(i)"""

"""text = str(input())
text_set = set(text)
if len(text) == len(text_set):
    print('YES')
else:
    print('NO')"""

"""text = input().split()
if set(text[0]) == set(text[1]) == set(text[2]):
    print('YES')
else:
    print('NO')"""

"""n = int(input())
i = 0
z = []
while i != n:
    z.append(set(input().lower()))
    i += 1
for j in z:
    print(len(j))"""

"""n = int(input())
i = 0
z = set()
while i != n:
    z.add(input().lower())
    i += 1

lst = []
for j in z:
    lst.append(j)

result = (''.join(lst))
print(len(set(result)))"""

"""text = [input().lower().strip('.,;:-?!').split()]

z = set()
lst = []

for i in text:
    for j in i:
        z.add(j.strip('.,;:-?!'))

print(len(z))"""

"""text = [input().split()]


z = []

for i in text:
    for j in i:
        if int(j) not in z:
            print('NO')
            z.append(int(j))
        else:
            print('YES')
            z.append(int(j))"""

"""from functools import reduce

print(volume := reduce(lambda x, y: x * y, map(int, input().split())))"""

"""x, y, z = input().split()

print(int(x) * int(y) * int(z))"""

"""num_1 = set(input())
num_2 = set(input())

result = 0

for i in num_1:
    if set(i).issubset(num_2):
        result = 'YES'
        break
    else:
        result = 'NO'

print(result)"""

"""num_1 = set(input())
num_2 = set(input())
print('YES' if any([set(i).issubset(num_2) for i in num_1]) else 'NO')"""

"""num_1 = set(input())
num_2 = set(input())
print('YES' if all([set(i).issubset(num_1) for i in num_2]) else 'NO')
"""

"""std_1 = set(input().split())
std_2 = set(input().split())
std_3 = set(input().split())

std_1_and_2 = set()

print(std_2)


for i in std_1:
    print(i)
    if len(i) >= 2:
        print(std_2.issubset(i))
        if set(i).issubset(std_2):
            std_1_and_2.add(i)

print(std_1.issubset(std_2))

z = []"""

"""for i in std_1_and_2:
    if set(i).isdisjoint(std_3):
        z.append(i)

print(' '.join(sorted(z, reverse=True)))"""

"""std_1 = set(input().split())
std_2 = set(input().split())
std_3 = set(input().split())

std_1_and_std_2 = std_1.intersection(std_2)
std_difference = std_1_and_std_2.difference(std_3)
print(*sorted(std_difference, reverse=True, key=int))
"""

"""set_1 = set(int(i) for i in input().split())
set_2 = set(int(i) for i in input().split())
set_3 = set(int(i) for i in input().split())

set_res = set_1.intersection(set_2, set_3)

set_res_2 = set_1.union(set_2, set_3)

set_dif = set_res_2.difference(set_res)
print(*sorted(set_dif))"""

"""set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
set_3 = set(map(int, input().split()))

set_1_2 = set_1.union(set_2)

set_res = set_3.difference(set_1_2)
print(*sorted(set_res, reverse=True, key=int))"""

"""set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
set_3 = set(map(int, input().split()))

set_res = set(x for x in range(10 + 1))

set_general = set_1.union(set_2, set_3)

set_last = set_res.difference(set_general)
print(*sorted(set_last))"""

"""words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']

set_res = {x[0].lower() for x in words}
print(*sorted(set_res))"""

# 1 Задание верное
"""lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

print(max(lst_1) * max(lst_2))


# Задание 2
countries = list(input().split(' '))
num_countries = int(input())

z = []

for _ in range(num_countries):
    new, old = input().split()
    if old in countries:
        countries.remove(old)
        countries.append(new)
print('-'.join(countries))"""

"""students = []
grades = []
while True:
    input_str = input().strip()
    if input_str == 'конец':
        break
    name, grade = input_str.split()
    grade = float(grade)
    if grade >= 8:
        students.append(name)
    grades.append(grade)

avg_grade = sum(grades) / len(grades)

print(', '.join(students))
print(avg_grade)"""

"""# Вопрос 1
def checkcolor(des, color):
    if color.lower() in des.lower():
        return True
    else:
        return False

print(checkcolor('Mersedes зелЕный', 'ЗеленыЙ'))



# Вопрос 2
def checksurname(sur, end):
    if sur[-len(end):] == end:
        return True
    else:
        return False



# Вопрос 3
def football(list):
    if list.count('победа') >= 3:
        return True
    elif list.count('победа') >= 2 and list.count('ничья') >= 2:
        return True
    else:
        return False



# Вопрос 4
def union(lst, union_name):
    count = 0
    for artist in lst:
        if artist.startswith(union_name + '-'):
            count += 1
    return f'Количество художников {count}'


# Вопрос 5
def checkemper(emp, user):
    user_list = user.split("/")
    user_years = int(user_list[1])
    if user_list[0] in emp.keys():
        years_list = emp[user_list[0]].split("-")
        start_year = int(years_list[0])
        end_year = int(years_list[1])
        if user_years == (end_year - start_year + 1):
            return True
        else:
            return False
    else:
        return False
    
    
# Вопрос 6
s = int(input())
r = int(input())

def checkclass(students, room):
    if students < room:
        return 'КАБИНЕТ ПОДХОДИТ'
    else:
        return 'КАБИНЕТ НЕ ПОДХОДИТ'


print(checkclass(s, r))"""

# Вопрос 7
"""def film_in_lib(film, director, collection):
    if director in collection:
        if film in collection[director]:
            return 'Фильм есть в коллекции'
    return 'Увы!'

lib = {'Д.Кемерон': ['Чужие', 'Титаник'], 'С.Спилберг': ['Список шиндлера', 'Война миров', 'Парк Юрского периода']}

film = input()
director = input()

print(film_in_lib(film, director, lib))"""

"""# Вопрос 5
def checkemper(emp, user):
    user_list = user.split("/")
    user_years = int(user_list[1])
    if user_list[0] in emp.keys():
        years_list = emp[user_list[0]].split("-")
        start_year = int(years_list[0])
        end_year = int(years_list[1])
        if user_years == (end_year - start_year + 1) or user_years == (start_year - end_year + 1):
            return True
        else:
            return False
    else:
        return False


print(checkemper({'Сы Юй Ди':'2043-2034', 'Сы Ци':'2033-1995', 'Сы Тай-кан':'1994-1982', 'Сы Чжун-кан':'1981-1953', 'Сы Сян':'1952-1886', 'Сы Шао-кан':'1885-1864', 'Сы Чжу':'1863- 1847'}, 'Сы Шао-кан/22'))
"""

"""# импортируем тип date из модуля datetime
from datetime import date

# выводим текущую дату
print(date.today())"""

"""# импортируем тип date из модуля datetime
from datetime import date

# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)"""

"""from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

for date in dates:
    if date.month in range(1, 3 + 1):
        print(f'{date.year}-Q1')
    elif date.month in range(4, 6 + 1):
        print(f'{date.year}-Q2')
    elif date.month in range(7, 9 + 1):
        print(f'{date.year}-Q3')
    else:
        print(f'{date.year}-Q4')"""

"""from datetime import date
def get_min_max(dates):
    return (min(dates), max(dates)) if dates else ()


print(get_min_max([]))"""

"""from datetime import date
def get_date_range(start, end):
    real_numbers = start.toordinal(), end.toordinal()
    if start.toordinal() > end.toordinal():
        return []
    else:
        for i in range(start.toordinal(), end.toordinal() + 1):
            return date.fromordinal(i)


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(get_date_range(date1, date2), sep='\n')"""

"""from datetime import date
def saturdays_between_two_dates(start, end):
    count_saturdays = 0

    if end < start:
        for i in range(end.toordinal(), start.toordinal() + 1):
            if date.fromordinal(i).isoweekday() == 6:
                count_saturdays += 1
        return count_saturdays

    else:
        for i in range(start.toordinal(), end.toordinal() + 1):
            if date.fromordinal(i).isoweekday() == 6:
                count_saturdays += 1
        return count_saturdays


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))"""

"""from datetime import time

alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))"""

"""from datetime import date

birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))"""

"""from datetime import date
# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%Y-%m-%d')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)"""

"""from datetime import date

andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number"""

"""from datetime import date

day_1, month_1, year_1 = input().split('-')
day_2, month_2, year_2 = input().split('-')

my_date_1 = date(int(day_1), int(month_1), int(year_1))
my_date_2 = date(int(day_2), int(month_2), int(year_2))

if my_date_1 < my_date_2:
    print(my_date_1.strftime('%d-%m (%Y)'))
else:
    print(my_date_2.strftime('%d-%m (%Y)'))"""

"""from datetime import date

num = int(input())

z = []

for _ in range(num):
    day_1, month_1, year_1 = input().split('-')
    my_date = date(int(day_1), int(month_1), int(year_1))
    z.append(my_date)

f = sorted(z)
for i in range(len(f)):
    print(f[i].strftime('%d/%m/%Y'))"""

"""from datetime import date
def print_good_dates(dates):
    lst = []
    for i in dates:
        z = str(i).split('-')
        if z[0] == '1992' and int(z[1]) + int(z[2]) == 29:
            lst.append(date(int(z[0]), int(z[1]), int(z[2])).strftime('%B %d, %Y').split())

    for j in sorted(lst, reverse=True, key=lambda x: x[1]):
        print(*j)


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)"""

"""from datetime import date
def is_correct(day, month, year):
    try:
        if date(year, month, day):
            return True

    except:
        return False

z = []
flag = 1
while flag != 2:
    date_num = input().split('.')
    try:
        z.append(1) if is_correct(int(date_num[0]), int(date_num[1]), int(date_num[2])) else z.append(0)
    except:
        break

for i in z:
    if i == 0:
        print('Некорректная')
    else:
        print('Корректная')

print(sum(z))"""

"""from datetime import datetime

def time_change(time_now=datetime.now()):
    date_1 = datetime.now()
    if date_1.strftime('%H') < str(12):
        return date_1.strftime('%H:%M AM')
    else:
        return date_1.strftime('%H:%M PM')

print(time_change())"""

# Написать программу, которая будет обновлять время, если оно изменилось


"""from datetime import datetime

def time_change(time_now=datetime.now()):
    date_now = datetime.now()
    i = date_now
    while i == date_now:
        return datetime.now().strftime('%H:%M PM')


print(time_change())"""

"""from datetime import datetime

print(date_now := datetime.now().strftime('%H:%M PM'))
i = 0
while i != 5:
    if date_now != datetime.now().strftime('%H:%M PM'):
        print(datetime.now().strftime('%H:%M PM'))
        i += 1
    else:
        continue"""

"""from datetime import datetime
import time

while True:
    date_now = datetime.now().strftime('%H:%M PM')
    print(date_now)
    time.sleep(60)"""

"""from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'

dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')

print(dt)"""

"""from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())"""

"""
from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

lst_am = []
lst_pm = []
for i in times_of_purchases:
    if i.hour >= 12:
        lst_pm.append(1)
    else:
        lst_am.append(1)

print('До полудня') if len(lst_am) > len(lst_pm) else print('После полудня')"""

"""from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]


z = []
dict_datetime = dict(zip(dates, times))
for i in dict_datetime:
    z.append(datetime.combine(i, dict_datetime[i]))

lst_result = (sorted(z, key=lambda x: x.second))

for j in lst_result:
    print(j)"""

"""from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

z = []
z_result = []
for i in data:
    a = datetime(int(data[i][0][6:10]), int(data[i][0][3:5]), int(data[i][0][0:2]), int(data[i][0][11:13]), int(data[i][0][14:16]), int(data[i][0][17:19])).timestamp()
    b = datetime(int(data[i][1][6:10]), int(data[i][1][3:5]), int(data[i][1][0:2]), int(data[i][1][11:13]), int(data[i][1][14:16]), int(data[i][1][17:19])).timestamp()
    z.append(i)
    z_result.append(b - a)

min_num = min(z_result)
min_index = z_result.index(min_num)

print(z[min_index])"""

"""from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))"""

"""from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = abs(today - birthday).days

print(days)"""

"""from datetime import date, timedelta

date_1 = input().split('.')
date_res = date(day=int(date_1[0]), month=int(date_1[1]), year=int(date_1[2]))

date_after = date_res - timedelta(days=1)
date_before = date_res + timedelta(days=1)

print(date_after.strftime('%d.%m.%Y'))
print(date_before.strftime('%d.%m.%Y'))"""

"""from datetime import date, timedelta, datetime, time

time_1 = input().split(':')

time_res = timedelta(hours=int(time_1[0]), minutes=int(time_1[1]), seconds=int(time_1[2]))

print(time_res.seconds)"""

"""from datetime import date, timedelta, datetime, time

timer = input().split(':')
timer_time = int(input())

timer_res = datetime(hour=int(timer[0]), minute=int(timer[1]), second=int(timer[2]), day=1, month=1, year=2001) + timedelta(seconds=timer_time)
print(timer_res.strftime('%H:%M:%S'))"""

"""from datetime import datetime, timedelta

pattern = '%H:%M:%S'
dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))

print(dt.strftime(pattern))"""

"""def num_of_sundays(year):
    from datetime import datetime, timedelta, date
    date_1 = datetime(year=year, day=1, month=1)
    if date_1.weekday() == 6 or year % 4 == 0 and (year % 100 != 0 and date_1.weekday() == 5 or year % 400 == 0 and date_1.weekday() == 5):
        return 53
    else:
        return 52


print(num_of_sundays(2021))"""

"""from datetime import datetime, timedelta, date

date_1 = input().split('.')

i = 0
num = 1
while i != 10:
    num += 1
    date_res = datetime(day=int(date_1[0]), month=int(date_1[1]), year=int(date_1[2]))
    final = date_res + timedelta(days=num)
    print(final)
    i += 1"""

"""from datetime import datetime, date, timedelta

date_1 = input().split('.')

date_default = datetime(day=int(date_1[0]), month=int(date_1[1]), year=int(date_1[2]))
date_2 = date_default + timedelta(days=2)
print(date_default.strftime('%d.%m.%Y'))
print(date_2.strftime('%d.%m.%Y'))

date_3 = date_2 + timedelta(days=3)
print(date_3.strftime('%d.%m.%Y'))

date_4 = date_3 + timedelta(days=4)
print(date_4.strftime('%d.%m.%Y'))

date_5 = date_4 + timedelta(days=5)
print(date_5.strftime('%d.%m.%Y'))

date_6 = date_5 + timedelta(days=6)
print(date_6.strftime('%d.%m.%Y'))

date_7 = date_6 + timedelta(days=7)
print(date_7.strftime('%d.%m.%Y'))

date_8 = date_7 + timedelta(days=8)
print(date_8.strftime('%d.%m.%Y'))

date_9 = date_8 + timedelta(days=9)
print(date_9.strftime('%d.%m.%Y'))

date_10 = date_9 + timedelta(days=10)
print(date_10.strftime('%d.%m.%Y'))"""

"""from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

z = []

for i in data:
    date_1 = abs(timedelta(hours=int(i[0][0:2]), minutes=int(i[0][3:6])) - timedelta(hours=int(i[1][0:2]), minutes=int(i[1][3:6])))
    z.append(date_1.seconds)

print(sum(z) // 60)
"""

# понедельник  сколько чисел 13 в понедельнике и т.д по дням недели
# вторник
# среда
# четверг
# пятница
# суббота
# воскресенье


"""
import time

start = time.time() ## точка отсчета времени

#время выполнения

from datetime import datetime, timedelta

date_1 = datetime(day=1, month=1, year=1)
date_2 = datetime(day=31, month=12, year=9999)


monday = 0
tuesday = 0
wednesday = 0
thirsday = 0
friday = 0
saturday = 0
sunday = 0

while date_1 != date_2:
    date_1 += timedelta(days=1)
    if date_1.day == 13 and date_1.weekday() == 0:
        monday += 1
    elif date_1.day == 13 and date_1.weekday() == 1:
        tuesday += 1
    elif date_1.day == 13 and date_1.weekday() == 2:
        wednesday += 1
    elif date_1.day == 13 and date_1.weekday() == 3:
        thirsday += 1
    elif date_1.day == 13 and date_1.weekday() == 4:
        friday += 1
    elif date_1.day == 13 and date_1.weekday() == 5:
        saturday += 1
    elif date_1.day == 13 and date_1.weekday() == 6:
        sunday += 1


print(monday)
print(tuesday)
print(wednesday)
print(thirsday)
print(friday)
print(saturday)
print(sunday)


#конец работы программу

end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени
"""

"""import time

start = time.time() ## точка отсчета времени

from datetime import datetime

def zeller_congruence(day, month, year):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    m = month
    q = day
    h = (q + 13*(m+1)//5 + k + k//4 + j//4 + 5*j) % 7
    return h

monday = 0
tuesday = 0
wednesday = 0
thirsday = 0
friday = 0
saturday = 0
sunday = 0

for y in range(1, 10000):
    for m in range(1, 13):
        if zeller_congruence(13, m, y) == 0:
            monday += 1
        elif zeller_congruence(13, m, y) == 1:
            tuesday += 1
        elif zeller_congruence(13, m, y) == 2:
            wednesday += 1
        elif zeller_congruence(13, m, y) == 3:
            thirsday += 1
        elif zeller_congruence(13, m, y) == 4:
            friday += 1
        elif zeller_congruence(13, m, y) == 5:
            saturday += 1
        elif zeller_congruence(13, m, y) == 6:
            sunday += 1

print(monday)
print(tuesday)
print(wednesday)
print(thirsday)
print(friday)
print(saturday)
print(sunday)

end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени"""

"""from datetime import datetime, timedelta, date

date_1 = datetime(day=20, month=3, year=2023, hour=10) #datetime.today()

if date_1.weekday() in (0, 1, 2, 3, 4):
    if timedelta(hours=21) < timedelta(hours=int(datetime.today().strftime('%H')), minutes=int(datetime.today().strftime('%M'))) < timedelta(hours=9):
        print('Магазин закрыт')
    elif timedelta(hours=21) > timedelta(hours=int(datetime.today().strftime('%H')), minutes=int(datetime.today().strftime('%M'))) >= timedelta(hours=10):
        bud = timedelta(hours=21) - timedelta(hours=int(datetime.today().strftime('%H')), minutes=int(datetime.today().strftime('%M')))
        print(bud.seconds // 60)


elif date_1.weekday() in (5, 6):
    if timedelta(hours=18) < timedelta(hours=int(datetime.today().strftime('%H')), minutes=int(datetime.today().strftime('%M'))) < timedelta(hours=10):
        print('Магазин закрыт')
    elif timedelta(hours=18) > timedelta(hours=int(datetime.today().strftime('%H')), minutes=int(datetime.today().strftime('%M'))) >= timedelta(hours=10):
        vih = timedelta(hours=18) - timedelta(hours=int(datetime.today().strftime('%H')), minutes=int(datetime.today().strftime('%M')))
        print(vih.seconds // 60)"""

"""from datetime import datetime, timedelta, date

date_in = input()
date_1 = datetime(day=int(date_in[0:2]), month=int(date_in[3:5]), year=int(date_in[6:10]), hour=int(date_in[11:13]), minute=int(date_in[14:16]))

if date_1.weekday() in (0, 1, 2, 3, 4):
    if timedelta(hours=21) <= timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))) or timedelta(hours=9) > timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))):
        print('Магазин не работает')

    elif timedelta(hours=21) > timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))) or timedelta(hours=9) <= timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))):
        bud = timedelta(hours=21) - timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M')))
        print(bud.seconds // 60)


elif date_1.weekday() in (5, 6):
    if timedelta(hours=18) <= timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))) or timedelta(hours=10) > timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))):
        print('Магазин не работает')

    elif timedelta(hours=18) > timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))) or timedelta(hours=10) <= timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M'))):
        vih = timedelta(hours=18) - timedelta(hours=int(date_1.strftime('%H')), minutes=int(date_1.strftime('%M')))
        print(vih.seconds // 60)"""

"""import time, timeit

def calculate_it(func, *args):
    return (func(), timeit.timeit(func))



print(calculate_it(add, 1, 2, 3))"""

"""import calendar

num = int(input())
z = []

for _ in range(num):
    year = int(input())
    z.append(calendar.isleap(year))
for i in z:
    print(i)"""

"""import calendar

date_1 = input().split(' ')
month_name = date_1[1]
if month_name in list(calendar.month_abbr):
    gen = list(calendar.month_abbr).index(month_name)
    print(calendar.month(int(date_1[0]), gen))"""

"""import calendar

year = input().split('-')
weekday_num = calendar.weekday(int(year[0]), int(year[1]), int(year[2]))
print(calendar.day_name[weekday_num])"""

"""import calendar

date_1 = input().split(' ')
if date_1[1] in list(calendar.month_name):
    gen = list(calendar.month_name).index(date_1[1])
    month_days = calendar.monthrange(int(date_1[0]), gen)
    print(month_days[1])"""

"""def get_days_in_month(year, month):
    import calendar
    from datetime import date
    gen = list(calendar.month_name).index(month)
    month_matrics = calendar.monthcalendar(year, gen)

    z = []

    for i in month_matrics:
        for j in i:
            if j == 0:
                pass
            else:
                z.append(date(year=year, month=gen, day=j))
    return z


print(get_days_in_month(2021, 'December'))"""

"""def get_all_mondays(year):
    import calendar
    from datetime import date, timedelta
    date_1 = date(year=year, month=1, day=1)
    z = []
    for _ in range(365):
        if calendar.weekday(year=int(date_1.strftime('%Y')), month=int(date_1.strftime('%m')), day=int(date_1.strftime('%d'))) == 0:
            z.append(date_1)
            date_1 += timedelta(days=1)
        else:
            date_1 += timedelta(days=1)
    return z


print(get_all_mondays(2021))"""

"""import calendar
from datetime import datetime, date, timedelta

year = int(input())
date_start = date(year=year, month=1, day=1)

z = []

month_num = 1

count = 0
for _ in range(365):
    date_start += timedelta(days=1)
    if calendar.weekday(year=int(date_start.strftime('%Y')), month=int(date_start.strftime('%m')), day=int(date_start.strftime('%d'))) == 3:
        count += 1
        if count == 3:
            z.append(date_start)
            count = 0
            month_num += 1
            print(date_start.month)
            print(month_num)
            #while int(date_start.strftime('%m')) != month_num:
                #print(month_num)
                #print(date_start.month)
                #date_start += timedelta(days=1) # как то добавить + 1 месяц
        else:
            continue
            #date_start += timedelta(days=1)


print(z)
for i in z:
    print(i.strftime('%d.%m.%Y'))"""

"""year_1 = int(input())
def get_all_mondays(year):
    import calendar
    from datetime import date, timedelta
    date_1 = date(year=year, month=1, day=1)
    z = []
    for _ in range(365):
        if calendar.weekday(year=int(date_1.strftime('%Y')), month=int(date_1.strftime('%m')), day=int(date_1.strftime('%d'))) == 3:
            z.append(date_1)
            date_1 += timedelta(days=1)
        else:
            date_1 += timedelta(days=1)
    #return z
    for i in z:
        #print(i)
        if z.index(i) == 2 or z.index(i) == 6 or z.index(i) == 10 or z.index(i) == 14 or z.index(i) == 19 or z.index(i) == 23 or z.index(i) == 27 or z.index(i) == 32 or z.index(i) == 36 or z.index(i) == 41 or z.index(i) == 45 or z.index(i) == 49:
            print(i.strftime('%d.%m.%Y'))


print(get_all_mondays(year_1))"""

"""import sys

lst = [x[::-1].strip('\n') for x in sys.stdin]
for i in lst:
    print(i)"""

"""import sys
from datetime import datetime

lst = sorted([datetime.strptime(i.strip(), '%Y-%m-%d') for i in sys.stdin.readlines()])
res = max(lst) - min(lst)
print(res.days)"""

"""import sys

lst = [int(x) for x in sys.stdin]

if len(lst) % 2 == 0 and lst[-1] % 2 == 0:
    print('Дима')
elif len(lst) % 2 != 0 and lst[-1] % 2 != 0:
    print('Дима')
else:
    print('Анри')"""

"""import sys
from statistics import mean

try:
    lst = [int(x) for x in sys.stdin]

    print(f'Рост самого низкого ученика: {min(lst)}')
    print(f'Рост самого высокого ученика: {max(lst)}')
    print(f'Средний рост: {mean(lst)}')
except:
    print('нет учеников')"""

"""import sys
for line in sys.stdin:
    if (line.lstrip(' ')[0] != '#'):
        print(line.rstrip('\n'))"""

"""import sys

lst = [x.strip('\n') for x in sys.stdin]
#print(lst)

res = []

if lst[-1] == 'Политика':
    for line in lst:
        #print(line.split('/'))
        try:
            if line.split('/')[1] == ' Политика ':
                res.append(line.split('/'))
        except:
            break

    #print(res)  # код работает

elif lst[-1] == 'Общество':
    for line in lst:
        #print(line.split('/'))
        try:
            if line.split('/')[1] == ' Общество ':
                res.append(line.split('/'))
        except:
            break

    #print(res)  # код работает

elif lst[-1] == 'Авиация':
    for line in lst:
        #print(line.split('/'))
        try:
            if line.split('/')[1] == ' Авиация ':
                res.append(line.split('/'))
        except:
            break

    #print(res)  # код работает

#print(res[-1][-1])

for i in sorted(res, key=lambda x: (float(x[-1]), x)):
    print(i[0].strip())"""

"""import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(csv_file, delimiter=';')
    # выводим каждую строку
    for row in rows:
        print(row)"""

"""import csv

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})"""

"""import csv

with open('sales.csv', 'r', encoding='utf-8') as csv_file:
    sales = csv.DictReader(csv_file, delimiter=';')
    for row in sales:
        if int(row['old_price']) > int(row['new_price']):
            print(row['name'])
        #print(row['name'] if int(row['old_price']) > int(row['new_price']) else '')"""

"""import csv

with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
    lst_names = {}
    dict_comp = csv.DictReader(csv_file, delimiter=';')
    for row in dict_comp:
        lst_names.setdefault(row['company_name'], int(row['salary']))
    print(lst_names)  # компании не повторяются, но нужно как-то суммировать среднюю зарплату

    #sorting = sorted(dict_comp, key=lambda x: (int(x['salary']), (x['company_name'])))
    #for row in sorting:
    #    print(row['company_name'])"""

"""import csv

num = int(input())

with open('deniro.csv', 'r', encoding='utf-8') as csv_file:
    text = csv.reader(csv_file, delimiter=',')
    if num == 1:
        result = sorted(text, key=lambda x: x[0])
        for i in result:
            print(','.join(i))

    elif num == 2:
        result_2 = sorted(text, key=lambda x: int(x[1]))
        for i in result_2:
            print(','.join(i))

    elif num == 3:
        result_3 = sorted(text, key=lambda x: int(x[2]))
        for i in result_3:
            print(','.join(i))"""

"""def csv_columns(filename):
    import csv
    with open(filename, "r") as csv_file:
        result = csv.DictReader(csv_file, delimiter=',')
        field_res = result.fieldnames  # сделать проверку на количество столбцов
        if len(field_res) == 2:
            first_lst = []
            second_lst = []
            for row in result:
                first_lst.append(row['name'])
                second_lst.append(row['year'])
                # еще два списка
            print(first_lst)
            
            
print(csv_columns('deniro.csv'))"""

"""def csv_columns(filename):
    import csv
    with open(filename, "r") as csv_file:
        result = csv.DictReader(csv_file, delimiter=',')
        field_res = result.fieldnames  # сделать проверку на количество столбцов
        if len(field_res) == 3:
            first_lst = []
            second_lst = []
            third_lst = []
            for row in result:
                first_lst.append(row[field_res[0]])
                second_lst.append(row[field_res[1]])
                third_lst.append(row[field_res[2]])
            res_dict = dict()
            res_dict.setdefault(field_res[0], first_lst)
            res_dict.setdefault(field_res[1], second_lst)
            res_dict.setdefault(field_res[2], third_lst)
            return res_dict
        elif len(field_res) == 2:
            first_lst = []
            second_lst = []
            for row in result:
                first_lst.append(row[field_res[0]])
                second_lst.append(row[field_res[1]])
            res_dict = dict()
            res_dict.setdefault(field_res[0], first_lst)
            res_dict.setdefault(field_res[1], second_lst)
            return res_dict

print(csv_columns('deniro.csv'))"""

"""#with open('data.csv', 'r', encoding='utf-8') as file_csv:
    import csv
    result = csv.DictReader(file_csv, delimiter=',')
    dict_email = dict()
    z = []
    for row in result:
        email_lst = row['email'].split('@')
        dict_email.setdefault(email_lst[1], (email_lst.count(email_lst[1])))
        z.append(email_lst[1])
    for i in z:
        if i in dict_email:
            dict_email[i] += 1

    res_dict = dict_email  # итерируемся по словарю, чтобы уменьшить значение каждого на -1
    for j in res_dict:
        res_dict[j] -= 1
    print(res_dict)
    #print(z)
    # теперь нужно перезаписать все в файл

    fieldnames = ['domain', 'count']

    with open('domain_usage.csv', 'w', encoding='utf-8') as write_file:
        res = csv.DictWriter(write_file, delimiter=',', fieldnames=fieldnames)
        res.writeheader()
        for row in res_dict:
            res.writerow(row)"""

"""#with open('wifi.csv', 'r', encoding='utf-8') as csv_file:
    import csv
    result = csv.DictReader(csv_file, delimiter=';')
    dict_info = dict()
    z = []
    for i in result:
        #print(i['district'], i['number_of_access_points'])
        z.append(i['district'])
        dict_info.setdefault(i['district'], int(i['number_of_access_points']))
    print(dict_info)
    print(z)
    for j in z:
        # я посчитал количество упоминаний района, а не количество точек
        print(j)
        print(dict_info[j])
        #dict_info[j] += int(i['number_of_access_points'])

    print(dict_info)"""

"""import csv

with open("wifi.csv", 'r', encoding='UTF-8') as f:
    reader = csv.DictReader(f, delimiter=';')

    with open('new_file.csv', 'w', encoding='UTF-8') as f:
        header = ['adm_area', 'district', 'location', 'number_of_access_points']
        writer = csv.DictWriter(f, fieldnames=header, delimiter=';')
        writer.writeheader()
        for line in reader:
            writer.writerow(line)"""

"""*********************************Приложение на ткинтер****************************************"""
"""from tkinter import *
from tkinter import filedialog

import csv

from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('400x300')2

frame = Frame(
   root,
   padx=10,
   pady=10
)
frame.pack(expand=True)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            text.delete("1.0", END)
            text.insert(END, content)

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            content = text.get("1.0", END)
            f.write(content)

text = Text(root)
text.pack()

btn_load = Button(frame, text="Load", command=load_file)

btn_load.pack()

btn_save = Button(frame, text="Save", command=save_file)

btn_save.pack()

root.mainloop()"""
"""*****************************Конец приложения на ткинтер******************************************"""

"""#with open('wifi.csv', 'r', encoding='utf-8') as f:
    import csv
    reader = csv.DictReader(f, delimiter=';')

    res = {}
    for line in reader:
        count_points = int(line['number_of_access_points'])
        district_only = line['district']
        try:
            res[district_only] += count_points
        except:
            res[district_only] = count_points

    final_res = res.items()
    for i in sorted(final_res, key=lambda x: (-x[1], x[0])):
        print(f'{i[0]}: {i[1]}')"""

"""import csv
with open('titanic.csv', 'r', encoding='utf-8') as file:
    result = csv.DictReader(file, delimiter=';')

    surv_man = []  # список выживших мужчин которым меньше 18
    surv_woman = []  # список выживших женщин которым меньше 18

    for i in result:
        if int(i['survived']) == 1 and float(i['age']) < 18 and i['sex'] == 'male':
            surv_man.append(i['name'])
        elif int(i['survived']) == 1 and float(i['age']) < 18 and i['sex'] == 'female':
            surv_woman.append(i['name'])

    for man in surv_man:
        print(man)
    for woman in surv_woman:
        print(woman)"""

"""import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

result = json.dumps(countries, indent=3, separators=(',', ' - '), sort_keys=True)
print(result)"""

"""import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.dumps(words, skipkeys=True)
print(data_json)"""

"""import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

lst = [club1, club2, club3]

with open('data.json', mode='w', encoding='utf-8') as file:
    json.dump(lst, fp=file, indent=3)"""

"""import json

specs = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }

specs_json = json.dumps(specs, ensure_ascii=False, indent=3)

print(specs_json)"""

"""def is_correct_json(string):
    import json
    try:
        json.loads(string)
        return True
    except:
        return False

data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))"""

"""import json, sys

data = json.load(sys.stdin)


for i in data:
    if type(data[i]) == list:
        print(f'{i}:', ', '.join(map(str, data[i])))
    else:
        print(f'{i}: {data[i]}')"""

"""import json
with open('data.json', mode='r', encoding='utf-8') as r_file:
    final_lst = []
    result = json.load(r_file)
    for i in result:
        if type(i) == str:
            final_lst.append(i + '!')
        elif type(i) == int:
            final_lst.append(i + 1)
        elif type(i) == bool:
            final_lst.append(not i)
        elif type(i) == list:
            final_lst.append(i + i)
        elif type(i) == dict:
            i.update({"newkey": None})
            final_lst.append(i)
        elif type(i) == None:
            pass
    with open('updated_data.json', mode='w') as w_file:
        json.dump(final_lst, w_file, indent=2)"""

"""import json

with open('data1.json', mode='r') as fread_1, open('data2.json', mode='r') as fread_2:
    result_1 = json.load(fread_1)
    result_2 = json.load(fread_2)
    result_1.update(result_2)

    with open('data_merge.json', mode='w') as result_json:
        json.dump(result_1, result_json, indent=2)
"""

"""import json

with open('people.json', mode='r', encoding='utf-8') as r_file:
    result = json.load(r_file)
    for j in result:

            if "age" not in j:
                j.update({"age": None})
            if "name" not in j:
                j.update({"name": None})
            if "country" not in j:
                j.update({"country": None})
            if "phone" not in j:
                j.update({"phone": None})
            if "family_status" not in j:
                j.update({"family_status": None})
            if "email" not in j:
                j.update({"email": None})
            if "children" not in j:
                j.update({"children": None})
            if "university" not in j:
                j.update({"university": None})


    with open("updated_people.json", mode='w', encoding='utf-8') as w_file:
        json.dump(result, w_file, indent=3)"""

"""import json

with open("countries.json", mode='r', encoding='utf-8') as r_file:
    result = json.load(r_file)

    islam_countries = []  # список стран в которых религия ислам

    christianity_countries = []

    hinduism_countries = []

    buddhism_countries = []

    Unaffiliated_Religions_countries = []

    Judaism_countries = []

    Folk_Religions_countries = []

    for i in result:
        if i['religion'] == 'Islam':
            islam_countries.append(i['country'])
        elif i['religion'] == 'Christianity':
            christianity_countries.append(i['country'])
        elif i['religion'] == 'Hinduism':
            hinduism_countries.append(i['country'])
        elif i['religion'] == 'Buddhism':
            buddhism_countries.append(i['country'])
        elif i['religion'] == 'Unaffiliated Religions':
            Unaffiliated_Religions_countries.append(i['country'])
        elif i['religion'] == 'Judaism':
            Judaism_countries.append(i['country'])
        elif i['religion'] == 'Folk Religions':
            Folk_Religions_countries.append(i['country'])

    final_dict = dict()
    final_dict.update({"Islam": islam_countries})
    final_dict.update({"Christianity": christianity_countries})
    final_dict.update({"Hinduism": hinduism_countries})
    final_dict.update({"Buddhism": buddhism_countries})
    final_dict.update({"Unaffiliated Religions": Unaffiliated_Religions_countries})
    final_dict.update({"Judaism": Judaism_countries})
    final_dict.update({"Folk Religions": Folk_Religions_countries})

    with open("religion.json", mode='w', encoding='utf-8') as w_file:
        json.dump(final_dict, w_file, indent=3)"""

"""import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('OK', self)
        btn.setToolTip('This is a "OK" widget')
        btn.resize(btn.sizeHint())
        btn.move(170, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This is quit button')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(700, 300, 450, 350)
        self.setWindowTitle('Tooltips')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())"""

"""import csv, json

with open('students.json', mode='r', encoding='utf-8') as r_file:
    result = json.load(r_file)

    final_lst = []

    for i in result:
        if i['age'] >= 18 and i['progress'] >= 75:
            final_lst.append(i)

    for j in final_lst:
        del j['city']
        del j['age']
        del j['progress']


    sort_lst = sorted(final_lst, key=lambda x: x['name'])

    columns = ['name', 'phone']

    with open('data.csv', mode='w', encoding='utf-8', newline='') as w_file:
        writer = csv.DictWriter(w_file, fieldnames=columns)
        writer.writeheader()
        for row in sort_lst:
            writer.writerow(row)"""

"""import eel

eel.init('Web')

eel.start('C:\Every_forPyCharm\Python_GIT_1\Web\main.html', size=(700, 700), mode='chrome')"""

"""import json

with open("pools.json", mode='r', encoding='utf-8') as r_file: # открываю файл в кодировке urf-8
    polls_dict = json.load(r_file)  # из файла json преобразую в обычный питон словарь
    time_result = []  # создаю список в который буду добавлять адреса и длину и ширину бассейна подходящие условиям
    for line in polls_dict:
        # Если время в понедельник начинается с 10 и время закрытия бассейна минус 10 больше либо равны 2
        # тогда добавляю адрес этого места и его длину и ширину
        if int(line['WorkingHoursSummer']['Понедельник'].split('-')[0][0:2]) == 10 and (int(line['WorkingHoursSummer']['Понедельник'].split('-')[1][0:2]) - int(line['WorkingHoursSummer']['Понедельник'].split('-')[0][0:2]) >= 2):
            time_result.append((line['Address'], line['DimensionsSummer']['Length'], line['DimensionsSummer']['Width']))

    final_result = max(time_result, key=lambda x: (int(x[1]), int(x[2])))  # с помощью лямбда сортировки нахожу самый длинный бассейн
    print(f'{final_result[1]}x{final_result[2]}')  # Вывожу результат
    print(final_result[0])"""

"""from zipfile import ZipFile

with ZipFile("just.zip", mode='w') as zip_file:
    zip_file.write('sales.csv')
    zip_file.write('pools.json')
    zip_file.printdir()
    print(zip_file.namelist())"""

"""from zipfile import ZipFile

with ZipFile('workbook.zip', mode='r') as zip_file:
    res = zip_file.infolist()

    info = sum([not line.is_dir() for line in res])
    print(info)"""

"""from zipfile import ZipFile

with ZipFile('workbook.zip', mode='r') as zip_file:
    res = zip_file.infolist()

    num_original = 0

    for file in res:
        num_original += file.file_size

    num_convert = 0

    for file in res:
        num_convert += file.compress_size

    print(f'Объем исходных файлов: {num_original} байт(а)')
    print(f'Объем сжатых файлов: {num_convert} байт(а)')"""

"""from zipfile import ZipFile

with ZipFile('workbook.zip', 'r') as zip_file:
    info = zip_file.infolist()

    result = []

    for file in info:
        try:
            result.append([file.filename, (file.compress_size / file.file_size) * 100])
        except:
            continue

    final = (min(result, key=lambda x: x[1]))

    answer = final[0].split('/')
    print(answer[-1])"""

"""from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip', mode='r') as zip_file:
    res = zip_file.infolist()

    date_original = datetime(year=2021, month=11, day=30, hour=14, minute=22)

    final_files = []

    for file in res:
        date_file = datetime(year=file.date_time[0], month=file.date_time[1], day=file.date_time[2], hour=file.date_time[3], minute=file.date_time[4])
        if date_original < date_file and not file.is_dir():
            final_files.append(file.filename)

    z = []

    for line in final_files:
        z.append(line.split('/')[-1])

    result = sorted(z, key=lambda x: x)

    print(*result, sep='\n')"""

"""from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip', 'r') as zip_file:
    res = zip_file.infolist()
    for file1 in sorted(res, key=lambda x: x.filename.split('/')[-1]):  # отсортировать по алфавиту
        if not file1.is_dir():
            print(file1.filename.split('/')[-1])
            print(f'  Дата модификации файла: {datetime(year=file1.date_time[0], month=file1.date_time[1], day=file1.date_time[2], hour=file1.date_time[3], minute=file1.date_time[4], second=file1.date_time[5])}')
            print(f'  Объем исходного файла: {file1.file_size} байт(а)')
            print(f'  Объем сжатого файла: {file1.compress_size} байт(а)')
            print()"""

"""from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    for file1 in file_names:
        zip_file.write(file1)"""

"""from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    for file in file_names:
        file_conv = os.path.getsize(file)
        if file_conv <= 100:
            zip_file.write(file)
"""

"""from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name, mode='r') as zip_file:
        if args:
            zip_file.extractall(members=args)
        elif args == ():
            zip_file.extractall()


extract_this('just.zip', 'pools.json')"""

"""import pickle, sys

file1 = str(input())  # ввод pkl файла

words = []

for line in sys.stdin:
    words.append(str(line.strip('\n')))

with open(file1, mode='rb') as pkl_file:
    elem_func = pickle.load(pkl_file)
    #elem_func(*words)
    print(elem_func(*words))"""

# with open(filename, mode='rb') as read_file:
#    result1 = pickle.load(read_file)

"""import pickle

def filter_dump(filename, objects, typename):
    z = []
    for elem in objects:
        if type(elem) == typename:
            z.append(elem)

    with open('filename.pkl', mode='wb') as write_file:
        result2 = pickle.dump(z, write_file)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)"""

"""x = {
    '🅐': 'a', '🅑': 'b', '🅒': 'c', '🅓': 'd', '🅔': 'e',
    '🅕': 'f', '🅖': 'g', '🅗': 'h', '🅘': 'i', '🅙': 'j', '🅚': 'k',
    '🅛': 'l', '🅜': 'm', '🅝': 'n', '🅞': 'o', '🅟': 'p', '🅠': 'q', '🅡': 'r', '🅢': 's',
    '🅣': 't', '🅤': 'u', '🅥': 'v', '🅦': 'w', '🅧': 'x', '🅨': 'y', '🅩': 'z'
}"""

"""letters = 'abcdefghijklmnopqrstuvwxyz'

new_alphabet = str(input())
phrase = str(input().lower())

slovar = dict()

for i in range(len(letters)):
    slovar[letters[i]] = new_alphabet[i]

result = phrase.maketrans(slovar)

print(phrase.translate(result))"""

"""from collections import namedtuple

Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])"""

"""from collections import namedtuple

Game = namedtuple('Game', 'name developer publisher')

res = Game._fields

ExtendedGame = namedtuple('ExtendedGame', (*res, 'release_date', 'price'))

print(ExtendedGame._fields)"""

"""import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])


with open("data.pkl", 'rb') as r_file:
    obj = pickle.load(r_file)
    for line in obj:
        print(f'name: {line.name}')
        print(f'family: {line.family}')
        print(f'sex: {line.sex}')
        print(f'color: {line.color}')
        print()"""

"""from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

result = []

gold_plan = []
silver_plan = []
bronze_plan = []
basic_plan = []

for line in users:
    if line.plan == 'Gold':
        gold_plan.append([line.name, ' ', line.surname, '\n', f'  Email: {line.email}', '\n', f'  Plan: {line.plan}', '\n'])
    elif line.plan == 'Silver':
        silver_plan.append([line.name, ' ', line.surname, '\n', f'  Email: {line.email}', '\n', f'  Plan: {line.plan}', '\n'])
    elif line.plan == 'Bronze':
        bronze_plan.append([line.name, ' ', line.surname, '\n', f'  Email: {line.email}', '\n', f'  Plan: {line.plan}', '\n'])
    elif line.plan == 'Basic':
        basic_plan.append([line.name, ' ', line.surname, '\n', f'  Email: {line.email}', '\n', f'  Plan: {line.plan}', '\n'])

result.append([sorted(gold_plan, key=lambda x: x[4][9:]), sorted(silver_plan, key=lambda x: x[4][9:]), sorted(bronze_plan, key=lambda x: x[4][9:]), sorted(basic_plan, key=lambda x: x[4][9:])])

for line in result:
    for i in line:
        for j in i:
            print(''.join(j))"""

"""# gdfbdfgb
from collections import namedtuple
import csv
from datetime import datetime, time

with open('meetings.csv', mode='r', encoding='utf-8') as r_file:
    obj = csv.DictReader(r_file, delimiter=',')

    res_time = []

    for line in obj:
        res_time.append([line, line['meeting_date'].split('.')])
        #print(line['meeting_date'].split('.'))

    for i in res_time:
        print(i[1])

    print(sorted(res_time, key=lambda x: datetime(int(x[1][0]),  int(x[1][1]), int(x[1][2]))))
    # доделать сортировку по дате и времени, все остальное уже сделано"""

"""from collections import namedtuple
import csv
from datetime import datetime

with open('meetings.csv', mode='r', encoding='utf-8') as r_file:
    obj = csv.DictReader(r_file, delimiter=',')

    res_time = []

    for line in obj:
        res_time.append(line)

    final_lst = sorted(res_time, key=lambda x: (datetime.strptime(x['meeting_date'], '%d.%m.%Y'), datetime.strptime(x['meeting_time'], '%H:%M')))
    for row in final_lst:
        print(row['surname'], row['name'])"""

"""from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]

info = defaultdict(int)

for line in data:
    if line[0] in info:
        info[line[0]] += line[1]
    else:
        info[line[0]] = line[1]

for res in sorted(info.items()):
    print(f'{res[0]}: ${res[1]}')"""

"""from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
         ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
         ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
         ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
         ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
         ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
         ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
         ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
         ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
         ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
         ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'),
         ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
         ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
         ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
         ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
         ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
         ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

info = defaultdict(int)

for line in staff:
    if line[0] in info:
        info[line[0]] += 1
    else:
        info[line[0]] = 1

for res in sorted(info.items()):
    print(f'{res[0]}: {res[1]}')"""


"""from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]

#  staff_broken

info = defaultdict(str)

for line in staff_broken:
    print(info.values())
    if line[0] in info and line[1] not in info.values():  # не выполняется так как он добавляет имена в одну строку
        info[line[0]] += line[1]  # исправить, так как добавляется просто строка, а нужно чтобы был новый элемент!!!
    else:
        info[line[0]] = line[1]

for res in info.items():
    print(res[0], ': ', res[1])"""


"""from collections import defaultdict

def wins(pairs):
    info = defaultdict(str, pairs)
    return info




result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))"""


"""#with open('aud_trans_1_1.txt', mode='r', encoding='utf-8') as file:
    z = []
    for line in file:
        if line != '\n':
            z.append(line)

    result = []

    for i, row in enumerate(z):
        if i % 2 == 0:
            result.append(f'Интервьюер: {row}')
        elif i % 2 != 0:
            result.append(f'Информант: {row}')

    with open('result_aud_1_1.txt', mode='w', encoding='utf-8') as w_file:
        w_file.writelines(result)"""


# действую так:
# 1 конвертирую аудио в текст на гугле
# 2 копирую текст и исправляю сам
# 3 пропускаю через прогу и проверяю
# 4 сохраняю в блокнот и называю: Интервью номер ""


"""#with open('audio_transkrib.txt', mode='r', encoding='utf-8') as file:
    z = []
    for line in file:
        z.append(line)


    with open('result_aud_1_1.txt', mode='w', encoding='utf-8') as w_file:

        word_orig = "inter"

        for row in z:
            if row == '\n':
                w_file.write('\n')
                if word_orig == "inter":
                    w_file.write('Интервьюер:')
                    word_orig = "infor"
                elif word_orig == "infor":
                    w_file.write('Информант:')
                    word_orig = "inter"



            w_file.write(row)

# ---------------------------------------------------------------------

        doc = docx.Document()

        with open('result_aud_1_1.txt', 'r', encoding='utf-8') as file:
            is_bold = False
            for line in file:
                if line.startswith('Интервьюер'):
                    is_bold = True
                    doc.add_paragraph(line.strip()).runs[0].bold = True
                elif line.startswith('Информант'):
                    is_bold = False
                    doc.add_paragraph(line.strip())
                elif is_bold:
                    doc.add_paragraph(line.strip()).runs[0].bold = True
                else:
                    doc.add_paragraph(line.strip())

        doc.save('result.docx')"""






    # переделать на меняющуюся переменную, которая будет определять
    # следующий информант или интервьюер


"""import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "0d920eb501msh22181cce92091a1p14cbefjsn779898d73a66",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())"""


"""import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
headers = {
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
    "X-RapidAPI-Key": "0d920eb501msh22181cce92091a1p14cbefjsn779898d73a66",
    "Content-Type": "application/x-www-form-urlencoded"
}

text = "Hello, world!"
params = {
    "source": "en",
    "target": "ru",
    "q": text
}

response = requests.post(url, headers=headers, params=params)
print(response.json())
result = response.json()["data"]["translations"][0]["translatedText"]

print(result)  # Привет, мир!"""


"""import customtkinter
import webbrowser
import tkinter

from PIL import Image, ImageTk
from translate import Translator

current_language = ""  # переменная для сменя языка в комбобоксе 3244 строка
language_to_translate = ""  # переменная для смены языка перевода

translator = Translator(from_lang=current_language, to_lang=language_to_translate)


customtkinter.set_appearance_mode("#1f1f1f")
app = customtkinter.CTk()
app.geometry("1000x500")


label = customtkinter.CTkLabel(app, text="Переводчик", fg_color="#353333", width=1000, height=50, font=("Montserrat", 18))
label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

# Краткое описание

url_lable = customtkinter.CTkLabel(app, text="Поддержите разработчиков данного проекта, подписавшись на их канал", fg_color='#393838', width=900, height=75, font=("Montserrat", 16))
url_lable.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)


# -----------------------------------------------------------------


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)
    if choice == "Русский":
        current_language = "ru"
    elif choice == "Английский":
        current_language = "en"
    elif choice == "Немецкий":
        current_language = "de"
    elif choice == "Итальянский":
        current_language = "it"

combobox = customtkinter.CTkComboBox(app, values=["Русский", "Английский", "Немецкий", "Итальянский"],
                                     command=combobox_callback, width=150, height=34, font=("Montserrat", 15))
combobox.place(relx=0.5, rely=0.55)
combobox.set("Русский")

# -----------------------------------------------------------------


app.mainloop()"""


"""def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data[key] = []
        data[key].append(element)




data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data=data, key='c', element=7)

print(data)"""


"""try:
    file_name = str(input())
    file = open(file=file_name, encoding='utf-8', mode='r')
    try:
        print(file.read())
    finally:
        file.close()
except FileNotFoundError:
    print('Файл не найден')"""


"""z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = int(input())
result = []
for i in z[k:-1]:
    result.append(i)
for j in z[0:k]:
    result.append(j)
print(result)"""


"""import matplotlib.pyplot as plt

# Пример баллов за экзамен для 20 пробных вариантов

exam_scores = []
for i in range(20):
    num = int(input())
    exam_scores.append(num)

result = 0
for j in exam_scores:
    result += j

# Создаем график
plt.plot(exam_scores, marker='o', linestyle='-', linewidth=1)

# Настраиваем оси
plt.xlabel('Пробный вариант')
plt.ylabel('Баллы за экзамен')
plt.title(f'Средний балл: {result / 20}')

# Отображаем график
plt.show()"""


"""def get_weekday(number):
    data = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг",
            5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    if type(number) != int:
        raise TypeError("Аргумент не является целым числом")
    elif number not in range(1, 8):
        raise ValueError("Аргумент не принадлежить целому диапозону")
    return data[number]"""


"""def get_id(names: list, name: str):
    if type(name) != str:
        raise TypeError("Имя не является строкой")
    elif not name[0].isupper() or not name[1:].islower() or not name.isalpha():
        raise ValueError("Имя не является корректным")
    return len(names) + 1

print(get_id(["Timur", "Oleg"], "Gahya"))"""



"""import json
name_file = str(input())

try:
    with open(name_file, "r") as f_js:
        try:
            data = json.load(f_js)
            print(data)
        except json.decoder.JSONDecodeError:
            print("Ошибка при десериализации")

except FileNotFoundError:
    print("Файл не найден")"""



"""def is_good_password(string: str) -> bool:
    if len(string) >= 9 and any([x.isupper() for x in string]) and any([x.islower() for x in string]) and any([x.isdigit() for x in string]):
        return True
    else:
        return False


print(is_good_password('HELLO1234'))"""



"""class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string: str):
    try:
        if len(string) >= 9:
            try:
                if any([x.isupper() for x in string]) and any([x.islower() for x in string]):
                    try:
                        if any([x.isdigit() for x in string]):
                            return "Success!"
                        else:
                            raise DigitError("DigitError")
                    except DigitError as err:
                        return err
                else:
                    raise LetterError("LetterError")
            except LetterError as err:
                return err
        else:
            raise LengthError("LengthError")
    except LengthError as err:
        return err



import sys

z = []
for j in sys.stdin:
    z.append(j.strip())

for i in z:
    g = is_good_password(i)
    print(g)
    if g == 'Success!':
        break"""




# Рекурсия -------------------------------------------------------------------------------------------

# Один из легких примеров того, как работает рекурсия!
"""def draw_rect(width, height, step):
    if step < height:
        print('*' * width)
        draw_rect(width, height, step + 1)

draw_rect(4, 3, 0)"""

# Пример с использованием вложенных функций
"""def draw_rect(width, height):
    def rec(step):
        if step < height:
            print('*' * width)
            rec(step + 1)
    rec(0)

draw_rect(4, 3)"""


"""def traffic(n):
    def rec(step):
        if step < n:
            print("Не парковаться")
            rec(step + 1)
    rec(0)


traffic(0)"""


"""def numbers(start, stop):
    if start <= stop:
        print(start)
        numbers(start + 1, stop)


numbers(1, 100)"""


"""numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
           437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
           323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
           984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351,
           777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]

def list_of_numbers(data: list, step=0):
    if step < len(data):
        print(f'Элемент {step}: {data[step]}')
        list_of_numbers(data, step + 1)


list_of_numbers(numbers)"""



"""z = []
while True:
    a = int(input())
    z.append(a)
    if a == 0:
        break

def list_reverse(data: list, step = -1):
    print(data[step])
    if abs(step) < len(data):
        list_reverse(data, step - 1)


list_reverse(z)"""




# Рисование елки сверху вниз (обычная)
"""def triangle(h):
    if h != 0:
        triangle(h - 1)
        print('*' * h)


triangle(5)"""


# Рисование елки снизу вверх (перевернутая)
"""def triangle(h):
    print("*" * h)
    if h != 0:
        triangle(h - 1)


triangle(5)"""



# 16 сумма каждого ряда
"""def bee(num: int, n):
    if n > 4:
        string1 = str(num).center(n, str(num))
        print("  " * num, string1, " " * num)
        bee(num + 1, n - 4)
    string2 = str(num).center(n, str(num))
    print("  " * num, string2, " " * num)

bee(1, 16)"""


"""def print_digits(number: int, step: int = 0):
    string_num = str(number)
    if step < len(string_num):
        print(string_num[step])
        print_digits(number, step + 1)



print_digits(12345)"""




"""def sum_to(n):
    if n == 0:
        return 0                       # базовый случай
    else:
        return n + sum_to(n - 1)


print(sum_to(5))"""


"""def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(12))"""


"""def sum_num(n):
    if n < 10:
        return 1
    else:
        return 1 + sum_num(n // 10)


n = int(input())
print(sum_num(n))"""


"""def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

n = int(input())
print(sum_of_digits(n))"""


#print(128 % 10 + 128 // 10)


"""def number_of_frogs(year, query=77):
    if year == 1:
        return query
    else:
        return number_of_frogs(year - 1, (query - 30) * 3)


print(number_of_frogs(3))"""


"""def range_sum(numbers: list, start, end):
    if numbers[start] == numbers[end]:
        return numbers[start]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
"""


"""def get_pow(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * get_pow(a, n - 1)


print(get_pow(2, 10))"""


"""def get_fast_pow(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return get_fast_pow(a * a, n / 2) if n % 10 == 0 else a * get_fast_pow(a, n - 1)


print(get_fast_pow(2, 10))"""



"""def recursive_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(0, 0))"""


"""def is_power(number):
    if number / 2 == 2 or number == 1:
        return True
    elif number % 2 != 0:
        return False
    else:
        return is_power(number / 2)


print(is_power(45))"""


"""import time
start = time.time()
def tribonacci(n):
    if n <= 3:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(100))

stop = time.time()
print(stop - start)"""



"""cache = {1: 1, 2: 1}                # ключ - номер числа, значение - число Фибоначчи

def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n-1)
        cache[n] = result
    return result


print(tribonacci(7))"""


"""cache = {1: 1, 2: 1, 3: 1}                # ключ - номер числа, значение - число Фибоначчи

def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
        cache[n] = result
    return result


print(tribonacci(7))"""


"""def is_palindrome(string: str, start=0, stop=-1):
    flag = 1
    if string[start] == string[stop]:
        flag += 1
    elif string[start] != string[stop]:
        return False
    elif flag < 0:
        return True
    try:
        return is_palindrome(string, start + 1, stop - 1)
    except IndexError:
        return True


print(is_palindrome('abaa'))"""


"""def is_palindrome(string: str, start=0, stop=-1):
    if string == '':
        return True
    elif string[start] == string[stop]:
        pass
    elif string[start] != string[stop]:
        return False
    try:
        return is_palindrome(string, start + 1, stop - 1)
    except IndexError:
        return True


print(is_palindrome('abba')):"""


"""def to_binary(number) -> str:
    z = []
    if number == 0:
        z.append('1')
    elif number == 1:
        z.append('1')
    else:
        return to_binary(number // 2)
    return str(z)


print(to_binary(123))"""


"""print(123 // 2, 123 % 2)"""


"""def to_binary(number, z=""):
    if number == 0:
        z += "0"
    elif number == 1:
        z += "1"
    else:
        return to_binary(number // 2, z + str(number % 2))
    return z[::-1]

print(to_binary(1))"""


"""def to_binary(number):
    if number <= 1:
        return str(number)
    return to_binary(number // 2) + str(number % 2)


print(to_binary(123))"""


"""def reverse_num(n):
    if n > 0:
        print(n)
        reverse_num(n - 5)
    print(n)



x = int(input())
reverse_num(x)"""


# реализовать с помощью вложенной функции
"""def recursive_sum(nested_lists):
    total = 0
    if nested_lists == [] or nested_lists == 0:
        return 0
    for i in nested_lists:
        if type(i) == int:
            total += i
        elif type(i) == list:
            total += recursive_sum(i)
    return total"""


"""def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for i in nested_dicts.values():
        if type(i) == dict:
            value = get_value(i, key)
            if value is not None:
                return value


data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetAddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'},
                    'postalCode': '125315'}}
print(get_value(data, 'cityName'))"""


"""def get_all_values(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for i in nested_dicts.values():
        if type(i) == dict:
            value = get_all_values(i, key)
            if value is not None:
                return value


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print((result))"""


"""# print([chr(i) for i in range(97, 123)])

for i in range(97, 123):
    print(chr(i))"""


"""def convert(number):
    return (bin(number).replace('0b', ''), oct(number).replace('0o', ''), hex(number).replace('0x', '').upper())

print(convert(-132))
"""


"""films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

min_grade = 10
film = ''
for x in films:
    if sum(films[x].values()) / 2 < min_grade:
        min_grade = sum(films[x].values()) / 2
        film = x
print(film)"""

"""result = min(films, key=lambda x: sum(films[x].values()))
print(result)"""


"""def non_negative_even(numbers: list):
    return all(x % 2 == 0 and x >= 0 for x in numbers)

print(non_negative_even([0, 2, 4, 8, 16]))"""


"""def is_greater(lists, number):
    return any(sum(x) > number for x in lists)



data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

print(is_greater(data, 2))"""


"""def custom_isinstance(objects, typeinfo):
    result = [x for x in objects if isinstance(x, typeinfo)]
    return len(result)



numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))"""


"""numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]

result = [x[0] for x in enumerate(numbers, 0) if x[-1] == max(numbers)]
print(*result)"""




"""def my_pow(number):
    result = sum([pow(int(x[-1]), int(x[0])) for x in enumerate(str(number), 1)])
    return result


print(my_pow(303))"""


"""def my_pow(number):
    char_num = str(number)
    sum_nums = 0
    for i in enumerate(char_num, 1):
        sum_nums += pow(int(i[-1]), int(i[0]))
    return sum_nums


print(my_pow(303))"""


"""names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]


result = [f'{x[0]}: {x[-1] - x[1]}$' for x in zip(names, budgets, box_offices)]

for i in sorted(result):
    print(i)"""


# Не решена
"""def zip_longest(*args, fill=None):
    z = []
    for i in zip(*args):
        z.append(i)
    lst_primer = []
    for l in z:
        for k in l:
            lst_primer.append(k)

    for j in args:
        for k in j:
            if k not in lst_primer:
                char_k = [k, fill]
                z.append(tuple(char_k))
                #z.append(tuple(f'{k}{fill}'))

    print(z)


data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))"""



"""def hash_as_key(objects):
    hash_objects = []
    for i in objects:
        hash_objects.append(hash(i))
    res_dict = {}
    for j in objects:
        if hash(j) in hash_objects:
            res_dict.setdefault(hash(j), [j, hash(j)] if j == -1 else j)

    return res_dict

data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))"""


"""data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]

result = filter(lambda x: x if type(x) == int or type(x) == float else False, data)
res = map(lambda x: str(x).split('.')[0], result)
for i in res:
    print(i)"""


"""numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

result = filter(lambda x: x if len(str(abs(x))) == 2 and x % 9 == 0 else False, numbers)
print(sum(map(lambda x: x**2, result)))"""


"""names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']

result = filter(lambda x: x if len(x) > 4 and x[0].lower() == 'а' or x[0].lower() == 'м' and len(x) > 4 else False, names)
print(*sorted(map(lambda x: x.capitalize(), result)))"""


"""fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)

print(fib(2))"""



"""def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(operation(i, j), end=' ')
        print()


print_operation_table(pow, 5, 4)"""




"""# login - логин пользователя
# password - пароль пользователя
# success - некоторая функция
# failure - некоторая функция
def verification(login, password, success, failure):
    text = {1: 'в пароле нет ни одной буквы', 2: 'в пароле нет ни одной заглавной буквы',
            3: 'в пароле нет ни одной строчной буквы', 4: 'в пароле нет ни одной цифры'}

    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if any([x in abc_upper for x in password]) and any([x in abc_lower for x in password]) and any([x.isdigit() for x in password]):
        return success(login)
    else:

        if not any([x in abc for x in password]):
            return failure(login, text[1])

        elif not any([x in abc_upper for x in password]):
            return failure(login, text[2])

        elif not any([x in abc_lower for x in password]):
            return failure(login, text[3])

        elif not any([x.isdigit for x in password]):
            return failure(login, text[4])

def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)"""


"""def numbers_sum(elems):
    #Принимает список и возвращает сумму его чисел (int, float),
    #игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    return sum([x if type(x) == int or type(x) == float else 0 for x in elems])


print(numbers_sum.__doc__)
print(numbers_sum([1, '2', 3, 4, 'five']))"""

"""
old_print = print
def up_print(*args, **kwargs):
    result = map(lambda x: x.upper() if type(x) == str else x, args)
    if kwargs == {}:
        old_print(*result)
    else:
        old_print(*result, sep=kwargs['sep'].upper(), end=kwargs['end'].upper())

print = up_print

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')"""


"""def primer():
    primer.name = 'Ruslan'


print(primer.__dict__)

primer.value = '178 sm'
primer.age = '18 let'

primer()

print(primer.__dict__)"""


"""def polynom(x: float):
    polynom.__dict__['values'] = set()
    return x**2 + 1



print(polynom(5))
print(polynom.values)"""


"""def num(n):
    def mult(x):
        return n * x
    return mult


res = num(5)
print(res(3))"""


"""def outer_function(arg):
    num = 5
    name = 'Timur'
    numbers = [1, 2, 3]

    def inner_function():  # определяем вложенную функцию
        print(arg)
        print(num)
        print(numbers)

    return inner_function  # возвращаем вложенную функцию


inner = outer_function('python')

for var in inner.__closure__:
    print(var.cell_contents)"""


"""def trans(word):
    alphabet = {"q": 'й', "w": 'ц', "e": 'у', "r": 'к', "t": 'е', "y": 'н', "u": 'г', "i": 'ш',
                "o": 'щ', "p": 'з', "[": 'х', "]": 'ъ', "a": 'ф', "s": 'ы', "d": 'в', "f": 'а',
                "g": 'п', "h": 'р', "j": 'о', "k": 'л', "l": 'д', ";": 'ж', "'": 'э',
                "z": 'я', "x": 'ч', "c": 'с', "v": 'м', "b": 'и', "n": 'т', "m": 'ь', ",": 'б', ".": 'ю', ' ': ' '}

    z = []
    for i in word:
        z.append(alphabet[i])

    return ''.join(z)



print(trans('cerf t,tyfz'))"""


"""def power(degree):
    def sqr(x):
        return x**degree
    return sqr


result = power(4)(2)
print(result)"""


"""def generator_square_polynom(a, b, c):
    def result(x):
        return a*x**2 + b * x + c
    return result


f = generator_square_polynom(26, 83, 22)
print(f(55))"""


"""def sourcetemplate(url):
    def address(**kwargs):
        if not kwargs:  # проверка на наличие именнованых элементов
            return url
        z = []
        for i in kwargs:  # преобразование именнованых элементов в строку и добавление в список z
            text = [i, "=", kwargs[i]]
            text_obr = [str(x) for x in text]
            res = ''.join(text_obr)
            z.append(res)
        if len(z) >= 2:   # если в z есть больше чем один именнованый аргумент, то добавляем разделитель &
            result = '&'.join(sorted(z))
            return f'{url}?' + result
        else:
            result = ''.join(sorted(z))   # иначе просто возвращаем список преобразованный в строку с одни именнованым аргументом
            return f'{url}?' + result
    return address


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))"""


"""
from datetime import date

def date_formatter(country_code):
    def loc_time(date):
        if country_code == 'ru':
            return date.strftime('%d.%m.%Y')
        elif country_code == 'us':
            return date.strftime('%m-%d-%Y')
        elif country_code == 'ca':
            return date.strftime('%Y-%m-%d')
        elif country_code == 'br':
            return date.strftime('%d/%m/%Y')
        elif country_code == 'fr':
            return date.strftime('%d.%m.%Y')
        elif country_code == 'pt':
            return date.strftime('%d-%m-%Y')
    return loc_time


date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))"""


"""def get_digits(number: int | float) -> list[int]:
    result = [int(x) for x in str(number) if x.isdigit()]
    return result



print(get_digits(-16733))"""


"""def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    z = dict()
    for i in grades:
        if i == "name":
            z.update({i: grades[i]})
        elif i == "grades":
            z.update({"top_grade": max(grades[i])})
    return z




print(*top_grade.__annotations__.values())
"""


"""def cyclic_shift(numbers: list[int | float], step: int) -> list[int]:
    return numbers[step]

# сделать по принципу от -2 до 2
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)"""



"""def decorator_line(func):
    def wrapper(*args, **kwargs):
        line_break = '-' * 15
        result = func(*args, **kwargs)
        return line_break + '\n' + result + '\n' + line_break
    return wrapper


@decorator_line
def say(name):
    return f'Hello {name}'


print(say('Oleg'))"""


"""def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = str(func(*args, **kwargs))
        print('---- Нижний ломтик хлеба ----')
        return result
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])"""


"""def decorator_print(func):
    def behavior(*args, **kwargs):
        new_args = (str(x).upper() for x in args)
        new_kwargs = {i: j.upper() for i, j in kwargs.items()}
        result = func(*new_args, **new_kwargs)
        return result
    return behavior


print = decorator_print(print)

print(111, 222, 333, sep='xxx')"""


"""def do_twice(func):
    def behavior(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return behavior


@do_twice
def beegeek(a, b, sep):
    print(a + b + sep)


beegeek(1, 2, sep=10)"""


"""def reverse_args(func):
    def behavior(*args, **kwargs):
        rever_args = reversed(args)
        result = func(*rever_args, **kwargs)
        return result
    return behavior


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))"""


"""def exception_decorator(func):
    def behavior(*args, **kwargs):
        try:
            func(*args, **kwargs)
            value = func(*args, **kwargs)
            return (value, 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')
    return behavior


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))"""


"""
def takes_positive(func):
    def behavior(*args, **kwargs):
        for i in args:
            if type(i) != int:
                raise TypeError
            elif i <= 0:
                raise ValueError
        for i, j in kwargs.items():
            if type(j) != int:
                raise TypeError
            elif j <= 0:
                raise ValueError
        result = func(*args, **kwargs)
        return result
    return behavior


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))"""

"""import time

def nice_print(text: str):
    for i in text:
        time.sleep(0.06)
        print(i, end='')



nice_print('Hello motherfucker. If u want to do some decorator, you are the best!')"""

"""import functools

def square(func):
    @functools.wraps(func)
    def behavior(*args, **kwargs):
        func_number = func(*args, **kwargs)
        return func_number**2
    return behavior


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)"""


"""import functools

def returns_string(func):
    @functools.wraps(func)
    def behavior(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            return result
        else:
            raise TypeError
    return behavior


@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))"""

"""import functools

def trace(func):
    @functools.wraps(func)
    def behavior(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        if type(func(*args, **kwargs)) == str:
            print(f"TRACE: возвращаемое значение {func.__name__}(): '{result}'")
        else:
            print(f"TRACE: возвращаемое значение {func.__name__}(): {result}")
        return result
    return behavior


@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)"""


"""import functools

def prefix(string, to_the_end=False):
    def decorator_prefix(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if to_the_end:
                return value + string
            else:
                return string + value
        return wrapper
    return decorator_prefix


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())"""

"""import functools

def make_html(tag):
    def dec_make_html(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return f'<{tag}>{value}</{tag}>'
        return wrapper
    return dec_make_html


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))"""

"""import functools

def repeat(times):
    def dec_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return dec_repeat


@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')


print(say_beegeek.__name__)
print(say_beegeek.__doc__)"""


"""import functools

def strip_range(start, end, char='.'):
    def dec_strip_range(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            z = []
            for i in value:
                z.append(i)
            for j in range(start, end):
                try:
                    z[j] = char
                except IndexError:
                    break
            return ''.join(z)
        return wrapper
    return dec_strip_range


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())"""


"""import functools

def returns(datatype):
    def dec_returns(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if datatype == type(value):
                return value
            else:
                raise TypeError
        return wrapper
    return dec_returns


@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))"""


"""import functools

def takes(*type_args):
    def dec_takes(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            for i in args:
                if type(i) not in type_args:
                    raise TypeError
            for j in kwargs.values():
                if type(j) not in type_args:
                    raise TypeError
            return value
        return wrapper
    return dec_takes


@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))"""


"""import functools

def add_attrs(**atr_kwargs):
    def dec_add_atrs(func):
        for i in atr_kwargs:
            func.__dict__[i] = atr_kwargs[i]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        return wrapper
    return dec_add_atrs


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)"""


"""import functools

def ignore_exception(*type_args):
    def dec_ignore_exception(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            list_exceptions = [x.__name__ for x in type_args]
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as e:
                error_name = type(e).__name__
                if error_name in list_exceptions:
                    print(f'Исключение {error_name} обработано')
                else:
                    raise type(e)
        return wrapper
    return dec_ignore_exception

# Решить проблему с тем почему выводит class TypeError, хотя должен ValueError

@ignore_exception()
def func():
    '''func docs'''
    raise ValueError


try:
    func()
except Exception as e:
    print(type(e))"""


"""import functools

class MaxRetriesException(Exception):
    pass

def retry(times):
    def dec_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return dec_retry


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()"""


"""def simple_sequence():
    num = 1
    i = 0
    while True:
        if i != num:
            i += 1
            yield num
        else:
            i = 0
            num += 1

generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)"""


"""def alternating_sequence(count=None):
    num = 1
    while True:
        if count is None:
            yield -num if num % 2 == 0 else num
            num += 1
        else:
            if num == count + 1:
                break
            else:
                yield -num if num % 2 == 0 else num
                num += 1



generator = alternating_sequence(10)

print(*generator)"""


"""def primes(left, right):
    for i in range(left, right + 1):
        if i == 1:
            continue
        z = []
        for x in range(2, i - 1):
            z.append(i % x)
        if all(z):
            yield i



generator = primes(6, 36)

print(next(generator))
print(next(generator))"""


"""def reverse(sequence):
    res = sequence[::-1]
    for i in res:
        yield i


print(*reverse([1, 2, 3, 4, 5]))"""

from datetime import date, timedelta

def dates(start, count=None):
    index = 0
    """if start > datetime.date(9999, 12, 31):
        raise StopIteration"""
    while True:
        try:
            if count is None:
                yield start
                start += timedelta(days=1)

            else:
                if index == count:
                    break
                else:
                    yield start
                    start += timedelta(days=1)
                    index += 1
        except OverflowError:
            break

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')
