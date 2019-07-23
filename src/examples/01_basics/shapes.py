from manimlib.imports import *


class Primitives(Scene):

    def construct(self):
        circle = Circle()
        self.play(Write(circle))
        self.play(FadeOut(circle))

