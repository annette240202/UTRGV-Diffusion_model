#!/usr/bin/env python
# coding: utf-8

# # A 1-D difussion model

# Here we develop a 1-d numerical model of diffusion

# Here is the diffusion equation:
# $$ \frac{\partial z}{\partial t} = D\frac{\partial^2 z}{\partial x^2} $$

# Here, $z$ is elevation, $x$ is the spatial dimension, and $D$ is the transport rate coefficient.

# The discretized version of this equation is: 
# $$ z^{t+1}_x = z^t_x + {D \Delta t \over \Delta x^2} (z^t_{x+1} - 2z^t_x + z^t_{x-1}) $$

# We'll use two Python libraries, NumPy (for arrays) and Matplotlib (for plotting), that are not a part of the core Python library

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# Start by setting two fized model parameters, the diffusivity and the size of the model domain.

# In[ ]:


D = 100 #Diffusitivity
Lx = 300 # model domain


# Next, set up the model grid using a NumPy array

# In[ ]:


dx = 0.5 # grid spacing
x = np.arange(start=0, stop=Lx, step=dx) # the grid
nx = len(x) #size of grid nodes


# In[ ]:


nx


# In[ ]:


x


# Set the initial conditions for the model.
# The elevation $z$ is a step function with a high value on the left, a low value on the right, and a cliff at the center of the domain.

# In[ ]:


z = np.zeros_like(x) #elevation
z_left = 500
z_right = 0
z[x <= Lx / 2] = z_left #step
z[x > Lx / 2] = z_right


# Make a plot of the initial conditions of the model.

# In[ ]:


plt.figure()
plt.plot(x, z, "r")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Initial profile")


# z uses the function "zeros_like" which uses the zeros as the array we first did.

# Set the number of time steps in the model.
# Calculate a stable time setp using a stability criterion.

# In[ ]:


nt = 5000 # number of time steps
dt = 0.5 * dx**2 / D


# In[ ]:


dt


# Loop over the time stpe of the model, solving the diffusion equation using the FTCS scheme described above.

# In[ ]:


for t in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])


# Note that this is an array operation on the elevation $z$.
# The boundary conditions remain fixed in each time step.

# In[ ]:


z


# Because this array is not fun to look at, let's make a graph.

# In[ ]:


plt.figure()
plt.plot(x, z, "b")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Final profile")


# We plot x vs z and "b" is a shortcut for "blue". Then labels were added along a title.

# In[ ]:




