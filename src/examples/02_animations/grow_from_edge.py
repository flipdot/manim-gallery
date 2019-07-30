from manimlib.imports import *


class AnimationGrowFromEdge(Scene):
    def construct(self):
        square = Square()
        labels = ['LEFT', 'RIGHT', 'UP', 'DOWN']
        edges = [LEFT, RIGHT, UP, DOWN]
        for label, edge in zip(labels, edges):
            annotation = TextMobject(f'Grow from {label} edge', height=.8)
            annotation.shift(2 * DOWN)
            self.add(annotation)
            self.play(GrowFromEdge(square, edge))
            self.remove(annotation, square)

        annotation = TextMobject('Grow from center', height=.8)
        annotation.shift(2 * DOWN)
        self.add(annotation)

        self.play(GrowFromCenter(square))
