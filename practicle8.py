import numpy as np

def gram_schmidt(V):
    """Perform the Gram–Schmidt process on matrix V (whose columns are vectors)."""
    n, k = V.shape
    U = np.zeros((n, k))
    
    for i in range(k):
        # Start with the original vector
        vec = V[:, i]
        
        # Subtract projections on all previously found orthogonal vectors
        for j in range(i):
            proj = np.dot(U[:, j], V[:, i]) * U[:, j]
            vec = vec - proj
        
        # Normalize the vector
        norm = np.linalg.norm(vec)
        if norm < 1e-10:  # Handle zero norm (linearly dependent vectors)
            U[:, i] = np.zeros_like(vec)
        else:
            U[:, i] = vec / norm
            
    return U

# Input number of vectors and their dimension
num_vecs = int(input("Enter number of vectors: "))
dim = int(input("Enter their dimension: "))

print("\nEnter each vector's elements separated by space:")

vectors = []
for i in range(num_vecs):
    vec = list(map(float, input(f"Vector {i+1}: ").split()))
    vectors.append(vec)

# Create matrix with vectors as columns
V = np.array(vectors).T

# Perform Gram–Schmidt process
orthonormal_basis = gram_schmidt(V)

# Display results
print("\nOrthonormal basis vectors (as columns):\n")
print(np.round(orthonormal_basis, 4))  # Rounded for cleaner display
