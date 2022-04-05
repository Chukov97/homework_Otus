from src.Rectangle import Rectangle


class TestRectangle:

    def test_create_rectangle(self):
        rectangle = Rectangle(5, 10)
        assert isinstance(rectangle, Rectangle)
        assert rectangle.name == 'Rectangle'
        assert rectangle.widht == 5
        assert rectangle.height == 10

    def test_perimeter_rectangle(self):
        rectangle = Rectangle(5, 10)
        assert rectangle.perimeter == 30

    def test_area_rectangle(self):
        rectangle = Rectangle(5, 10)
        assert rectangle.area == 50

    def test_add_area_rectangle(self):
        rectangle_one = Rectangle(5, 10)
        rectangle_two = Rectangle(10, 20)
        assert rectangle_one.add_area(rectangle_two) == 250
