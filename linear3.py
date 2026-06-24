# Linear Transformation Example — Video 3

# Transformation = a function that changes a vector into another vector.
# 2 Main Properties of Linear Transformation:
# 1. Linear Transformation keep the grid lines staight
# 2. Linear Transformation keep the origin fixed.
# -> just track i and j all the transformation will be described completely.
#  Because each vector = a*i + b*j, so after the transformation, it will become a*i' + b*j',


import numpy as np
import matplotlib.pyplot as plt

# ── 1. Original Basis Vectors ─────────────────
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])

# ── 2. Transformation Matrix ──────────────────
# î → [2, 1]  (pehla column)
# ĵ → [3, 4]  (dusra column)
matrix = np.array([[2, 3],
                   [1, 4]])

# ── 3. Transform Basis Vectors ────────────────
i_transformed = matrix @ i_hat
j_transformed = matrix @ j_hat

print("î pehle:", i_hat, "→ baad me:", i_transformed)
print("ĵ pehle:", j_hat, "→ baad me:", j_transformed)

# ── 4. Transform Any Vector ───────────────────
v = np.array([3, 2])
v_transformed = matrix @ v

print("\nVector pehle:", v, "→ baad me:", v_transformed)

# ── 5. Plot ───────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Before transformation
ax1.set_title("Pehle (Original)")
ax1.quiver(0, 0, *i_hat, scale=1, scale_units='xy',
           angles='xy', color='blue', label='î [1,0]')
ax1.quiver(0, 0, *j_hat, scale=1, scale_units='xy',
           angles='xy', color='red', label='ĵ [0,1]')
ax1.quiver(0, 0, *v, scale=1, scale_units='xy',
           angles='xy', color='green', label='v [3,2]')
ax1.set_xlim(-1, 6)
ax1.set_ylim(-1, 6)
ax1.grid()
ax1.legend()

# After transformation
ax2.set_title("Baad Me (Transformed)")
ax2.quiver(0, 0, *i_transformed, scale=1, scale_units='xy',
           angles='xy', color='blue', label=f'î → {i_transformed}')
ax2.quiver(0, 0, *j_transformed, scale=1, scale_units='xy',
           angles='xy', color='red', label=f'ĵ → {j_transformed}')
ax2.quiver(0, 0, *v_transformed, scale=1, scale_units='xy',
           angles='xy', color='green', label=f'v → {v_transformed}')
ax2.set_xlim(-1, 20)
ax2.set_ylim(-1, 20)
ax2.grid()
ax2.legend()

plt.suptitle("Linear Transformation — Video 3")
plt.tight_layout()
plt.show()