from numpy import exp, log, inf, array, zeros, shape
from scipy.optimize import minimize, root
import pandas as pd


def solve_ChemEQ_log(Cl_0, Tl, guesses):

    C1 = 164.039636, -707.0056712, -26.40136817, 0
    C2 = 366.061867998774, -13326.25411, -55.68643292, 0

    def f_logK(C, T):
        C1, C2, C3, C4 = C
        return C1 + C2 / T + C3 * log(T) + C4 * T + log(1e-3)

    K1 = f_logK(C1, Tl)
    K2 = f_logK(C2, Tl)

    def f(Cl):

        Kee1 = log(Cl[3]) + log(Cl[4]) - log(Cl[0]) - 2*log(Cl[1])
        Kee2 = log(Cl[3]) + log(Cl[5]) - log(Cl[0]) - log(Cl[1]) - log(Cl[2])

        eq1 = Kee1 - K1
        eq2 = Kee2 - K2
        eq3 = Cl_0[0] - (Cl[4] + Cl[5] + Cl[0])
        eq4 = Cl_0[1] - (Cl[4] + Cl[3] + Cl[1])
        eq5 = Cl_0[2] - (Cl[5]         + Cl[2])
        eq6 = Cl[3] - (Cl[4] + Cl[5])

        eqs = array([eq1, eq2, eq3, eq4, eq5, eq6])

        return eqs

    return array(root(f, guesses).x).astype('float')






