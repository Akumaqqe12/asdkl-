import tkinter as tk
import random

COLOR_1 = '#FFF00'
COLOR_2 = 'C0C0C0'

def click():
    global score
    button.configure(text = 'взять Карту')
    while True:
        random_key = random.choice(list(card_list.keys()))
        texts.append(random_key)
        score += (card_list[random_key])
        break
    print(texts)
    label_spis.configure(text = texts)
    label_score.configure(text = score)
def deleted():
    global score
    texts.clear()
    label_spis.configure(text = 'У вас нет карт')
    score = 0
    label_score.configure(text = 0)
win = tk.Tk()

win.geometry('400x600')
win.resizable(0,0)

card_list = {"туз": 11, "десять": 10,"кароль": 4,"дама": 3,"валет": 2,"девять": 9,"восемь": 8,"семь": 7,"шесть": 6,}

score = 0

texts = []

button = tk.Button(bg = COLOR_1, fg = COLOR_2,font = ('Franklin Gothic',12), text = "Взять Карту/ Начать игру", command=lambda: click())
button.place(x = 77,y= 65, width = 230, height= 80)

button_2 = tk.Button(bg = COLOR_1, fg = COLOR_2,font = ('Franklin Gothic',12),text = 'Сбросить руку',command=lambda: deleted())
button_2.place(x = 77,y= 165, width = 230, height= 80)


label = tk.Label(text='Список карт:', fg = COLOR_1, font = ('Franklin Gothic',15))
label.place(x=80,y=250)

label_spis = tk.Label(text= texts, fg = COLOR_1, font = ('Franklin Gothic',10))
label_spis.place(x=85,y=275)

label_score_sum = tk.Label(text='Сумма очков:', fg = COLOR_1, font = ('Franklin Gothic',15))
label_score_sum.place(x=60,y=300)

label_score = tk.Label(text= score, fg = COLOR_1, font = ('Franklin Gothic',10))
label_score.place(x=75,y=327)

win.mainloop()