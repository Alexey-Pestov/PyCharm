import random
import datetime
from tkinter import *
from pygame import mixer

mixer.init()
window = Tk()
w, h = 600, 600
window.geometry(str(w)+'x'+str(h))
window.title('Dragon`s war')

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window,x=0,y=0)
bg_photo = PhotoImage(file='bg_2.png')
lose = PhotoImage(file='Lose_2.png')
win = PhotoImage(file='Win.png')

canvas.label_KD = Label()


def play_sound(sound, channel): # функция для многоканального звука
    mixer.Channel(channel).play(mixer.Sound(sound))

class Knight: # класс Рыцаря
    def __init__(self):
        self.alive = 1
        self.x = 55
        self.y = h//2
        self.v = 0
        self.vy = 0
        self.photo = PhotoImage(file='knight.png')
        self.photo = self.photo.zoom(10,10)
        self.photo = self.photo.subsample(13,13)

    def up(self, event):
        if knight.y < 60:
            self.y = 60 # реализовано через фиксацию координат при достижении границы экрана. Альтернативный вариант: обнуление скорости глючит при зажатии клавиш управления
        else:
            self.vy = -1

    def down(self, event):
        if knight.y > 540:
            self.y = 540
        else:
            self.vy = 1

    def stop(self, event):
        self.vy = 0

class Dragon: # класс Дракона
    def __init__(self, y):
        self.x = 550
        self.f_x = self.x - 110
        self.y = y
        self.f_y = self.y - 15
        self.v = random.randint(1,3) # переменная для скорости огонька
        self.vy = 0
        while self.vy == 0: # задаем скорость смещения дракона по вертикали
            self.vy = random.randint(-3,3)
        self.y_2 = self.y # запоминаем начальное положение
        self.photo = PhotoImage(file='dragon.png')
        self.photo_fire = PhotoImage(file='fire_dragon.png')

class Spear: # класс Копья
    def __init__(self):
        self.x = knight.x
        self.y = knight.y
        self.v = 4
        self.photo = PhotoImage(file='spear.png')

t2 = 0 # время последнего выстрела

def create_spear(event): # функция порождения копья (стрельба ЛКМ)
    global t2
    time = datetime.datetime.now()
    if t2 == 0 or (time-t2).total_seconds()>5:
        t2 = time
        spear = Spear()
        spears.append(spear)
        play_sound('shot.mp3', 1)
    else:
        pass
    canvas.label_KD.pack(anchor='n')

spears = []
dragons = []
knight = Knight()

for i in range(3): # создаем 3 драконов c шагом в 150 пикселей
    dragon = Dragon(150*(i+1))
    dragons.append(dragon)

def kill_spear(spear_to_kill): # функция уничтожения копья, если не попало
    del spears[spear_to_kill]

def kill_dragon(i): # функция уничтожения дракона
    play_sound('dragon_death.mp3', 2)
    del dragons[i]

def game():
    canvas.delete('all') # полностью очищаем холст
    canvas.create_image(300,300, image = bg_photo) # вводятся координаты центра картинки
    canvas.create_image(knight.x, knight.y, image = knight.photo)

    for spear in spears: # перерисовываем копья
        spear.x += spear.v
        canvas.create_image(spear.x, spear.y, image=spear.photo)
        if spear.x > 600-37:
            kill_spear(0)

    knight.y += knight.vy # смещаем рыцаря

    for i, dragon in enumerate(dragons): # смещаем огоньки и двигаем туда-обратно по вертикали драконов
        dragon.f_x -= dragon.v
        dragon.y += dragon.vy
        if abs(dragon.y - dragon.y_2) > 100:
            dragon.vy = - dragon.vy
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)
        canvas.create_image(dragon.f_x, dragon.f_y, image=dragon.photo_fire)

        if (dragon.f_x < 145 and abs(dragon.f_y - knight.y) < 51): # проверка на убийство рыцаря огоньком
            knight.alive = 0

        if dragon.f_x <= 0: # проверяем, не улетел ли огонек за экран, возвращаем
            dragon.f_x = dragon.x - 110
            dragon.f_y = dragon.y-15
            if dragon.f_x == dragon.x - 110:
                play_sound('fire.mp3', 4)
            dragon.v = random.randint(1, 3)

        for j, spear in enumerate(spears): # проверяем на убийство дракона копьем
            if (spear.x > 600 - 137 and abs(dragon.y -spear.y) < 51):
                kill_dragon(i)
                kill_spear(j)

    if t2 != 0:
        delta_KD = 5-(datetime.datetime.now() - t2).total_seconds()
        if delta_KD < 0:
            delta_KD = 0
        canvas.label_KD.config(text=f'Достаю новое копье еще {delta_KD:.1f} сек.',font='Arial 22 bold', bg='#4c226c', fg='white')

    if knight.alive == 0: # если рыцарь того, то игра тоже того
        play_sound('knight_death_2.mp3', 6)
        canvas.delete('all')
        canvas.label_KD.destroy()
        canvas.create_image(300, 300, image=lose)
        dragons.clear()
        spears.clear()
    elif len(dragons) == 0 and knight.alive != 0: # если все драконы убиты, а рыцарь не того, то мы красавчики
        play_sound('Victory.mp3', 5)
        canvas.delete('all')
        canvas.label_KD.destroy()
        canvas.create_image(300, 300, image=win)
    else: # продолжаем
        window.after(10, game)

game()

play_sound('nas_atakuyut_2.mp3', 0)

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<Button-1>', create_spear)
window.mainloop()