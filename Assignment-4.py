import numpy as np

print("Enter elements of Matrix A:")

A = []

for i in range(2):
    row = []
    for j in range(2):
        x = int(input("Enter element: "))
        row.append(x)
    A.append(row)

print("\nEnter elements of Matrix B:")

B = []

for i in range(2):
    row = []
    for j in range(2):
        x = int(input("Enter element: "))
        row.append(x)
    B.append(row)

C = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition using Python List:")
print(C)

A = np.array(A)
B = np.array(B)

C = A + B

print("\nAddition using NumPy:")
print(C)
