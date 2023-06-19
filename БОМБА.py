from tkinter import *
import random
import time

window = Tk()
window.geometry('700x500')
window.config(bg = 'black')
window.title('БОМБА')

points = 0

def check1():
    global points

    b1.place(x = random.randint(1,600), y = random.randint(200,400))
    points += 1
    time2 = time.perf_counter()
    label2['text'] = str(points)
    label3['text'] = 'Осталось ' + str(round(10 - (time2 - time1), 2))+ ' секунд!!!'
    if 10 - (time2 - time1) < 0:
        label4 = Label(text='БАМ !!!!!', font=('Courier New', 40), fg='white', bg='black')
        label4.place(x=1, y=1, width=700, height=500)
    elif points == 15:
        label4 = Label(text='ВАМ ПОВЕЗЛО !!!!!', font=('Courier New', 40), fg='white', bg='black')
        label4.place(x=1, y=1, width=700, height=500)

b1 = Button(text = 'Нажми меня', font= ('Arial', 20), bg = 'grey', fg = 'white', command=check1)
b1.place(x = 250, y = 300)

label = Label(text = 'У вас 10 секунд, чтобы нажать на кнопку 15 раз', font= ('Courier New', 18), fg = 'green', bg = 'black')
label.place(x = 20, y = 10)

time1 = time.perf_counter() # программа и функция работают с переменными time1 и time2 без обозначения их глобальными
time2 = time1

label2 = Label(text = str(points), font= ('Courier New', 40), fg = 'white', bg = 'black')
label2.place(x = 320, y = 50)

label3 = Label(text = 'Осталось ' + str(10 - (time2 - time1))+ ' секунд!!!', font= ('Courier New', 30), fg = 'red', bg = 'black')
label3.place(x = 60, y = 120)

window.mainloop()