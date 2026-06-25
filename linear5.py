# Lecture 5 3D Linear Transformations
# 3 Basis Vectors — 3D has î, ĵ, k̂ instead of 2D's î, ĵ
# 3×3 Matrix — Each column is a basis vector result: î=col1, ĵ=col2, k̂=col3
# Same Rule — result = x×(î result) + y×(ĵ result) + z×(k̂ result)
# ML Connection — Neural network data is always 3D+: [batch, sequence, features]


import numpy as np
import matplotlib.pyplot as plt

# ── 1. Define 3D Basis Vectors ────────────────
i_hat = np.array([1, 0, 0])
j_hat = np.array([0, 1, 0])
k_hat = np.array([0, 0, 1])

print("=== Original Basis Vectors ===")
print("î:", i_hat)
print("ĵ:", j_hat)
print("k̂:", k_hat)

# ── 2. Define 3D Transformation Matrix ────────
# î → [2, 3, 0]
# ĵ → [1, 4, 2]
# k̂ → [0, 1, 5]
matrix = np.array([[2, 1, 0],
                   [3, 4, 1],
                   [0, 2, 5]])

print("\n=== Transformation Matrix ===")
print(matrix)

# ── 3. Transform Basis Vectors ────────────────
i_transformed = matrix @ i_hat
j_transformed = matrix @ j_hat
k_transformed = matrix @ k_hat

print("\n=== Transformed Basis Vectors ===")
print("î gaya:", i_transformed)
print("ĵ gaya:", j_transformed)
print("k̂ gaya:", k_transformed)

# ── 4. Transform Any Vector ───────────────────
v = np.array([1, 2, 3])

# Manual calculation
manual = 1*i_transformed + 2*j_transformed + 3*k_transformed

# Matrix multiplication
matrix_result = matrix @ v

print("\n=== Vector [1, 2, 3] Transform ===")
print("Original vector    :", v)
print("Manual result      :", manual)
print("Matrix mult result :", matrix_result)
print("Same result?       :", np.allclose(manual, matrix_result))

# ── 5. Diagonal Matrix Example ────────────────
diagonal = np.array([[2, 0, 0],
                     [0, 3, 0],
                     [0, 0, 4]])

diag_result = diagonal @ v

print("\n=== Diagonal Matrix ===")
print("Diagonal matrix result:", diag_result)
print("x scaled 2x:", diag_result[0])
print("y scaled 3x:", diag_result[1])
print("z scaled 4x:", diag_result[2])

# ── 6. Plot ───────────────────────────────────
fig = plt.figure(figsize=(14, 6))

# Before transformation
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title("Original Basis Vectors")

ax1.quiver(0, 0, 0, *i_hat, color='blue',   label='î [1,0,0]')
ax1.quiver(0, 0, 0, *j_hat, color='red',    label='ĵ [0,1,0]')
ax1.quiver(0, 0, 0, *k_hat, color='green',  label='k̂ [0,0,1]')
ax1.quiver(0, 0, 0, *v,     color='purple', label=f'v {v}')

ax1.set_xlim([-1, 4])
ax1.set_ylim([-1, 4])
ax1.set_zlim([-1, 4])
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()

# After transformation
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title("Transformed Vectors")

ax2.quiver(0, 0, 0, *i_transformed, color='blue',   label=f'î→{i_transformed}')
ax2.quiver(0, 0, 0, *j_transformed, color='red',    label=f'ĵ→{j_transformed}')
ax2.quiver(0, 0, 0, *k_transformed, color='green',  label=f'k̂→{k_transformed}')
ax2.quiver(0, 0, 0, *matrix_result, color='purple', label=f'v→{matrix_result}')

ax2.set_xlim([-1, 8])
ax2.set_ylim([-1, 8])
ax2.set_zlim([-1, 8])
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend()

plt.suptitle(" 3D Linear Transformations", fontsize=14)
plt.tight_layout()
plt.show()