import turtle
import time

t = turtle.Turtle()
t.speed(8) # скорость черепашки
t.shape('turtle') # варианты circle или square
# t.hideturtle() # можно скрыть черепашку
# t.home() # возвращает черепашку домой
# t.pencolor('red') # меняет цвет обводки
t.color('orange') # принимает 2 параметра: цвет пера и цвет заливки
t.begin_fill()
t.left(90) # = t.lt - повернуть черепашку в градусах
t.forward(100) # = t.fd или backward = t.bk  - движение вперед или назад
t.right(35) # = t.rt
t.forward(50)
t.right(110)
t.forward(50)
t.left(110)
t.forward(50)
t.right(110)
t.forward(50)
t.right(35)
t.forward(100)
t.right(90)
t.forward(120)
t.end_fill() # begin_fill и end_fill делают заливку фигуры

t.goto(30, 80) # левый глаз - перемещает черепаху в заданные координаты х и у. причем за черепашкой остается след
t.color('white')
t.begin_fill()
t.circle(10) # рисует круг с заданным радиусом
t.end_fill()

t.goto(27, 70) # зрачок левого глаза
t.color('black')
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup() # поднять перо, т.е. не оставлять следа при перемещении
t.goto(70, 80)
t.pendown() # опустить перо
t.color('white')
t.begin_fill()
t.circle(10)
t.end_fill()

t.goto(67, 70)
t.color('black')
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(40, 50)
t.pendown()
t.left(35)
t.forward(10)
t.right(55)
t.backward(10)

t.penup()
t.goto(40, 20)
t.pendown()
t.left(180)
t.circle(30, 45)

t.hideturtle()
time.sleep(3)