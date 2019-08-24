from manimlib.imports import *

class RatePoints2(Scene):
    CONFIG = {
        "my_ratefunc1": lambda t: wiggle(t),
        "my_ratefunc2": lambda t: there_and_back(t),
        "my_ratefunc3": lambda t: there_and_back_with_pause(t, 1. / 4)
    }
    def construct(self):
        dot1a = Dot(point=[-1, 1, 0])
        dot2a = Dot(point=[-1, 0, 0])
        dot3a = Dot(point=[-1, -1, 0])

        dot1b = Dot(point=[1, 1, 0])
        dot2b = Dot(point=[1, 0, 0])
        dot3b = Dot(point=[1, -1, 0])


        self.add(dot1a,dot2a,dot3a)
        self.play( Transform(dot1a,dot1b),rate_func= self.my_ratefunc1 ,run_time=2 )
        self.play( Transform(dot2a,dot2b),rate_func= self.my_ratefunc2 ,run_time=2 )
        self.play( Transform(dot3a,dot3b),rate_func= self.my_ratefunc3 ,run_time=2 )

        self.wait(2)
