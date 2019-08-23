from manimlib.imports import *

class RatePoints(Scene):
    def construct(self):
        dot1a = Dot( point = [-1 , 1 , 0] )
        dot2a = Dot( point = [-1 , 0 , 0] )
        dot3a = Dot( point = [-1 ,-1 , 0] )

        dot1b = Dot( point = [1, 1, 0] )
        dot2b = Dot( point = [1, 0, 0] )
        dot3b = Dot( point = [1,-1, 0] )

        self.add(dot1a,dot2a, dot3a)
        self.play( Transform(dot1a,dot1b),rate_func= linear ,run_time=2 )
        self.play( Transform(dot2a,dot2b),rate_func= smooth ,run_time=2 )
        self.play( Transform(dot3a,dot3b),rate_func= running_start,run_time=2 )

        self.wait(2)
