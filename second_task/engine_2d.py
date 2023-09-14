from color import Color

class Engine2D:
    
    def __init__(self):
        self.canvas = []
        self.current_color = Color.BLACK

    def add_figure_to_canvas(self, figure):
        self.canvas.append(figure)

    def draw(self):
        for figure in self.canvas:
            figure.draw(self.current_color)
        self.canvas.clear()

    def set_color(self, color: Color):
        self.current_color = color