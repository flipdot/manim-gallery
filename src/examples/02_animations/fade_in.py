from manimlib.imports import *


class AnimationFadeIn(Scene):
    def construct(self):
        square = Square()

        anno = TextMobject('Fade In', height=.8)
        anno.shift(2 * DOWN)
        self.add(anno)
        self.play(FadeIn(square))
