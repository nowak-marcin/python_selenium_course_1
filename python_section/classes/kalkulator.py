class BasicCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def devide(self):
        return self.x / self.y


myresult1 = BasicCalculator(2,3)
print(myresult1.add())
print(myresult1.multiply())

myresult2 = BasicCalculator(10,10)
print(myresult2.subtract())
print(myresult2.devide())

