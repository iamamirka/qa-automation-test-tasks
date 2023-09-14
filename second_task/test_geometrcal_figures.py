import pytest
from color import Color
from point import Point
from engine_2d import Engine2D
from geometrical_figures import Circle, Triangle, Rectangle

class TestGeometricalFigures():

    def test_create_circle(self):
       circle = Circle(Point(0,5), 5)
       assert circle.center == Point(0,5)
       assert circle.radius == 5

    def test_create_triangle(self):
        triangle = Triangle([Point(0,1), Point(0,5), Point(5,5)])
        assert triangle.points == [Point(0,1), Point(0,5), Point(5,5)]

    def test_create_rectangle(self):
        rectangle = Rectangle(Point(0,5), 5, 3)
        assert rectangle.upper_left_point == Point(0,5)
        assert rectangle.width == 5
        assert rectangle.height == 3
    
    def test_draw_circle(self, capfd):
        circle = Circle(Point(0,0), 0)
        circle.draw(Color.AQUA)
        drawn_figure = capfd.readouterr()[0].strip()
        assert drawn_figure == 'Drawing Circle: (0, 0) with radius: 0 in Color.AQUA color'

    def test_draw_triangle(self, capfd):
        triangle = Triangle([Point(0,1), Point(0,5), Point(5,5)])
        triangle.draw(Color.GREEN)
        drawn_figure = capfd.readouterr()[0].strip()
        assert drawn_figure == 'Drawing Triangle: with points: (0,1),(0,5),(5,5) in Color.GREEN color'

    def test_draw_rectangle(self, capfd):
        rectangle = Rectangle(Point(0,0), 5, 5)
        rectangle.draw(Color.ORANGE)
        drawn_figure = capfd.readouterr()[0].strip()
        assert drawn_figure == 'Drawing Rectangle: (0,0) with width: 5 and height: 5 in Color.ORANGE color'

if __name__ == "__main__":
    pytest.main([__file__])