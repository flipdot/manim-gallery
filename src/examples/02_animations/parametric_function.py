from manimlib.imports import *


def lissajous_curve_func(t):
    return np.array((np.sin(2 * t), np.sin(3 * t), 0))


class ParamFunc(Scene):

    def construct(self):
        func = ParametricFunction(lissajous_curve_func, t_max=TAU, fill_opacity=0)
        dot = Dot()
        self.add(dot)
        self.add(func)
        self.wait(3)
