from manimlib.imports import *


class MoveAlongPath1(Scene):
    def construct(self):
        circle = Circle(radius=4)
        square = Square()
        square.move_to(2 * RIGHT)
        self.add(square)
        self.add(circle)
        self.play(MoveAlongPath(square, circle), run_time=5.0)
        self.play(MoveAlongPath(square, circle))


class MoveAlongPath2(Scene):
    def construct(self):
        circle = Circle(radius=4)
        square = Square()
        square.move_to(2 * RIGHT)
        self.add(square)
        self.play(MoveAlongPath(square, circle), run_time=5.0)
        self.play(MoveAlongPath(square, circle))
