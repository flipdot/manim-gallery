from manimlib.imports import *


class AnimationFadeInFromPoint(Scene):
    def construct(self):
        square = Square()
        for i in range(-6, 7, 2):
            annotation = TextMobject(f'Fade In from point {i}', height=.8)
            annotation.shift(2 * DOWN)
            self.add(annotation)
            self.play(FadeInFromPoint(square, point=i))
            self.remove(annotation, square)
