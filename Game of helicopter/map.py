from utils import randboll
from utils import randcell
from utils import randneibre


CELL_TYPES = ['🟩', '🌲', '🟦', '🏥', '🏦', '🔥', '🚁' ]

TREE_BONUS = 100
UPGRAID = 500

class Map:

    
    def __init__(self, width, height):
        self.cells = [[0 for i in range(width + 2)] for j in range(height + 2)]
        self.w = width
        self.h = height


    def checj_bounds(self, x, y):
        if (x < 0 or y < 0 or x>= self.h or y>= self.w):
            return False
        return True
    

    def print_map(self, helico):
        print ('⬛'*(self.w + 2))
        for ri in range(self.h):
            print('⬛', end = '')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if helico.x == ri and helico.y == ci:
                    print ('🚁', end= '')
                elif (cell >= 0 and cell <len(CELL_TYPES)):
                   print(CELL_TYPES[cell], end='')
            print('⬛')
        print ('⬛'*(self.w + 2))  


    def genetate_river(self, l):
        rc = randcell(self.w, self.h)
        rx = rc[0]
        ry = rc[1]
        self.cells[rx][ry] = 2
        while l>0:
            rc2 = randneibre(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.checj_bounds(rx2, ry2)):
                if self.cells[rx2][ry2] == 2:
                    continue
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
    

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.checj_bounds(cx, cy) and self.cells[cx][cy] == 1):
            self.cells[cx][cy] = 5
    
    def update_fire(self):
        for i in range (self.h):
            for ci in range(self.w):
                cell = self.cells[i][ci]
                if cell == 5:
                    self.cells[i][ci] = 0
        for i in  range(10):
            self.add_fire()


    def genetare_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.checj_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
    
    def genetate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randboll(r, mxr):
                    self.cells[ri][ci] = 1

    def prosses_helico(self, helico):
        c = self.cells[helico.x][helico.y]
        if (c == 2):
           helico.tank = helico.mxtank
        elif (c == 5 and helico.tank > 0):
           helico.tank -= 1
           helico.score += TREE_BONUS
           self.cells[helico.x][helico.y] = 1
        elif (c == 4 and helico.score >= UPGRAID):
            helico.mxtank += 1
            helico.score -= UPGRAID
        elif (c == 3 and helico.score >= 50):
            if helico.life > 3:
                helico.score -= 50
                helico.life = helico.mxlife

    def genetate_uphraaid_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4
    
    def genetate_mpp(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 3

