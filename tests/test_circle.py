from src.Circle import Circle


class TestCircle:

    def test_create_circle(self):
        circle = Circle(10)
        assert isinstance(circle, Circle)
        assert circle.name == "Circle"
        assert circle.rad == 10

    def test_perimeter_circle(self):
        circle = Circle(10)
        assert circle.perimeter == 62.800000000000004

    def test_area_circle(self):
        circle = Circle(10)
        assert circle.area == 314.0

    def test_add_area_circle(self):
        circle_one = Circle(10)
        circle_two = Circle(5)
        assert circle_one.add_area(circle_two) == 392.5
