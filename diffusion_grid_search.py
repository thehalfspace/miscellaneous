# Grid search inversion for diffusion equation

# D^n - D(0)^n = kt

# Input parameters:
#           D = measured data vector; D_i = ith measurement
#           D(0) = constant initial condition
#           t = measured times; t_i = ith measurement

# Unknown variables
#           k = unknown
#           n = unknown (between 2 and 3)

import numpy as np
import matplotlib.pyplot as plt

# trial data set
D = np.random.random(10) # 10 random points betewen 0 and 1
t = 20*np.random.random(10) # 10 random points between 0 and 20

D0 = 0.5 # assumed initial condition

# Seach space for the unknowns
k = np.linspace(-10, 10, 1000) # 10k values between -1000 to 1000
n = np.linspace(2,3,100) # 1000 values between 2 and 3

misfit = np.zeros((1000, 100))

for it_k in range(len(k)):
    for it_n in range(len(n)): # search iterations for n

        misfit[it_k, it_n] = np.linalg.norm(D**n[it_n] - D0**n[it_n] - k[it_k]*t)

idx = np.where(misfit == misfit.min())

