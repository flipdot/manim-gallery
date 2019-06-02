from manimlib.imports import *


class HelloWorld(Scene):

    def construct(self):
        hello = TexMobject('\\text{Hello manim!}')
        self.play(Write(hello))
        self.play(FadeOut(hello))
