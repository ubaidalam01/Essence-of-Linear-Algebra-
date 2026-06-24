# Lecture 4 Matrix Multiplication — Order Matters
# Definition — Multiplying 2 matrices means applying 2 transformations one after another
# Order Matters — A × B means apply B first, then A. A × B ≠ B × A
#  Shear x Rotation = Combined Transformation
# Composition — Any 2 matrices can be combined into one single matrix giving same result
# ML Connection — Every neural network layer is a matrix, all layers combined = one big matrix


import numpy as np
import matplotlib.pyplot as plt

# ── 1. Define Matrices ────────────────────────
M1 = np.array([[1, 1],   # Shear
               [0, 1]])

M2 = np.array([[0, -1],  # Rotation
               [1,  0]])

vector = np.array([2, 1])

# ── 2. Way 1 — Alag Alag ─────────────────────
step1 = M2 @ vector      # Pehle M2
step2 = M1 @ step1       # Phir M1
print("Way 1 Result:", step2)

# ── 3. Way 2 — Combined ───────────────────────
combined = M1 @ M2
result = combined @ vector
print("Way 2 Result:", result)

# ── 4. Order Matters ──────────────────────────
reverse = M2 @ M1 @ vector
print("Reverse Order Result:", reverse)

# ── 5. Plot ───────────────────────────────────
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

origin = [0, 0]

# Original
ax1.set_title("Original Vector")
ax1.quiver(*origin, *vector, scale=1, scale_units='xy',
           angles='xy', color='blue', label=f'v {vector}')
ax1.set_xlim(-3, 4)
ax1.set_ylim(-3, 4)
ax1.grid()
ax1.legend()

# Shear then Rotation (M1 x M2)
ax2.set_title("Shear → Rotation (M1×M2)")
ax2.quiver(*origin, *vector, scale=1, scale_units='xy',
           angles='xy', color='blue', label=f'original {vector}')
ax2.quiver(*origin, *step2, scale=1, scale_units='xy',
           angles='xy', color='green', label=f'result {step2}')
ax2.set_xlim(-3, 4)
ax2.set_ylim(-3, 4)
ax2.grid()
ax2.legend()

# Rotation then Shear (M2 x M1)
ax3.set_title("Rotation → Shear (M2×M1)")
ax3.quiver(*origin, *vector, scale=1, scale_units='xy',
           angles='xy', color='blue', label=f'original {vector}')
ax3.quiver(*origin, *reverse, scale=1, scale_units='xy',
           angles='xy', color='red', label=f'result {reverse}')
ax3.set_xlim(-3, 4)
ax3.set_ylim(-3, 4)
ax3.grid()
ax3.legend()

plt.suptitle("Matrix Multiplication — Order Matters")
plt.tight_layout()
plt.show()