from manimlib.imports import *


class Primitives(Scene):

    def construct(self):
        # TODO: put more complicated examples, e.g. parameters, in new example. Keep this one streight forward
        # circle = Circle(
        #     radius=4,
        #     stroke_width=50,
        #     stroke_color='#ffffff',
        #     fill_color='#ff0000',
        #     fill_opacity=1
        # )
        circle = Circle()
        self.play(FadeIn(circle))
        self.play(FadeOut(circle))

        square = Square()
        self.play(FadeIn(square))
        self.play(FadeOut(square))

        rect = Rectangle()
        self.play(FadeIn(rect))
        self.play(FadeOut(rect))