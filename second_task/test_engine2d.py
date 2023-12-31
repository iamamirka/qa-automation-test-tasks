import pytest
from color import Color
from point import Point
from engine_2d import Engine2D
from geometrical_figures import Circle, Triangle, Rectangle

class TestEngine2D:

    def test_add_figure_to_canvas_adds_figure_to_canvas(self):
        sut = Engine2D()
        circle = Circle(Point(0, 1), 5)
        assert not sut.canvas, "Canvas is not empty"
        sut.add_figure_to_canvas(circle)
        assert sut.canvas == [circle]

    def test_add_figure_to_canvas_adds_already_added_figure_to_canvas(self):
        sut = Engine2D()
        circle = Circle(Point(0, 1), 5)
        sut.canvas.append(circle)
        sut.add_figure_to_canvas(circle)
        assert sut.canvas == [circle, circle]

    def test_add_figure_to_canvas_raises_on_wrong_argument_type_passed(self):
        sut = Engine2D()
        with pytest.raises(TypeError):
            sut.add_figure_to_canvas("circle")

    def test_set_color_sets_color(self):
        sut = Engine2D()
        color_before = sut.current_color
        sut.set_color(Color.RED)
        color_after = sut.current_color
        assert color_before != color_after
        assert color_after == Color.RED

    def test_set_color_raises_on_wrong_argument_type_passed(self):
        sut = Engine2D()
        sut.current_color = Color.BLACK
        with pytest.raises(TypeError):
            sut.set_color("violet")

    def test_set_color_raises_on_same_color_passed(self):
        sut = Engine2D()
        sut.current_color = Color.BLACK
        with pytest.raises(ValueError):
            sut.set_color(sut.current_color)

    def test_draw_draws_figure_on_canvas(self, capfd):
        sut = Engine2D()
        circle = Circle(Point(0, 1), 5)
        sut.canvas = [circle]
        sut.draw()
        drawn_figures = capfd.readouterr()[0].strip()
        assert drawn_figures == 'Drawing black Circle with parameters: center:(0,1) radius:5'

    def test_draw_draws_multiple_figures_on_canvas(self, capfd):
        sut = Engine2D()
        triangle = Triangle([Point(0,1), Point(0,5), Point(5,5)])
        rectangle = Rectangle(Point(0,0), 5, 5)
        sut.canvas = [triangle, rectangle]
        sut.draw()
        drawn_figures = capfd.readouterr()[0].strip().split('\n')
        assert drawn_figures == ['Drawing black Triangle with parameters: points (0,1), (0,5), (5,5)',
                                 'Drawing black Rectangle with parameters: upper_left_point:(0,0) width:5 height:5']

    def test_draw_raises_on_empty_canvas(self):
        sut = Engine2D()
        with pytest.raises(ValueError):
            sut.draw()

    def test_draw_clears_canvas_after_all_figures_drawn(self):
        sut = Engine2D()
        circle = Circle(Point(0, 1), 5)
        rectangle = Rectangle(Point(0,0), 5, 5)
        sut.canvas = [circle, rectangle]
        sut.draw()
        assert not sut.canvas, "Canvas was not empty after method execution"

if __name__ == "__main__":
    pytest.main([__file__])