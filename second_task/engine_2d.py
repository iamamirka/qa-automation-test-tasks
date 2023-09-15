from color import Color
from geometrical_figures import Figure

class Engine2D:
    
    def __init__(self):
        self.canvas = []
        self.current_color = Color.BLACK

    def add_figure_to_canvas(self, figure: Figure):
        if not isinstance(figure, Figure):
            raise TypeError("Inappropriate argument type passed to method add_figure_to_canvas as figure")
        self.canvas.append(figure)

    def draw(self):
        if not self.canvas:
            raise ValueError("Nothing to draw, canvas is empty")
        for figure in self.canvas:
            figure.draw(self.current_color)
        self.canvas.clear()

    def set_color(self, color: Color):
        if not isinstance(color, Color):
            raise TypeError("Inappropriate argument type passed to method as color")
        if color == self.current_color:
            raise ValueError(f"Engine color is already {self.current_color.name.lower()}")
        self.current_color = color