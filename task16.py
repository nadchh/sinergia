#Задача 1

class box_office:
    def __init__(self, balance = 0):
        self.balance = balance
        
    def top_up(self, X):
        if X > 0:
            self.balance += X
            print(f"Касса пополнена на {X} рублей. Текущий баланс: {self.balance} рублей.")
        else:
            print("Сумма пополнения должна быть положительной!")

    def count_1000(self):
        thousands = self.balance // 1000
        print(f"В кассе {thousands} целых тысяч.")
        return thousands

    def take_away(self, X):
        if X > self.balance:
            print("Недостаточно средств в кассе!")
        else:
            self.balance -= X
            print(f"С кассы снято {X} рублей. Текущий баланс: {self.balance} рублей.")
    

box = box_office(5000)
box.top_up(6500)
print(box.balance)
box.count_1000()
box.take_away(100)
box.take_away(12000)

# Задача 2

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Черепашка переместилась вверх. Новая позиция: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Черепашка переместилась вниз. Новая позиция: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Черепашка переместилась влево. Новая позиция: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Черепашка переместилась вправо. Новая позиция: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Черепашка эволюционировала! Теперь шаг: {self.s}")

    def degrade(self):
        if self.s > 1:
            self.s -= 1
            print(f"Черепашка деградировала! Теперь шаг: {self.s}")
        else:
            raise ValueError("Шаг не может быть меньше или равен 0!")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        return moves_x + moves_y


turtle = Turtle(0, 0, 2)

turtle.go_up()
turtle.go_right()
turtle.go_left()

turtle.evolve()
turtle.degrade()

moves = turtle.count_moves(7, 6)
print(f"Минимальное количество шагов для достижения точки (7, 6): {moves}")
