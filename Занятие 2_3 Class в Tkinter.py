from tkinter import  *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg = 'white')
canvas.pack()
# canvas.create_rectangle(10,10,70,70, fill = 'blue', outline= '')
# canvas.create_rectangle(10,10,50,50, fill = 'red', outline= '')
# canvas.create_rectangle(10,10,30,30, fill = 'green', outline= '')
#
# canvas.create_polygon(10,180,60,120,110,180, fill='yellow', outline='red')
#
# canvas.create_rectangle(200,200,270,270, fill = 'blue', outline= '')
# canvas.create_polygon(200,200,235,150,270,200, fill='yellow', outline='red')
# canvas.create_rectangle(220,220,250,250, fill = 'white', outline= '')
class House:
    def __init__(self, roof_color, wall_color, number):
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.number = number
        self.height = 130
        self.width = 140
        self.wall = None
        self.roof = None

    def build (self, x,y):
        w = self.width
        h = self.height

        self.roof = canvas.create_polygon(x,y,
                                          x+w,y,
                                          x+w/2,h-100,
                                          fill=self.roof_color, outline='')
        self.wall = canvas.create_rectangle(x+20,y,
                                            x+120,y+100,
                                            fill=self.wall_color, outline='')

house_1 = House('green', 'black',1)
house_1.build(100,100)

window.mainloop()