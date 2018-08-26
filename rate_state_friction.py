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

    Vpl = 1e-9       # Plate motion rate at constant velocity

    Seff = 50e6     # effective normal stress (Pa)
    a = 0.015       # rate and state friction parameter 'a'
    b = 0.02        # rate and state friction parameter 'b'
    Dc = 0.2        # critical slip distance Dc
    fo = 0.6        # static friction coefficient
    Vo = 1e-6       # when V = V0, f = f0.

class RSF:

    # Regularized rate and state friction law
    def F(V, Seff, state):
        f = a * np.arcsinh(V/(2*Vo)*np.exp(state/a))
        return f*Seff

    # State evolution: aging law
    def G(V, state):
        return (b*Vo/Dc)*(np.exp((fo - state)/b) - (V - Vo))



