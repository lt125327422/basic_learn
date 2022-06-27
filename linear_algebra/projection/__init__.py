import numpy as np

A = np.array([
    [1, 6],
    [0, 9],
])

B = np.array([
    [3, 0],
    [3, 3],
])

print(np.linalg.eig(A))
print(np.linalg.eig(B))
print(np.linalg.det(A))
print(np.linalg.det(B))
