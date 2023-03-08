import threading
import time


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class Garden:
    def __init__(self, **vegetables):
        self.vegetables = vegetables

    def show(self):
        sumary = 0

        for i in self.vegetables:
            vegetable = self.vegetables[i]
            sumary += vegetable.amount

            print(f'Кількість {vegetable.name}: {vegetable.amount}шт')

        print(f'Сумарна кількість всіх овочів: {sumary}шт')


class Vegetables:
    def __init__(self):
        self.name = 'овоч'
        self.amount = 0

    def gether(self):
        self.amount += 1


class Carrot(Vegetables):
    def __init__(self):
        super().__init__()
        self.name = 'моркви'
        self.amount = 10

        set_interval(self.gether, 3)


class Tomatoes(Vegetables):
    def __init__(self):
        super().__init__()
        self.name = 'помідори'
        self.amount = 8

        set_interval(self.gether, 1)


class Potatoes(Vegetables):
    def __init__(self):
        super().__init__()
        self.name = 'картопля'
        self.amount = 6

        set_interval(self.gether, 2)


class Cucumber(Vegetables):
    def __init__(self):
        super().__init__()
        self.name = 'огірок'
        self.amount = 5

        set_interval(self.gether, 5)


class Garlic(Vegetables):
    def __init__(self):
        super().__init__()
        self.name = 'часник'
        self.amount = 10

        set_interval(self.gether, 4)


garden1 = Garden(carrot=Carrot(), tomatoes=Tomatoes(), potatoes=Potatoes(), cucumber=Cucumber(), garlic=Garlic())
time.sleep(7)
garden1.show()

garden2 = Garden(carrot=Carrot(), tomatoes=Tomatoes(), potatoes=Potatoes(), cucumber=Cucumber(), garlic=Garlic())