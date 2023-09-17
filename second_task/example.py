from engine_2d import Engine2D
from geometrical_figures import Circle, Triangle, Rectangle
from point import Point
from color import Color

engine = Engine2D()

engine.add_figure_to_canvas(Circle(Point(0,5), 5))
engine.add_figure_to_canvas(Triangle([Point(0,1), Point(0,5), Point(5,5)]))
engine.add_figure_to_canvas(Rectangle(Point(0,5), 5, 3))

engine.set_color(Color.BLUE)

engine.draw()

engine.add_figure_to_canvas(Circle(Point(0,5), 5))
engine.draw()

engine.add_figure_to_canvas(Triangle([Point(0,1), Point(0,5), Point(5,5)]))
engine.add_figure_to_canvas(Rectangle(Point(0,5), 5, 3))

engine.set_color(Color.RED)

engine.draw()
