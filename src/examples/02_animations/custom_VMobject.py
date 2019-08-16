from manimlib.imports import *


class MyDotGrid(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        dot1 = Dot(fill_color=GREEN).shift(LEFT)
        dot2 = Dot(fill_color=BLUE)
        dot3 = Dot(fill_color=RED).shift(RIGHT)
        self.dotgrid = VGroup(dot1, dot2, dot3)
        self.add(self.dotgrid)

    def update_dot(self):
        self.dotgrid.become(self.dotgrid.shift(UP))


class ExampleScene(Scene):
    def construct(self):
        dot = MyDotGrid()
        dot2 = MyDotGrid()
        dot2.update_dot()
        self.add(dot)
        self.wait(1)
        self.play(Transform(dot, dot2), rate_func=linear)
        self.wait(1)
