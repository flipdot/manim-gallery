from manimlib.imports import *


class AnimationFadeInFrom(Scene):
    def construct(self):
        square = Square()
        edges = {
            'LEFT': LEFT,
            'RIGHT': RIGHT,
            'UP': UP,
            'DOWN': DOWN
        }
        for label, edge in edges.items():
            annotation = TextMobject(f'Fade In from {label}', height=.8)
            annotation.shift(2 * DOWN)
            self.add(annotation)

            self.play(FadeInFrom(square, edge))
            self.remove(annotation, square)
