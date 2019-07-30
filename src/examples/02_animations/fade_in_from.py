from manimlib.imports import *


class AnimationFadeInFrom(Scene):
    def construct(self):
        square = Square()
        labels = ['LEFT', 'RIGHT', 'UP', 'DOWN']
        edges = [LEFT, RIGHT, UP, DOWN]
        for label, edge in zip(labels, edges):
            anno = TextMobject(f'Fade In from {label}', height=.8)
            anno.shift(2 * DOWN)
            self.add(anno)

            self.play(FadeInFrom(square, edge))
            self.remove(anno, square)
