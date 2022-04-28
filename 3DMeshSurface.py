#!/usr/bin/env python
# coding: utf-8

# # An Example 3D Mesh Surface

# Define a surface and then use matplotlib imshow() to plot it. See PME Ch. 10

# In[1]:


from mpl_toolkits.mplot3d import axes3d #3D axes with matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


fig = plt.figure(figsize = (7,7))
ax = fig.add_subplot(111, projection = "3d")
x = np.linspace(0, 1 * np.pi, 200)
y = np.linspace(0, 2 * np.pi, 200)
x, y = np.meshgrid(x, y)
z = -np.sin(x) * np.sin(y)


#Create a 3D wire frame of the z surface
ax.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 0.5, color = "0.25")
ax.view_init(20)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
plt.savefig("3DMeshSurface.png", bbox_inches = "tight", facecolor = "white")


# In[ ]:




