from homework_2_OOP.src.Figure import Figure


class Square(Figure):
    def __init__(self, w, name='Square'):
        super().__init__(name)
        self.name = 'Square'
        self.widht = w

    @property
    def area(self) -> int:
        return self.widht ** 2

    @property
    def perimetr(self) -> int:
        return self.widht * 4
