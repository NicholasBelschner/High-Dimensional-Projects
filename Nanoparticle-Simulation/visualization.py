import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load simulation data
data = pd.read_csv('lammps_output.csv')

# Extract positions
x = data['x'].values
y = data['y'].values
z = data['z'].values

# Create a 3D plot of particle trajectories
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of particle positions
ax.scatter(x, y, z, c='b', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Trajectories of Nanoparticles')

plt.savefig('particle_trajectories.png')
plt.show()
