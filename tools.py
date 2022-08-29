import math

# Number of unique combinations of length k that can be generated from a set of length n
def n_choose_k(n, k=2):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

def probability_mass_function(p, n):
    out = []
    for k in range(n):
        prob = n_choose_k(n, k) * (p**k) * ((1-p)**(n-k))
        out.append(prob)
    return out