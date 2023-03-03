# DRY -> НЕПОВТОРЮЙ КОД!!!


# 1.) Наслідування
# 2.) Інкапсуляція
# 3.) Поліморфізм
# 4.) Абстракція

class Animal:
    def __init__(self, firstname, lastname, weight, eyes):  # це один з магічних методів
        self.__name = firstname + " " + lastname
        self.weight = weight
        self.eyes = eyes

    def breath(self):
        print(self.__name + " with " + self.eyes + " eyes and weight " + self.weight + " is breathing!")

    def jump(self):
        print(self.__name + " with " + self.eyes + " eyes and weight " + self.weight + " is jumping!")

    def eat(self):
        print(self.__name + " with " + self.eyes + " eyes and weight " + self.weight + " is eating!")



class Cat(Animal):
    def _climb(self):
        print(self.__name + " with " + self.eyes + " eyes and weight " + self.weight + " is climbing!")
    def breath(self):
        print("Ketya is breathing...")

class Dog(Animal):
    def bark(self):
        print(self.__name + " with " + self.eyes + " eyes and weight " + self.weight + " is barking!")
    def breath(self):
        print("Dog is breathing...")

class Bird(Animal):
    def fly(self):
        print(self.__name + " with " + self.eyes + " eyes and weight " + self.weight + " is flying!")


cat = Cat("Ketya", "Queen", "4kg", "green")
cat.breath()