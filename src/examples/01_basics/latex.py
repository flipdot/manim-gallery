from manimlib.imports import *


class LaTeX(Scene):

    def construct(self):
        hello = TexMobject(r'\text{Hello \LaTeX!}', height=1.6)
        formula = TexMobject(r'\int_{a}^{b} x^2 dx', height=3)
        formula.move_to(ORIGIN + DOWN * 2.5)
        self.play(
            Write(hello),
            Write(formula)
        )
        self.play(
            FadeOut(hello),
            FadeOut(formula)
        )
