import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import mpl_toolkits.mplot3d.axes3d as p3

fig=plt.figure()
ax=p3.Axes3D(fig)
fig.add_axes(ax)
x=np.arange(-3,3,0.2)
y=np.arange(-3,3,0.2)
x,y=np.meshgrid(x,y)
r=np.sqrt(x**2+y**2)
z=np.sin(r)
ax.plot_surface(x,y,z,rstride=3,cstride=1,cmap="hot")

ax.contour(x,y,z, zdir = 'z', offset = -1, cmap = plt.get_cmap('rainbow'))
ax.set_zlim(-2, 2)
plt.show()
