from manimlib.imports import *


def i_need_a_name(t):
    return np.array((np.sin(2 * t), np.sin(3 * t), 0))


class ParamFunc(Scene):

    def construct(self):
        func = ParametricFunction(i_need_a_name, t_max=TAU, fill_opacity=0)
        dot = Dot()
        self.add(dot)
        self.add(func)
        self.wait(3)
