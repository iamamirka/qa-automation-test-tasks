import pytest
from color import Color
from point import Point
from geometrical_figures import Circle, Triangle, Rectangle, Figure

class TestGeometricalFigures:

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
        assert drawn_figure == 'Drawing aqua Circle with parameters: center:(0,0) radius:0'

    @pytest.mark.parametrize("figure", [
        Circle(Point(0,0), 0),
        Triangle([Point(0,1), Point(0,5), Point(5,5)]),
        Rectangle(Point(0,0), 5, 5)])
    def test_draw_raises_on_wrong_value_passed(self, figure: Figure):
        with pytest.raises(TypeError):
            figure.draw("AQUA")

    def test_draw_triangle(self, capfd):
        triangle = Triangle([Point(0,1), Point(0,5), Point(5,5)])
        triangle.draw(Color.GREEN)
        drawn_figure = capfd.readouterr()[0].strip()
        assert drawn_figure == 'Drawing green Triangle with parameters: points (0,1), (0,5), (5,5)'

    def test_draw_rectangle(self, capfd):
        rectangle = Rectangle(Point(0,0), 5, 5)
        rectangle.draw(Color.ORANGE)
        drawn_figure = capfd.readouterr()[0].strip()
        assert drawn_figure == 'Drawing orange Rectangle with parameters: upper_left_point:(0,0) width:5 height:5'

if __name__ == "__main__":
    pytest.main([__file__])