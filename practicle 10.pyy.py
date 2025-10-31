import numpy as np

# Function to encode a message using matrix multiplication
def encode_message(message, encoding_matrix):
    """Encodes a message using the given encoding matrix (mod 26)."""
    message = message.upper().replace(" ", "")
    char_to_num = lambda c: ord(c) - ord('A')
    nums = [char_to_num(c) for c in message if c.isalpha()]
    
    # Pad message to fit matrix size
    n = encoding_matrix.shape[0]
    padding_size = (-len(nums)) % n
    nums.extend([23] * padding_size)  # 'X' padding if needed
    
    # Convert to matrix form (columns are message blocks)
    message_matrix = np.array(nums).reshape(-1, n).T
    
    # Encode by multiplying with encoding matrix mod 26
    coded_matrix = np.dot(encoding_matrix, message_matrix) % 26
    return coded_matrix

# Function to decode the encoded message
def decode_message(coded_matrix, encoding_matrix):
    """Decodes a message encoded by encode_message()."""
    decoding_matrix = np.linalg.inv(encoding_matrix)
    decoded_matrix = np.dot(decoding_matrix, coded_matrix)
    
    # Round to nearest integer and take mod 26
    decoded_matrix = np.round(decoded_matrix).astype(int) % 26
    
    # Convert numbers back to letters
    num_to_char = lambda i: chr(i + ord('A'))
    decoded_nums = decoded_matrix.T.flatten()
    decoded_chars = ''.join(num_to_char(i) for i in decoded_nums)
    return decoded_chars

# Function to check diagonalizability and verify Cayley–Hamilton theorem
def diagonal_check_and_cayley_hamilton(matrix):
    """Checks diagonalizability and verifies Cayley–Hamilton theorem for a given matrix."""
    eigvals, eigvecs = np.linalg.eig(matrix)
    rank = np.linalg.matrix_rank(eigvecs)
    diagonalizable = (rank == matrix.shape[0])
    
    # Cayley–Hamilton verification
    char_poly_coeffs = np.poly(matrix)
    n = matrix.shape[0]
    pA = np.zeros_like(matrix, dtype=float)
    
    for i, coeff in enumerate(char_poly_coeffs):
        power = n - i
        if power > 0:
            pA += coeff * np.linalg.matrix_power(matrix, power)
        else:
            pA += coeff * np.eye(n)
            
    ch_verified = np.allclose(pA, np.zeros_like(matrix))
    return eigvals, diagonalizable, ch_verified

# ------------------------ MAIN PROGRAM ------------------------

message = "Linear Algebra is fun"
print("Original message:", message)

# Example invertible 3×3 encoding matrix
encoding_matrix = np.array([
    [2, 5, 1],
    [1, 3, 1],
    [1, 2, 1]
])

print("\nEncoding Matrix:\n", encoding_matrix)

# Encode message
coded = encode_message(message, encoding_matrix)
print("\nEncoded Message Matrix (mod 26):\n", coded)

# Decode message
decoded = decode_message(coded, encoding_matrix)
print("\nDecoded Message:", decoded)

# Check diagonalizability and Cayley–Hamilton theorem
eigvals, is_diag, ch_verified = diagonal_check_and_cayley_hamilton(encoding_matrix)
print("\nEigenvalues:", np.round(eigvals, 3))
print("Is Matrix Diagonalizable?:", is_diag)
print("Cayley–Hamilton Theorem Verified?:", ch_verified)
