import numpy as np

# Coefficient Matrix (A)
print("Enter the dimensions of coefficient matrix (A):")

NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))

print("Enter the elements of coefficient matrix (A) in a single line (separated by space):")
coeff_entries = list(map(float, input().split()))

# Create Coefficient Matrix
Coefficient_Matrix = np.array(coeff_entries).reshape(NR, NC)
print("\nCoefficient Matrix (A) is as follows:\n", Coefficient_Matrix, "\n")

# Column Matrix (B)
print("Enter the elements of column matrix (B) in a single line (separated by space):")
column_entries = list(map(float, input().split()))

Column_Matrix = np.array(column_entries).reshape(NR, 1)
print("\nColumn Matrix (B) is as follows:\n", Column_Matrix, "\n")

# Solution of System of Equations using Gauss elimination method
Solution = np.linalg.solve(Coefficient_Matrix, Column_Matrix)
print("Solution of the system of equations using Gauss elimination method:\n")
print(Solution_of_the_system_of_equations)

