from manimlib.imports import *

class MakeBrace(Scene):
    def construct(self):
        dot = Dot([0,0,0])
        dot2= Dot([2,1,0])
        line = Line(dot,dot2)
        b=Brace(VGroup(dot,dot2),UP)
        eq_text = b.get_tex("x-x_1")

        self.add(dot,dot2)
        self.add(line,b, eq_text)
        self.wait()
