def hello():
    print('Привет')

def random_rectangle(width: int, height: int, '''fill_collor'''):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    '''canvas.create_rectangle(x1, y1, x2, y2, fill = fill_collor)'''

from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
'''canvas.create_line(0, 0, 500, 500)
btn = Button(tk, text = 'Нажми меня', command = hello)
btn.pack()'''

for x in range(0, 100):
    random_rectangle(400, 400)

