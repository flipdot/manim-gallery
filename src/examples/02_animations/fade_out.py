from manimlib.imports import *


class AnimationFadeOut(Scene):
    def construct(self):
        square = Square()

        anno = TextMobject('Fade Out', height=.8)
        anno.shift(2 * DOWN)
        self.add(anno)
        self.add(square)
        self.play(FadeOut(square))