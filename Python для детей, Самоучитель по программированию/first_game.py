'''Игра угадайка'''

import random

num = random.randint(0, 100)
while True:
    i = int(input('Введите число: '))
    if i == num:
        print('Правильный ответ!')
        break
    elif i < num:
        print('Загаданное число больше. Ваше число: %s' % i)
    else:
        print('Загаданное число меньше. Ваше число: %s'% i)
    
