import sympy as sp

# Define symbolic variables
x, y, z = sp.symbols('x y z')

# ---------------- Gradient ----------------
# Input scalar function
scalar_field = input("Enter scalar function f(x, y, z): ")
f = sp.sympify(scalar_field)

# Compute gradient (∇f)
gradient_f = sp.Matrix([f.diff(var) for var in (x, y, z)])

print("\nGradient of the scalar field (∇f):")
sp.pprint(gradient_f)

# ---------------- Divergence and Curl ----------------
print("\nEnter vector field components P, Q, R as functions of x, y, z:")

P = sp.sympify(input("P = "))
Q = sp.sympify(input("Q = "))
R = sp.sympify(input("R = "))

# Vector field F = (P, Q, R)
F = sp.Matrix([P, Q, R])

# Compute divergence (∇·F)
divergence_F = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)

print("\nDivergence of the vector field (∇·F):")
sp.pprint(divergence_F)

# Compute curl (∇×F)
curl_F = sp.Matrix([
    sp.diff(R, y) - sp.diff(Q, z),
    sp.diff(P, z) - sp.diff(R, x),
    sp.diff(Q, x) - sp.diff(P, y)
])

print("\nCurl of the vector field (∇×F):")
sp.pprint(curl_F)
