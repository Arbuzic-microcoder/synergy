class Cash:
    def __init__(self):
        self.сумма = 0  # текущее количество денег в кассе
    
    def top_up(self, X):
        """Пополнить кассу на X"""
        if X < 0:
            raise ValueError("Нельзя пополнить на отрицательное число")
        self.сумма += X
    
    def count_1000(self):
        """Вернуть целые тысячи в кассе"""
        return self.сумма // 1000
    
    def take_away(self, X):
        """Забрать X из кассы или выбросить ошибку, если недостаточно денег"""
        if X > self.сумма:
            raise ValueError("Недостаточно денег в кассе")
        self.сумма -= X