


"""numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
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


#with open('input.txt', encoding='utf-8') as file:
"""    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')"""


#with open('text.txt', 'r') as file:
""""    for i in file:
        z = (i.split())
    z.reverse()
    c = []
    for j in z:
        c.append(j[::-1])
    print(*c)"""


#with open('data.txt', 'r') as file:
"""z = []
    for i in file:
        z.append(i.strip())
    z.reverse()
    print(*z, sep='\n')"""


#with open('lines(1).txt', 'r') as file:
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


#with open('numbers.txt', 'r') as file:
"""z = []
    for i in file:
        z.append(i.strip().split())
    for j in z:
        a = list(map(int, j))
        print(sum(a))"""
            

#with open('file.txt', 'r') as file:
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



#with open('population.txt', 'r') as file:
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


mail_sum = int(input())

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

print(mail_lst)