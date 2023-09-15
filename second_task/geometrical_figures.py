from color import Color
from point import Point

class Figure:
    def draw():
        pass

class Circle(Figure):

    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius

    def draw(self, color: Color):
        if not isinstance(color, Color):
            raise TypeError(f"Inappropriate argument type passed to method {self.draw.__name__}")
        print(MessageBuilder.build_message(self, color))

class Triangle(Figure):

    def __init__(self, points: [Point]):
        self.points = points

    def draw(self, color: Color):
        if not isinstance(color, Color):
            raise TypeError(f"Inappropriate argument type passed to method {self.draw.__name__}")
        print(MessageBuilder.build_message(self, color))

class Rectangle(Figure):

    def __init__(self, upper_left_point: Point, width: int, height: int):
        self.upper_left_point = upper_left_point
        self.width = width
        self.height = height

    def draw(self, color: Color):
        if not isinstance(color, Color):
            raise TypeError(f"Inappropriate argument type passed to method {self.draw.__name__}")
        print(MessageBuilder.build_message(self, color))

class MessageBuilder:

    def build_message(figure: Figure, color: Color):
        figure_name = figure.__class__.__name__
        figure_parameters = vars(figure)
        message = f"Drawing {color.name.lower()} {figure_name} with parameters:"
        for param_name, param_value in figure_parameters.items():
            message += MessageBuilder._format_parameter(param_name, param_value)
        return message
    
    @staticmethod
    def _format_parameter(name, value):
        if isinstance (value, list):
            return f" {name} " + ", ".join(map(str, value))
        return f" {name}:{value}"