'''
The python code that generates the 3D parameter space plots in the 
article arXiv:2403.00070.
This version plots the second solution in the article when a generic static, 
spherically symmetric interior metric is considered.
It is straightforward to make the relevant changes for the first solution.
The text files imported from Mathematica which checks the causal condition for the 2nd solution
are included in the github repository as an example of the output.

Author: Mariam Campbell (UCT) 
Email: CMPMAR009@myuct.ac.za 
If enquiries about this file is post 2025, email me at mariam.campbell09@gmail.com

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors

## Import the text files that were imported from Mathematica
randosphere = np.loadtxt('/Users/mariamcampbell/Desktop/starobinsky4sphere1000pts.txt', dtype=float) # this file contains all the random parameter sets generated.
sosconstraintpoints = np.loadtxt('/Users/mariamcampbell/Desktop/starobinskycausalsphere1000pts.txt', dtype=float) # this file contains the parameter sets that satisfy the causal condition for the matter fluid.

## Model parameters separated into single arrays containing the generated random numbers
# Model parameters for all generated random numbers
D1randosphere = randosphere[:,0]
D2randosphere = randosphere[:,1]
rsrandosphere = randosphere[:,2]
alpharandosphere = randosphere[:,3]
# Model parameters that satisfy the causal condition
D1soscon = sosconstraintpoints[:,0]
D2soscon = sosconstraintpoints[:,1]
rssoscon = sosconstraintpoints[:,2]
alphasoscon = sosconstraintpoints[:,3]


## D1, D2, rb, alpha -- central point
centerp = [6.8, 10, 1, 0.0001]      # Defined as a list.
centerparr = np.array(centerp[2])   # Convert list to an array.
#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~######

## Changing font
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})

#####   PLOTTING   #####

## Normalizing the color bar -- this assigns the values in the array to the color bar and not the preprogrammed number to color, and centers the central parameter array on the color bar.
zmin = rsrandosphere.min()
zmax = rsrandosphere.max()
normal = colors.Normalize(vmin=zmin, vmax=zmax, clip=True)

## Plot           
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d')
# Assigning the color bar to the first set of points we want to plot. This is for all the generated random numbers. 
scamap = plt.cm.ScalarMappable(norm=normal, cmap='plasma')
fcolors = scamap.to_rgba(rsrandosphere)
# Assigning the color bar to the second sets of points that satisfy the causal condition.
scamap2 = plt.cm.ScalarMappable(norm=normal, cmap='viridis')
fcolors2 = scamap2.to_rgba(rssoscon)
# Assigning the color bar to the central point in the paramter space.
fcolors3 = scamap2.to_rgba(centerparr)
## 3D scatter plot
ax.scatter(alpharandosphere, D1randosphere, D2randosphere, facecolors=fcolors, cmap='plasma', alpha=0.07) # all the sets of generated random numbers plotted as fainter points (alpha=0.07).
ax.scatter(alphasoscon, D1soscon, D2soscon, facecolors=fcolors2, cmap='viridis', alpha=1) # the sets that satisfy the causal condition.
ax.scatter(centerp[3], centerp[0], centerp[1], facecolors=fcolors3, cmap='viridis', s=100) # the central point, plotted at a larger point size (s=100).
ax.set_xlabel('$\\alpha$', fontsize=16)
ax.set_ylabel('$D_{1}$', fontsize=16)
ax.set_zlabel('$D_{2}$', fontsize=16)
## Tuning the spacing between the color bars and figure.
cbar = fig.colorbar(scamap, pad=0.01)
cbar1 = fig.colorbar(scamap2, pad=0.01)
## Labelling the color bar.
cbar.set_label(label='$r_{b}$', size='x-large', weight='bold')


plt.show()
