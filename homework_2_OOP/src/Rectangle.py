from homework_2_OOP.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, w, h, name='Rectangle'):
        super().__init__(name)
        self.widht = w
        self.height = h

    @property
    def area(self) -> int:
        return self.widht * self.height

    @property
    def perimeter(self):
        return (self.widht * 2) + (self.height * 2)
