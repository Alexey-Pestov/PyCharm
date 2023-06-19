import random
from tkinter import *

window = Tk()
w, h = 600, 600
window.geometry(str(w)+'x'+str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window,x=0,y=0)
bg_photo = PhotoImage(file='bg_2.png')
# canvas.label = Label()

class Knight:
    def __init__(self):
        self.x = 70
        self.y = h//2
        self.v = 0
        self.photo = PhotoImage(file='knight.png')

    def up(self, event):
        self.v = -3
    def down(self, event):
        self.v = 3
    def stop(self, event):
        self.v = 0

class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100,500)
        self.v = random.randint(1,3)
        self.photo = PhotoImage(file='dragon.png')

knight = Knight()
dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete('all') # полностью очищаем холст
    canvas.create_image(300,300, image = bg_photo) # вводятся координаты центра картинки
    knight.y += knight.v
    canvas.create_image(knight.x, knight.y, image = knight.photo)

    curremt_dragon = 0
    dragons_to_kill = -1
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)

        if ((dragon.x - knight.x)**2 + (dragon.y - knight.y)**2) <= 96**2: # 2 * 110**2:
            dragons_to_kill = curremt_dragon

        # canvas.label.config(text=f'привет, {dragon.x}, {dragon.y}, {knight.x}, {knight.y}')
        # canvas.label.update()

        curremt_dragon += 1
        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w // 2, h // 2, text='LOSE', font='Verdana 42', fill='red')
            break
    if dragons_to_kill >= 0:
        del dragons[dragons_to_kill]

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text = 'WIN', font= 'Verdana 42', fill = 'red')
    else:
        window.after(10, game)


game()

# canvas.label.pack()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.mainloop()