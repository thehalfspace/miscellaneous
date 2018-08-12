# Quasi-dynamic 1D earthquake model: rate and state friction solver

import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import ode, odeint
import matplotlib.pyplot as plt

# Global constants
class Parameters:
    mu = 3e10        # Shear Modulus (Pa)
    density = 2700
    vs = np.sqrt(mu/density)
    eta = mu/(2*vs)  # radiation damping coefficient

    L = 60*1000      # width of plate boundary (m)
    k = mu/L         # stiffness aka spring constant

    Vpl = 1e-9

    Seff = 50e6     # effective normal stress (Pa)
    a = 0.015
    b = 0.02
    Dc = 0.2
    fo = 0.6
    Vo = 1e-6

class RSF:

    # Regularized rate and state friction law
    def F(V, Seff, state):
        f = a * np.arcsinh(V/(2*Vo)*np.exp(state/a))
        return f*Seff

    # State evolution: aging law
    def G(V, state):
        return (b*Vo/Dc)*(np.exp((fo - state)/b) - (V - Vo))



