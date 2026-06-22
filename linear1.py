# Vectors | Chapter 1, Essence of linear algebra

# 1. What's the difference between thinking of a vector as an arrow vs a list of numbers?
# Ans: Arrow has a directtion and length starts from origin, while list of numbers : 
# The cordinates tell us where the arrows tip lands.
# 2. What does "adding two vectors" look like geometrically?
# Ans: It looks like placing the tail of one vector at the tip of another and drawing a new vector
# from the origin to the tip of the second vector
# 3. What is scalar multiplication visually?
# Simply Stretches or shrinks the vector 
# Multiply by 2 -> Stretches the vector to twice its length
# Multiply by 0.5 -> Shrinks the vector to half its length
# Multiply by -1 -> Flips the vector in the opposite direction
# Multiply by 0 -> Collapses the vector to a single point at the origin

import numpy as np
import matplotlib.pyplot as plt

# Define two vectors
v1 = np.array([3, 2])
v2 = np.array([1, 4])

# Vector addition
v3 = v1 + v2
print("Sum:", v3)

# Scalar multiplication
scaled = 2 * v1
print("Scaled:", scaled)

# Plot them
origin = [0, 0]

plt.quiver(*origin, *v1, scale=1, scale_units='xy', angles='xy', color='blue', label='v1')
plt.quiver(*origin, *v2, scale=1, scale_units='xy', angles='xy', color='red', label='v2')
plt.quiver(*origin, *v3, scale=1, scale_units='xy', angles='xy', color='green', label='v1+v2')

plt.xlim(0, 6)
plt.ylim(0, 7)
plt.grid()
plt.legend()
plt.title("Vector Addition")
plt.show()