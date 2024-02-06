import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vector
v = np.array([1, -2, 1])

# Define the square matrix
M = np.array([[2, 0, 0],
              [0, 3, 0],
              [0, 0, 1]])

# Apply the square matrix to the vector
v_transformed = np.dot(M, v)
print(v_transformed)
# Plot the original vector and the transformed vector
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original vector
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b', label='Original Vector')

# Transformed vector
ax.quiver(0, 0, 0, v_transformed[0], v_transformed[1], v_transformed[2], color='r', label='Transformed Vector')

ax.set_xlim([0, max(v[0], v_transformed[0])])
ax.set_ylim([0, max(v[1], v_transformed[1])])
ax.set_zlim([0, max(v[2], v_transformed[2])])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.legend()
plt.show()
