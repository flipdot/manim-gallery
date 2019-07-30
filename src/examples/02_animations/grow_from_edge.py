from manimlib.imports import *


class AnimationGrowFromEdge(Scene):
    def construct(self):
        square = Square()
        labels = ['LEFT', 'RIGHT', 'UP', 'DOWN']
        edges = [LEFT, RIGHT, UP, DOWN]
        for label, edge in zip(labels, edges):
            anno = TextMobject(f'Grow from {label} edge', height=.8)
            anno.shift(2 * DOWN)
            self.add(anno)
            self.play(GrowFromEdge(square, edge))
            self.remove(anno, square)

        anno = TextMobject('Grow from center', height=.8)
        anno.shift(2 * DOWN)
        self.add(anno)

        self.play(GrowFromCenter(square))
