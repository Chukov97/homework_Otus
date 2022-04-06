from src.Triangle import Triangle


class TestTriangle:

    def test_create_triangle(self):
        triangle = Triangle(10, 10, 10)
        assert isinstance(triangle, Triangle)
        assert triangle.name == 'Triangle'
        assert triangle.side1 == 10
        assert triangle.side2 == 10
        assert triangle.side3 == 10

    def test_perimeter_triangle(self):
        triangle = Triangle(10, 10, 10)
        assert triangle.perimeter == 30

    def test_area_triangle(self):
        triangle = Triangle(10, 10, 10)
        assert triangle.area == 43.30127018922193

    def test_add_area_triangle(self):
        triangle_one = Triangle(10, 10, 10)
        triangle_two = Triangle(20, 20, 20)
        assert triangle_one.add_area(triangle_two) == 216.50635094610965
