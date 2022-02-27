import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# set up plot and assign x,y,z values and assign cmap
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.cos(R) + np.sin(X)
#Z = np.sin(0.01*X)*np.cos(R)
cmap = cm.PuRd

# solid contour plot
Z = np.cos(R+1*np.pi)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cmap)
ax.set_zlim(-2, 2)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
plt.axis("off")
plt.grid(False)
plt.show()

# wireframe contour plot
'''ax=plt.axes(projection='3d')
ax.contourf(X, Y, Z, 25, cmap='hot')
plt.axis("off")
plt.show()'''

# for loops to generate gif
'''for i in range(101):
    fig = plt.figure()
    ax = Axes3D(fig)
    multiplier = 2*(i/100)
    print(multiplier)
    Z = multiplier*np.sin(0.05*X)*np.cos(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cmap)
    ax.set_zlim(-2, 2)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(i),transparent=True,dpi=300)

for i in range(101,200):
    fig = plt.figure()
    ax = Axes3D(fig)
    multiplier = 2 - 2*((i-100)/100)
    print(multiplier)
    Z = multiplier*np.sin(0.05*X)*np.cos(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cmap)
    ax.set_zlim(-2, 2)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(i),transparent=True,dpi=300)'''

'''for i in range(1,101):
    fig = plt.figure()
    ax = Axes3D(fig)
    Z = np.cos(R+(1-(i/100))*np.pi)
    ax.contourf(X, Y, Z, cmap=cmap)
    ax.set_zlim(-2, 2)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(201-i),transparent=True,dpi=300)'''

'''for i in range(400):
    fig = plt.figure()
    ax = Axes3D(fig)
    multiplier = (i/40)
    Z = np.cos(R+multiplier*np.pi)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cmap)
    ax.set_zlim(-2, 2)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(i),transparent=True,dpi=300)'''

'''for i in range(1,101):
    fig = plt.figure()
    ax = Axes3D(fig)
    multiplier = i/100*np.pi
    Z = multiplier*np.sin(0.05*X+multiplier)*np.cos(R-multiplier)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cmap)
    ax.set_zlim(-2, 2)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    plt.axis("off")
    plt.grid(False)
    plt.savefig('frame'+str(i+130),transparent=True,dpi=300)'''
