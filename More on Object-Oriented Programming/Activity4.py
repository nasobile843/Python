class Rectangle():
    def __init__(self, l, w):
        self.lenght = l
        self.width = w

    def rectangle_area(self):
        return self.lenght*self.width
    
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())