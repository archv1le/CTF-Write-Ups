from sympy import mod_inverse

n = 5912718291679762008847883587848216166109
e = 876603837240112836821145245971528442417

# Step 1: Factorize n
# For demonstration purposes, you might want to use a library like sympy for factorization
from sympy import factorint
factors = factorint(n)
p, q = factors.keys()

# Step 2: Compute phi(n)
phi_n = (p-1) * (q-1)

# Step 3: Find d (modular multiplicative inverse of e mod phi_n)
d = mod_inverse(e, phi_n)

print(f"The private exponent (d) is: {d}")
