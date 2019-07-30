from manimlib.imports import *


class AnimationFadeIn(Scene):
    def construct(self):
        square = Square()

        annotation = TextMobject('Fade In', height=.8)
        annotation.shift(2 * DOWN)
        self.add(annotation)
        self.play(FadeIn(square))
