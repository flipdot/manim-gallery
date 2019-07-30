from manimlib.imports import *


class Grid(Scene):
    """
    Manim uses a grid to place elements. At the center of the image is the origin, coordinate (0, 0, 0).
    This example demonstrates the size of the grid.
    """

    def construct(self):
        for x in range(-7, 8):
            for y in range(-5, 6):
                annotation = TexMobject(f'P({x}, {y}, 0)', height=1.5, fill_opacity=.5)
                self.add(annotation)
                dot = Dot(point=(x, y, 0))
                self.add(dot)
                self.wait(.05)
                self.remove(annotation)
