class Hero:
    def __init__(self, name):
        self.name = name
        self.lifes = 3
        self.coord = [5, 5]
        self.loot = []

    def move(self, d):
        if d == "right":
            self.coord[0] += 1
        elif d == 'left':
            self.coord[0] -= 1
        elif d == 'up':
            self.coord[1] -= 1
        else:
            self.coord[1] += 1

    def lost_life(self):
        self.lifes -= 1

    def get_life(self, n):
        self.lifes += n

    def add__items(self, item):
        self.loot.append(item)


class Monster:
    def __init__(self, canva):
        self.coord = [10, 2]
        canva.create_rectangle(20*self.coord[0]-20, 20*self.coord[1]-20, 20*self.coord[0], 20*self.coord[1], fill='red', tags='enemy')

    def move(self, x, y, canva):
        dx = self.coord[0] - x
        dy = self.coord[1] - y
        d = max(abs(dx), abs(dy))
        if d == abs(dx):
            if dx < 0:
                self.coord[0] += 1
            elif dx > 0:
                self.coord[0] -= 1
            else:
                if dy > 0:
                    self.coord[1] -= 1
                else:
                    self.coord[1] += 1
        else:
            if dy > 0:
                self.coord[1] -= 1
            else:
                self.coord[1] += 1

        canva.delete('enemy')
        canva.create_rectangle(20*self.coord[0]-20, 20*self.coord[1]-20, 20*self.coord[0], 20*self.coord[1], fill='red', tags='enemy')