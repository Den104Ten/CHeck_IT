# Счетчик времени доставки

"""N = int(input())
M = int(input())
T = int(input())

N = N * 60  # часы переводим в минуты
Time = N + M  # время в минутах когда был сделан заказ
Time_2 = Time + T  # время в минутах через сколько будет привезен заказ

i = 1
d = 0


for i in range(Time_2):
    if Time_2 % 60 == 0:
        if d > 9:
            print(f'{Time_2 // 60}:{d}')
            break
        elif d < 9:
            print(f'{Time_2 // 60}:0{d}')
            break
    else:
        Time_2 = Time_2 - 1
        d += 1"""


# Камень ножницы и бумага
import random

a = 'Камень', 'Ножницы', 'Бумага'
role = random.choice(a).lower()  # Рандом - выводит рандомную строку


choice = str(input("Камень, ножницы или бумага?: ").lower())  # Пользователь выбирает предмет

if choice == role:
    print(f"Компьютер тоже выбрал: {role.title()}. Переигровка!")  # Одинаковые предметы. Переигровка!


# Варианты выигрыша

elif choice == 'Камень'.lower() and role == 'Ножницы'.lower():  # Победа при камне и ножницах у пк
    print(f"Компьютер выбрал: {role.title()}. Вы победили!")

elif choice == 'Ножницы'.lower() and role == 'Бумага'.lower():  # Победа при ножницах и бумаге у пк
    print(f"Компьютер выбрал: {role.title()}. Вы победили!")

elif choice == 'Бумага'.lower() and role == 'Камень'.lower():  # Победа при бумаге и камне у пк
    print(f"Компьютер выбрал: {role.title()}. Вы победили!")


# Варианты проигрыша

elif choice == 'Ножницы'.lower() and role == 'Камень'.lower():  # Проигрыш при ножницах и камне у пк
    print(f"Компьютер выбрал: {role.title()}. Вы проиграли!")

elif choice == 'Бумага'.lower() and role == 'Ножницы'.lower():  # Проигрыш при бумаге и ножницах у пк
    print(f"Компьютер выбрал: {role.title()}. Вы проиграли!")

elif choice == 'Камень'.lower() and role == 'Бумага'.lower():  # Проигрыш при камне и бумаге у пк
    print(f"Компьютер выбрал: {role.title()}. Вы проиграли!")




