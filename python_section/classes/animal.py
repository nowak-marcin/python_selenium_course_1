class Animal:
    def __init__(self, color, food_type):
        self.color = color
        self.food_type = food_type

    def eat(self):
        print(f'to zwierze je najczesciej: {self.food_type}')

    def coloristic(self):
        print(f'to zwierze jest koloru: {self.color}')

    def move(self):
        print('to zwierze może sie poruszac')

    def main(self):
        self.eat()
        self.coloristic()


animal1 = Animal('szary', 'mieso')
print(f'kolor zwierzecia to: {animal1.color}, a podstawowy pokarm to: {animal1.food_type}')

animal2 = Animal('zielony', 'rosliny')
animal2.eat()
animal2.coloristic()
animal2.move()

animal3 = Animal('bialy', 'wszystko')
animal3.main()