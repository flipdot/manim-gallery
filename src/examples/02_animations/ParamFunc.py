from manimlib.imports import *

class ParamFunc(Scene):

    def func(self,t):
        return np.array((np.sin(2*t), np.sin(3*t),0))

    def construct(self):
        func=ParametricFunction(self.func, t_max=TAU, fill_opacity=0)
        dot = Dot()
        self.add(dot)
        self.add(func)
        self.wait(3)
