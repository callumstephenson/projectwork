import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# set up plot and assign x,y,z values
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X ** 2 + Y ** 2)
R = X**2 + Y**2
#Z = np.cos(R) + np.sin(X)


'''# solid contour plot
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2, 2)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
plt.axis("off")
plt.grid(False)
plt.show()'''

# wireframe contour plot
'''ax=plt.axes(projection='3d')
ax.contourf(X, Y, Z, 25, cmap='hot')
plt.axis("off")
plt.show()'''

for i in range(100):
    fig = plt.figure()
    ax = Axes3D(fig)
    multiplier = 0.75 + round(i/100,5)
    print(multiplier)
    Z = multiplier*np.sin(0.05*X)*np.cos(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
    ax.set_zlim(-2, 2)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(i),transparent=True,dpi=300)