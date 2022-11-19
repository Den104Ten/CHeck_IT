N = int(input())
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
        d += 1
