# python pozwala na dziedziczenie zmiennych i metod danej klasy z wielu innych klas

class Animal:
    def __init__(self, color, food_type):
        self.color = color
        self.food_type = food_type

    def eat(self):
        print(f'to zwierze je najczesciej: {self.food_type}')

    def coloristic(self):
        print(f'to zwierze jest koloru: {self.color}')

    def breath(self):
        print('breath...')


class Dog(Animal):
    def __init__(self, color, food_type, race, name):
        super().__init__(color, food_type)
        self.race = race
        self.name = name

    def bark(self):
        print('wooof...')


class Cat(Animal):
    def __init__(self, color, food_type, race, name):
        super().__init__(color, food_type)
        self.race = race
        self.name = name

    def meaw(self):
        print('meaw...')


mydog1 = Dog('red', 'meat', 'buldog', 'max')
print(f'Pies to: {mydog1.race}, imie to: {mydog1.name}, kolor to: {mydog1.color}')
mydog1.eat()
mydog1.bark()
mydog1.breath()

mycat1 = Cat('black', 'whiskas', 'pers', 'luna')
print(f'rasa kota to: {mycat1.race}, a imie to: {mycat1.name}')
mycat1.eat()
mycat1.meaw()
mycat1.breath()
