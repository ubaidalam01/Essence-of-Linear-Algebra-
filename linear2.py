# TOPICS: Basis Vectors, Linear Combinations, Span

# Whenever we scale two vectors and add them together, we get a linear combination of those vectors.
# "Linear Combination" of v and w is any vector that can be written in the form 
# a×v + b×w, where a and b are scalars.

# The set of all possible linear combinations of a given set of vectors is called the span of those vectors.
# Inshort Span means : All the places you can reach by using two arrows.

# If you fix the one of those scalars and let the other one change it's value freely ,
#  the tip of the resulting vector draw a straight line. 

# Linearly Dependent vs Independent
# If one vector is a combination of the other vectors, then the vectors are dependent.
# Example : v1 = [1, 2] and v2 = [2, 4]
# If no vector can be formed from the other vectors, then the vectors are independent.
# Example : v1 = [1, 2] and v2 = [2, 3]

import numpy as np
import matplotlib.pyplot as plt

# ── 1. Basis Vectors ───────────────────────────
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])
# ── 2. Linear Combination ──────────────────────
# [5, 3] = 5×i_hat + 3×j_hat

a = 5
b = 3

result = a * i_hat + b * j_hat
print("Linear Combination:", result)
# ── 3. Span Demo ───────────────────────────────
# Different directions = poora plane cover hota hai

v1 = np.array([2, 1])
v2 = np.array([1, 3])

# Linearly Dependent vectors

v3 = np.array([2, 4])
v4 = np.array([1, 2])  # v3 ka half — same direction
# ── 4. Plot ────────────────────────────────────

origin = [0, 0]
plt.figure(figsize=(8, 8))
# Basis vectors
plt.quiver(*origin, *i_hat, scale=1, scale_units='xy',
           angles='xy', color='blue', label='î [1,0]')
plt.quiver(*origin, *j_hat, scale=1, scale_units='xy',
           angles='xy', color='red', label='ĵ [0,1]')
# Linear combination result
plt.quiver(*origin, *result, scale=1, scale_units='xy',
           angles='xy', color='green', label=f'{a}î + {b}ĵ = {result}')


# Linearly dependent vectors
plt.quiver(*origin, *v3, scale=1, scale_units='xy',
           angles='xy', color='orange', label='v3 [2,4]')
plt.quiver(*origin, *v4, scale=1, scale_units='xy',
           angles='xy', color='purple', label='v4 [1,2] — dependent')
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.grid()
plt.legend()
plt.title("Video 2 — Basis Vectors, Linear Combinations, Span")
plt.show()

