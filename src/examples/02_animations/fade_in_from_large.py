from manimlib.imports import *


class AnimationFadeInFromLarge(Scene):
    def construct(self):
        square = Square()

        for factor in [0.1, 0.5, 0.8, 1, 2, 5]:
            annotation = TextMobject(fr'Fade In from large scale\_factor={factor}', height=.8)
            annotation.shift(2 * DOWN)
            self.add(annotation)

            self.play(FadeInFromLarge(square, scale_factor=factor))
            self.remove(annotation, square)
