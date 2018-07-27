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

# input data set
D = np.array([4, 6, 16])
t = np.array([3600, 21600, 86400])

D0 = 3 # assumed initial condition

# Seach space for the unknowns
nk = 10000
nn = 10
k = np.linspace(1.0e-6, 1.0e2, nk) # 10k values between -1000 to 1000
n = np.linspace(2, 3, nn) # 1000 values between 2 and 3

misfit = np.zeros((nk, nn))

for idk in range(nk):
    for idn in range(nn):

        residual = D**n[idn] - D0**n[idn] - k[idk]*t

        misfit[idk, idn] = np.linalg.norm(residual)


#misfit = misfit[np.nonzero(misfit)]

idx = np.where(misfit == misfit.min())

print("\nOptimized k = ", k[idx[0][0]])
print("\nOptimized n = ", n[idx[1][0]])
