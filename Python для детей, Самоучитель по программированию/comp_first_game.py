'''Игра угадайка, 40'''

import time
import random

min = 0
max = 1_000_000_000
caunt = 0
num = random.randint(min, max)
timeSleep = 0

print('Сейчас компьютер попытается угадать чилсо сам у себя')
time.sleep(timeSleep)
while True:
    print('Крутим рулетку')
    time.sleep(timeSleep)
    i = random.randint(min, max)
    if i == num:
        print('Правильный ответ! Ваше число: %s' % i)
        break
    elif i < num:
        print('Загаданное число больше. Ваше число: %s' % i)
        min = i + 1
        time.sleep(timeSleep)
    else:
        print('Загаданное число меньше. Ваше число: %s'% i)
        max = i - 1
        time.sleep(timeSleep)
    caunt += 1
print(caunt)
