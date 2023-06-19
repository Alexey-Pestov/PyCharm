from tkinter import  *
from for_game import Hero
from for_game import Monster

def pos(player, monster):
    if player.coord == monster.coord:
        player.lifes -= 1
        canva.delete('enemy')
        monster = Monster(canva)
        return monster
    else:
        return monster

def moveleft(event):
    hero.move('left')
    coords = canva.coords('Hero')
    #butnormal()
    canva.delete('Hero')
    canva.create_rectangle(coords[0]-20, coords[1], coords[2]-20, coords[3], fill='blue', tags='Hero')
    coords = canva.coords('Hero')
    print(coords)
    butnormal()
    if coords[0] == 0:
        butleft.config(state=DISABLED)
        butleft.unbind('<Button-1>')

def moveup(event):
    hero.move('up')
    coords = canva.coords('Hero')
    #butnormal()
    canva.delete('Hero')
    canva.create_rectangle(coords[0], coords[1]-20, coords[2], coords[3]-20, fill='blue', tags='Hero')
    coords = canva.coords('Hero')
    print(coords)
    butnormal()
    if coords[1] == 0:
        butup.config(state=DISABLED)
        butup.unbind('<Button-1>')

def moveright(event):
    hero.move('right')
    coords = canva.coords('Hero')
    #butnormal()
    canva.delete('Hero')
    canva.create_rectangle(coords[0]+20, coords[1], coords[2]+20, coords[3], fill='blue', tags='Hero')
    coords = canva.coords('Hero')
    print(coords)
    butnormal()
    if coords[2] == 200:
        butright.config(state=DISABLED)
        butright.unbind('<Button-1>')

def movedown(event):
    hero.move('down')
    coords = canva.coords('Hero')
    #butnormal()
    canva.delete('Hero')
    canva.create_rectangle(coords[0], coords[1]+20, coords[2], coords[3]+20, fill='blue', tags='Hero')
    coords = canva.coords('Hero')
    print(coords)
    butnormal()
    if coords[3] == 200:
        butdown.config(state=DISABLED)
        butdown.unbind('<Button-1>')

def butnormal():
    coords = canva.coords('Hero')
    print('проверка ',coords)
    if coords[0] != 0 and butleft['state'] == DISABLED:
        butleft.config(state=NORMAL)
        butleft.bind('<Button-1>', moveleft)
    if coords[1] != 0 and butup['state'] == DISABLED:
        butup.config(state=NORMAL)
        butup.bind('<Button-1>', moveup)
    if coords[2] != 200 and butright['state'] == DISABLED:
        butright.config(state=NORMAL)
        butright.bind('<Button-1>', moveright)
    if coords[3] != 200 and butdown['state'] == DISABLED:
        butdown.config(state=NORMAL)
        butdown.bind('<Button-1>', movedown)

    enemylist[0].move(hero.coord[0], hero.coord[1], canva)

    enemy = pos(hero, enemylist[0])
    enemylist.clear()
    enemylist.append(enemy)

    lbl.config(
        text='\nИгрок: {}  Жизни: {}  Местоположение: {}  Инвентарь: {}'.format(hero.name, hero.lifes, hero.coord,
                                                                                hero.loot))  # config обновляет аргументы

hero = Hero("Alex")

root = Tk() # можно написать и window()
root.title('Первая игра') # вводим заглавие окна
root.geometry('400x400')
canva = Canvas(root, width=200, height=200, bg='grey') # поле игры
canva.pack()
enemy = Monster(canva)
enemylist = [enemy]
for i in range(1, 10):
    canva.create_line(20*i,0,20*i,200, fill='white', width=2)
    canva.create_line(0, 20*i, 200, 20 * i, fill='white', width=2)

canva.create_rectangle(80,80,100,100, fill='blue', tags='Hero') # рисуем персонажа, присваиваем объекту тег Hero
coords = canva.coords('Hero')
print('начальные', coords)

lbl = Label(root, text='\nИгрок: {} Жизни: {} Местоположение: {} Инвентарь: {}'.format(hero.name, hero.lifes, hero.coord, hero.loot))
lbl.pack()

butleft = Button(root, text='Влево') # создаем экземпляр от общего класса кнопок
butleft.pack() # вторая строка для кнопки, которая выводит ее на экран
butleft.bind('<Button-1>', moveleft)

butright = Button(root, text='Вправо')
butright.pack()
butright.bind('<Button-1>', moveright)

butup = Button(root, text='Вверх')
butup.pack()
butup.bind('<Button-1>', moveup)

butdown = Button(root, text='Вниз')
butdown.pack()
butdown.bind('<Button-1>', movedown)

root.mainloop() # цикл для поддержания отображения окна

#def delblue(event):
    #canva.delete("Hero") # удаляем наш объект с тегом Hero
#butdel = Button(root, text='Удалить') # кнопока удалить героя
#butdel.pack()
#butdel.bind('<Button-1>', delblue)

# canva.create_line(20,20,180,180, fill='white', width=3)
# canva.create_line(20,180,180,20, fill='white', width=3)  # рисую крестик