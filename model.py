#!/usr/bin/env python3

# model for static catenary equation
import math
import numpy as np

def inch2mm(inch):
    return inch*25.4

def z(cutoff, x, T_0, P):
    if (x <= cutoff):
        return 0
    else:
        x_cut = x - cutoff
        return (T_0 / P) * math.cosh(P * x_cut / T_0) - (T_0 / P)


def ptype(typ):
    return {
        'Studless' : lambda dia: 0.171 * pow(inch2mm(dia), 2),
        'Stud'     : lambda dia: 0.187 * pow(inch2mm(dia), 2),
        'Wire'     : lambda dia: 0.043 * pow(inch2mm(dia), 2),
        'Polyester': lambda dia: 0.0017 * pow(inch2mm(dia), 2)
    }.get(typ, lambda dia: 0.171 * pow(inch2mm(dia), 2)) # default to studless

def calculate(p, t0, h, dia, r=1000):
    # P = 0.171 * pow(inch2mm(3), 2)
    P = ptype(p)(dia)
    t0 *= 1000 # kN to N

    # l_eff being the length of afloat mooring
    l_eff = lambda: math.sqrt(h * (h + 2 * (t0 / P)))

    # l being the projected length of afloat mooring
    l = lambda: (t0 / P) * math.asinh((P / t0) * math.sqrt(h * (h + 2 * (t0 / P))))
    if(l() > r):
        print('\033[91m' + "l_eff:%f is longer than given radius" % (l()) + '\033[0m')

    x = np.linspace(0, r, 1000)
    cut = r - l()
    y = map(lambda x: z(cut, x, t0, P), x)
    return (x,y)
