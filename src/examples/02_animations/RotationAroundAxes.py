from manimlib.imports import *

class RotationAroundAxes(Scene):
    def construct(self):
        sq= Square()
        self.add(sq)
        self.wait(0.1)
        sq2= sq.copy()
        sq2.rotate(-20,  OUT+RIGHT) #rotate around the axis which lays between OUT(z) and RIGHT(x)
        self.play(Transform(sq,sq2))
