from tkinter import *
import requests
from bs4 import BeautifulSoup
import re
import random
from PIL import ImageTk, Image  # https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window?answertab=createdasc#tab-top


window = Tk()
# canvas = Canvas(window, width=700, height=650, highlightthickness=0)
# canvas.pack()
window.geometry('700x650')

def animals():
  responce = requests.get('https://bipbap.ru/jivotnie/samye-krasivye-i-milye-zhivotnye-100-foto.html')
  responce = responce.content
  html = BeautifulSoup(responce, 'lxml')
  subtitle = html.find_all(src = re.compile('zhivotnie-zhivotnie-krasivo-foto')) # источник: https://docs-python.ru/packages/paket-beautifulsoup4-python/metody-find-all/

  A = [] # формируем список с ссылками на все картинки
  for element in subtitle:
    A.append(element['src'])

  image = A[random.randint(0, len(A)-1)] # выбираем случайную
  image = requests.get(image, stream=True).raw # преобразование ссылки, взято из https://python-scripts.com/pillow

  clear()
  pic_happy = Image.open(image)
  pic_happy = ImageTk.PhotoImage(pic_happy)
  label_happy = Label(window, image=pic_happy)
  label_happy.image = pic_happy
  label_happy.place(x=0, y=0,  height=500)

def draw_menu():
    clear()
    label_title = Label(text='Что 6ы вы хотели сделать?', font=('Arial', 24), fg='white', bg='orange')
    label_title.place(width=700, height=50, x=0, y=0)

    b_1 = Button(text='Узнать что-то новое', font=('Arial', 18), fg='black', command=clear)
    b_1.place(x=25, y=75, width=300)

    b_2 = Button(text='Посмотреть на котиков', font=('Arial', 18), fg='black', command=animals)
    b_2.place(x=375, y=75, width=300)

def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l. destroy()
    draw_home_button()

def draw_home_button():
    our_button = PhotoImage(file="Back-Button-Transparent.png")
    # our_button = Image.open('back_icon.png')
    # our_button = ImageTk.PhotoImage(our_button)
    our_button = our_button.subsample(4,4)

    #b = Button(window, text='Домой', font=('Arial', 24), fg='black', command=draw_menu)
    b = Button(highlightthickness=0, font=('Arial', 24), fg='black', command=lambda : print('111'))
    b.configure(image=our_button)
    b.configure(text='111')
    b.place(x=25, y=550)

draw_menu()
window.mainloop()