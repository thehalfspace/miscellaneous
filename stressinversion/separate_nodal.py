##################################################
#   SEPARATE THE FAULT/NODAL PLANES GCMT DATA FILE
#	
#       Author: Prithvi
#	Date Created: 01-25-2019
#################################################

from sys import argv
from io import StringIO
import numpy as np

#   Read from input file
#   Input file is the output from gmt
#   it is the projected earthquake data

dataA = np.genfromtxt('projection1.dat', usecols=(3,4,5))
dataB = np.genfromtxt('projection1.dat', usecols=(6,7,8))
dataC = np.zeros((2*len(dataA),3))

#	Change strike to the dip direction
for x in range(len(dataA)):
	dataA[x,0] = (dataA[x,0]+90) if (dataA[x,0]+90) < 360 else (dataA[x,0]+90-360)
	dataB[x,0] = (dataB[x,0]+90) if (dataB[x,0]+90) < 360 else (dataB[x,0]+90-360)

a = 0
b = 0
c = 0
while c < 2*len(dataA):
	if c%2 == 0:
		dataC[c,:] = dataA[a,:]
		a = a+1
		c = c+1
	else:
		dataC[c,:] = dataB[b,:]
		b= b+1
		c= c+1

np.savetxt('PlaneB.txt',dataC, fmt= '%1.0f',header= 'Projection3: Both planes')
