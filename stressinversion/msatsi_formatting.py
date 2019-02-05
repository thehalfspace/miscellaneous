#####################################
#   Format the fault planes to match 
#   msatsi input requirements.
#####################################


# We are doing a 0D stress inversion, which implies
# we need to have first two columns to be zero

import numpy as np

data = np.loadtxt("projection2_both_planes")

