import numpy as np
from sympy import Matrix

# Coefficient Matrix (A) Elements
print("Enter the dimensions of Matrix (A):")
NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))

print("Enter the elements of Matrix (A) in a single line (separated by space):")
Entries = list(map(float, input().split()))

# Create Matrix (A)
A_np = np.array(Entries).reshape(NR, NC)
print("\nMatrix (A) is as follows:\n", A_np, "\n")

# Convert NumPy array to Sympy Matrix
A = Matrix(A_np)

# Null Space of A
NullSpace_list = A.nullspace()   # Returns a list of vectors
if NullSpace_list:
    NullSpace = Matrix.hstack(*NullSpace_list)  # Combine into a single matrix
else:
    NullSpace = Matrix([])  # Empty matrix if null space is zero vector only

print("Null Space of Matrix (A) is:\n", NullSpace, "\n")

# Check whether NullSpace satisfies A * NullSpace = 0
print("Checking whether NullSpace satisfies A * NullSpace = 0 ...\n")
if NullSpace.shape != (0, 0):
    print("A * NullSpace =\n", A * NullSpace, "\n")
else:
    print("A * NullSpace = [0] (Trivial Null Space)\n")

# Python Code for Nullity of a Matrix
NoC = A.shape[1]      # Number of columns
rank = A.rank()       # Rank of matrix
nullity = NoC - rank  # Nullity of matrix

print("Rank of Matrix (A) =", rank)
print("Nullity of Matrix (A) =", nullity)
