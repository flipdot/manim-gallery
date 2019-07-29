from manimlib.imports import *


class ChangeShape(Scene):
      def construct(self):
          circle = Circle()
          square = Square()
          self.play(Transform(circle, square))
          self.wait(1)
          new_circle = Circle()
          self.play(Transform(circle, new_circle))
          self.wait(1)


class Surround(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        circle.surround(square)
        self.play(FadeIn(square))
        self.play(GrowFromCenter(circle))
        self.wait(1)
        
