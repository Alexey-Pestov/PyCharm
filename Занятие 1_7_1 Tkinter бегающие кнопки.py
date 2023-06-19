from tkinter import *
import random
import time

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points1 = 0
points2 = 0

def check1():
    global points1
    global points2
    b1.place(x = random.randint(1,550), y = random.randint(1,350))
    points1 += 1
    label['text'] = 'Счет первой кнопки ' + str(points1) + ' , счет второй кнопки ' + str(points2)
    if points1 == 10 and points2 == 0:
        b2.configure(text = 'Ну пожалуйста :(')

def check2():
    global points1
    global points2
    b2.place(x = random.randint(1,550), y = random.randint(1,350))
    points2 += 1
    label['text'] = 'Счет первой кнопки ' + str(points1) + ' , счет второй кнопки ' + str(points2)
    if points2 == 10 and points1 == 0:
        b1.configure(text = 'Ну пожалуйста :(')

b1 = Button(text = 'Нажми меня', font= ('Arial', 20), fg = 'black', command=check1)
b1.place(x = 150, y = 150)

b2 = Button(text = 'Нажми меня', font= ('Arial', 20), fg = 'black', command=check2)
b2.place(x = 350, y = 70)

label = Label(text = 'Счет первой кнопки ' + str(points1) + ' , счет второй кнопки ' + str(points2), font= ('Arial', 16), fg = 'red')
label.place(x = 10, y = 10)

window.mainloop()