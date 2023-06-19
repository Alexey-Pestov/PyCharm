# from tkinter import *
#
# window = Tk()
# window.title('Форточка')
# window.geometry('500x500+200+200')
#
# count = 0
#
# def change_count():
#     global count
#     count += 1
#     lab['text'] = count
#
# lab = Label(window, text='В форточку дуло', bg='red', fg='yellow')
# lab.place(x=100, y=100)
#
# btn = Button(text='Нажми',  bg='red', fg='yellow', font='16',command=change_count)
# btn.place(x=200, y=200)
#
# window.mainloop()

from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.title('Курс валют')
window.geometry('500x500')
# window.configure(bg='pink')
canvas = Canvas(window, width=500, height=500, bg='pink', highlightthickness=0)
canvas.place(in_=window,x=0,y=0)

today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req' : today}

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params=payload)
xml = BeautifulSoup(responce.content, features="xml")

def get_course(id):
    return  xml.find('Valute', {'ID':id}).Value.text

img = PhotoImage(file='logo.png')
canvas.create_image(75,75, image = img)
# logo = Label(window, image=img, bg='pink')
# logo.place(x=0,y=0)

canvas.create_text(300, 70, text="Курс валют", font='Arial 32')
# lab = Label(window, text="Курс валют", font='Arial 32')
# lab.place(x=200,y=50)

canvas.create_text(300, 110, text = 'на ' + today.replace('/','.'), font='Arial 16')
# course_info = Label(window, text = 'на ' + today.replace('/','.'), font = 'Arial 16')
# course_info.place(x=250, y=100)

# usd_course = Label(window,text = "$ " + get_course('R01235'), font = 'Arial 20')
# usd_course.place(x=100, y=190)
# euro_course = Label(window,text = "€ " + get_course('R01239'), font = 'Arial 20')
# euro_course.place(x=100, y=240)
canvas.create_text(250, 230, text = f'$ {get_course("R01235")[:5]}', fill='red', font=('Arial', 32, 'bold'))
canvas.create_text(250, 300, text = '€ ' + str(round(float(get_course("R01239").replace(',' , '.')),2)).replace('.' , ','), fill='red', font=('Arial', 32, 'bold'))

window.mainloop()