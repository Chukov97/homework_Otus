from src.Square import Square


class TestSquare:

    def test_create_square(self):
        square = Square(4)
        assert isinstance(square, Square)
        assert square.name == 'Square'
        assert square.widht == 4

    def test_perimeter_square(self):
        square = Square(4)
        assert square.perimetr == 16

    def test_area_square(self):
        square = Square(4)
        assert square.area == 16

    def test_add_area_square(self):
        square_one = Square(4)
        square_two = Square(8)
        assert square_one.add_area(square_two) == 80
