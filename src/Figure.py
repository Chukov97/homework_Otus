class Figure:

    def __init__(self, name):
        self.name = name

    @property
    def area(self) -> int:
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError('Неверная фигура')
