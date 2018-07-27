# Bayesian monte carlo inversion for diffusion equation

# D^n - D(0)^n = kt

# Input parameters:
#           D = measured data vector; D_i = ith measurement
#           D(0) = constant initial condition
#           t = measured times; t_i = ith measurement

# Unknown variables
#           k = unknown
#           n = unknown (between 2 and 3)

# Using L1 misfit and laplacian likelihood,
# to accomodate for more outliers.

import numpy as np
import matplotlib.pyplot as plt


# input data set
D = np.array([4, 6, 16])
t = np.array([3600, 21600, 86400])

D0 = 3 # assumed initial condition

# Search space
# k = 1e-6 to 1e6
# n = 2 to 3

# number of trial models
no = 1000000

# Initial set of trial values
k_trial = np.random.uniform(1.0e-6, 1.0e2, no)
n_trial = np.random.uniform(2,3,no)

# Plot function
def plotModels(k_trial, n_trial, title):
    fig = plt.figure()

    ax1 = fig.add_subplot(221)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    # trial model
    ax3.scatter(k_trial, n_trial, marker = '.', s = 5)

    ax3.set_xlabel("k values")
    ax3.set_ylabel("n values")

    # histogram
    ax1.hist(k_trial, range=(k_trial.min(), k_trial.max()),\
            bins=100, edgecolor='none')

    ax1.set_ylabel('Frequency')
    ax1.set_title(title)

    ax4.hist(n_trial, range=(n_trial.min(), n_trial.max()),\
            bins=100, orientation='horizontal', edgecolor='none')

    ax4.set_xlabel('Frequency')

    plt.show()

# Plot trial models
#plotModels(k_trial, n_trial, "Search Space")

# Calculate misfit
misfit = np.zeros(no)

for it in range(no):

    residual= D**n_trial[it] - D0**n_trial[it] - k_trial[it]*t

    misfit[it] = np.sum(np.abs(residual))

# Laplacian likelihood
L = np.exp(-np.sqrt(2)*misfit)

# Normalized likelihood
L_norm = L/np.amax(L)

# Posterior model index
n_post = np.zeros(no)
k_post = np.zeros(no)

# Accept posterior models
for j in range(no):

    if L_norm[j] > np.random.uniform():
        n_post[j] = n_trial[j]
        k_post[j] = k_trial[j]

n_post = n_post[np.nonzero(n_post)]
k_post = k_post[np.nonzero(k_post)]

# Plot posterior models
#plotModels(n_post, k_post, "Posterior Models")

print("Optimized n value = ", np.mean(n_post))
print("Optimized k value = ", np.mean(k_post))
