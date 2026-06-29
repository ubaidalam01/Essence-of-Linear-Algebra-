# The Deteminant tells us how much a transformation stretches or shrinks an area. 
# It also tells us if the transformation flips the area (negative determinant) or crushes it to zero (determinant = 0).
# Det = 0 -- Space is crushed to a line or point ,
# means the transformation is not invertible.(reverse impossible)
# Negative Det -- Same area scale but orientation is flipped (like flipping a paper).
# Det (M1 @ M2) = Det(M1) * Det(M2) -- The determinant of a product is the product of the determinants.


import numpy as np
import matplotlib.pyplot as plt

# ── 1. Define Matrices ────────────────────────
M1 = np.array([[3, 1],
               [0, 2]])

M2 = np.array([[2, 0],
               [1, 4]])

M_zero = np.array([[2, 1],
                   [4, 2]])  # Det = 0

M_neg = np.array([[-1, 0],
                  [ 0, 1]])  # Negative Det

# ── 2. Determinants ───────────────────────────
det_M1    = np.linalg.det(M1)
det_M2    = np.linalg.det(M2)
det_zero  = np.linalg.det(M_zero)
det_neg   = np.linalg.det(M_neg)
det_comb  = np.linalg.det(M1 @ M2)

print("=== Determinants ===")
print(f"Det(M1)        = {det_M1:.1f}")
print(f"Det(M2)        = {det_M2:.1f}")
print(f"Det(M_zero)    = {det_zero:.1f}  ← Not Invertible")
print(f"Det(M_neg)     = {det_neg:.1f}  ← Flipped")
print(f"Det(M1 × M2)   = {det_comb:.1f}")
print(f"Det(M1) × Det(M2) = {det_M1 * det_M2:.1f}")
print(f"Same? {np.isclose(det_comb, det_M1 * det_M2)}")

# ── 3. Invertible Check ───────────────────────
print("\n=== Invertible Check ===")
print(f"M1  invertible? {det_M1 != 0}")
print(f"M_zero invertible? {det_zero != 0}")

# ── 4. Visualize Area Scaling ─────────────────
def plot_transformation(ax, matrix, title):
    # Original square corners
    square = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0]])

    # Transformed square
    transformed = matrix @ square

    # Plot original
    ax.plot(square[0], square[1],
            'b-', linewidth=2, label='Original')

    # Plot transformed
    ax.plot(transformed[0], transformed[1],
            'r-', linewidth=2, label='Transformed')

    # Dotted lines showing movement
    for i in range(4):
        ax.plot([square[0, i], transformed[0, i]],
                [square[1, i], transformed[1, i]],
                'gray', linestyle='dotted', linewidth=1)

    det = np.linalg.det(matrix)
    ax.set_title(f"{title}\nDet = {det:.1f}")
    ax.set_xlim(-3, 6)
    ax.set_ylim(-3, 6)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid()
    ax.legend()

# ── 5. Plot ───────────────────────────────────
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 12))

plot_transformation(ax1, M1,     "Det = 6  (6x bigger)")
plot_transformation(ax2, M2,     "Det = 8  (8x bigger)")
plot_transformation(ax3, M_zero, "Det = 0  (Crushed!)")
plot_transformation(ax4, M_neg,  "Det = -1 (Flipped!)")

plt.suptitle("The Determinant", fontsize=15)
plt.tight_layout()
plt.show()