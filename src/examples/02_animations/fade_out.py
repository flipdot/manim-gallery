from manimlib.imports import *


class AnimationFadeOut(Scene):
    def construct(self):
        square = Square()

        annotation = TextMobject('Fade Out', height=.8)
        annotation.shift(2 * DOWN)
        self.add(annotation)
        self.add(square)
        self.play(FadeOut(square))
