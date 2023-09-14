from color import Color
from point import Point

class Circle():

    def __init__(self, center: Point, radius: int) -> None:
        self.center = center
        self.radius = radius

    def draw(self, color: Color):
        print(f"Drawing Circle: {self.center.x, self.center.y} with radius: {self.radius} in {color} color")

class Triangle():

    def __init__(self, points: [Point]) -> None:
        self.points = points

    def draw(self, color: Color):
        print(f"Drawing Triangle: with points: {self.points[0]},{self.points[1]},{self.points[2]} in {color} color")

class Rectangle():

    def __init__(self, upper_left_point: Point, width: int, height: int) -> None:
        self.upper_left_point = upper_left_point
        self.width = width
        self.height = height

    def draw(self, color: Color):
        print(f"Drawing Rectangle: {self.upper_left_point} with width: {self.width} and height: {self.height} in {color} color")