from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r, name='Circle'):
        super().__init__(name)
        self.rad = r

    @property
    def area(self) -> int:
        return (self.rad ** 2) * 3.14

    @property
    def perimeter(self) -> int:
        return self.rad * 2 * 3.14
