import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as plot

# (3D!)set values and function
'''r = np.linspace(0, 2, 50)
p = np.linspace(0,2 * np.pi, 40)
R,phi = np.meshgrid(r,p)
X = R*np.cos(10*phi)
Y = R*np.sin(phi)
Z = R
cmap=cm.PuRd

# set up plots
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cmap)
plt.axis("off")
plt.grid(False)
plt.show()'''

# (2D!) set values and function
for i in range(600): 
    #plt.figure()
    theta = np.linspace(0, 2 * np.pi , 1000)
    rad = abs(2*np.cos(i*theta))
    x = rad*np.cos(theta)
    y = rad*np.sin(theta)
    plt.plot(x,y)
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(i),transparent=True,dpi=300)