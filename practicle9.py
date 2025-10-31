import numpy as np

def is_diagonalizable(A):
    """Check if a square matrix A is diagonalizable."""
    eigenvalues, eigenvectors = np.linalg.eig(A)
    # A matrix is diagonalizable if eigenvectors are linearly independent
    rank = np.linalg.matrix_rank(eigenvectors)
    return rank == A.shape[0], eigenvalues, eigenvectors

def cayley_hamilton_verify(A):
    """Verify the Cayley–Hamilton theorem for matrix A."""
    n = A.shape[0]
    # Characteristic polynomial coefficients (highest degree first)
    char_poly_coeffs = np.poly(A)
    
    # Evaluate polynomial at A: p(A) = c0*A^n + c1*A^(n-1) + ... + cn*I
    pA = np.zeros_like(A, dtype=float)
    for i, coeff in enumerate(char_poly_coeffs):
        power = n - i
        if power > 0:
            pA += coeff * np.linalg.matrix_power(A, power)
        else:
            pA += coeff * np.eye(n)
    return pA

# Input matrix
n = int(input("Enter the size of the square matrix: "))
print(f"Enter the {n*n} elements of the matrix row-wise (space separated):")
entries = list(map(float, input().split()))
A = np.array(entries).reshape(n, n)

print("\nMatrix A:")
print(A)

# Check diagonalizability
diag, eigenvalues, eigenvectors = is_diagonalizable(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors (as columns):")
print(eigenvectors)

if diag:
    print("\n✅ The matrix IS diagonalizable.")
else:
    print("\n❌ The matrix is NOT diagonalizable.")

# Cayley–Hamilton verification
result = cayley_hamilton_verify(A)

print("\nMatrix obtained by substituting A into its characteristic polynomial:")
print(result)

if np.allclose(result, np.zeros_like(A)):
    print("\n✅ Cayley–Hamilton theorem is verified.")
else:
    print("\n❌ Cayley–Hamilton theorem is NOT verified.")
