from manimlib.imports import *


class ColoringAndPosition(Scene):
    def construct(self):
        circle = Circle(color=RED)
        square = Square(color='#0000FF')
        triangle = Triangle(color=GREEN)
        square.move_to(RIGHT)
        circle.move_to(LEFT)
        triangle.move_to(2 * UP)
        self.play(FadeIn(square))
        self.play(FadeIn(circle))
        self.play(FadeIn(triangle))
        self.wait(1)


class Size(Scene):
    def construct(self):
        circle = Circle()
        medium_circle = Circle(radius=2, color='#0000FF')
        large_circle = Circle(radius=3, color=WHITE)

        self.play(ShowCreation(circle))
        self.play(ShowCreation(medium_circle))
        self.play(ShowCreation(large_circle))
        self.play(FadeOut(circle))
        self.play(FadeOut(medium_circle))
        self.play(FadeOut(large_circle))
