from manimlib.imports import *


class ChangeShape(Scene):
      def construct(self):
          circle = Circle();
          square = Square();

          self.play(Transform(circle, square));
          new_circle = Circle();
          self.play(Transform(circle, new_circle));