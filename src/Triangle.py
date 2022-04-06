from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, s1, s2, s3, name='Triangle'):
        super().__init__(name)
        self.name = "Triangle"
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
            print("Треугольник существует")

        if not (
                self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1):
            print(None)
            #exit()

    @property
    def area(self) -> int:
        pol = (self.side1 + self.side2 + self.side3) / 2  # Вычисляем полупериметр
        return (pol * (pol - self.side1) * (pol - self.side2) * (
                pol - self.side3)) ** 0.5  # Вычисляем площадь по формуле Герона

    @property
    def perimeter(self) -> int:
        return self.side1 + self.side2 + self.side3
