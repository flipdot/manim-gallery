from manimlib.imports import *


class AnimationFadeInFromPoint(Scene):
    def construct(self):
        square = Square()
        for i in range(-6, 7, 2):
            anno = TextMobject(f'Fade In from point {i}', height=.8)
            anno.shift(2 * DOWN)
            self.add(anno)
            self.play(FadeInFromPoint(square, point=i))
            self.remove(anno, square)
