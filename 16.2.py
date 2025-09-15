class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Скорость не может быть меньше или равна 0")
    
    def count_moves(self, x2, y2):
        # Вычислим минимальное количество действий
        # Для этого определим разницы по координатам
        delta_x = abs(x2 - self.x)
        delta_y = abs(y2 - self.y)

        # Можно перемещаться по прямым направлениям на s клеток за ход.
        # Минимальное число ходов по каждой оси — это округление вверх
        # от деления разницы на текущую скорость.

        from math import ceil

        moves_x = ceil(delta_x / self.s) if delta_x != 0 else 0
        moves_y = ceil(delta_y / self.s) if delta_y != 0 else 0

        # Минимальное число ходов — это максимум между moves_x и moves_y,
        # поскольку можно двигаться одновременно по обеим осям
        return max(moves_x, moves_y)