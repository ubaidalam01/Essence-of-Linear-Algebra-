# Lecture 7: Inverse, Column Space, Rank and Null Space
# Inverse Matrix — Undoes a transformation (A × A⁻¹ = Identity). Only exists when Det ≠ 0
# Column Space — All possible output vectors a transformation can produce (span of columns)
# Rank — Number of dimensions in the output (Rank 2 = full 2D plane, Rank 1 = line, Rank 0 = point)
# Null Space — All vectors that land on origin after transformation. When Det ≠ 0
# only zero vector. When Det = 0, more vectors exist


import numpy as np

# ── 1. Define Matrix ──────────────────────────
A = np.array([[2, 1],
              [4, 2]])

# ── 2. Determinant ────────────────────────────
det = np.linalg.det(A)
print(f"Determinant: {det:.1f}")

# ── 3. Rank ───────────────────────────────────
rank = np.linalg.matrix_rank(A)
print(f"Rank: {rank}")

# ── 4. Column Space ───────────────────────────
print(f"Column 1: {A[:, 0]}")
print(f"Column 2: {A[:, 1]}")

# ── 5. Null Space ─────────────────────────────
null_vector = np.array([1, -2])
result = A @ null_vector
print(f"Null Space vector: {null_vector}")
print(f"A × null_vector = {result}")

# ── 6. Inverse ────────────────────────────────
if det != 0:
    inverse = np.linalg.inv(A)
    print(f"Inverse:\n{inverse}")
else:
    print("Inverse does not exist! Det = 0")