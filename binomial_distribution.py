import tools
import numpy as np

#Given 13 trials of lets make a deal, what is the probability that 7 people win without changing doors?
# n choose k * (normal win probability ^ k) * the probability of them not winning ** (n-k)
prob = tools.n_choose_k(13, 7) * ((1/3) ** 7) * ((1-(1/3))**6)
print("Probability of 7 winning out of 13 without changing doors: \n{}".format(prob))

#Now what if they switched doors?
prob = tools.n_choose_k(13, 7) * ((2/3) ** 7) * ((1-(2/3))**6)
print("Probability of 7 winning out of 13 with changing doors: \n{}".format(prob))


# What are the chances of each k given a certain probability p?
def k_probability_given_p(p, n):
    out = []
    for k in range(n):
        prob = tools.n_choose_k(n, k) * (p**k) * ((1-p)**(n-k))
        out.append(prob)
    return out

print("Probability of k successes (0 indexed) in 5 tries if p is .3: \n"
      "This is also called the 'probability mass function (pmf)\n{}".format(k_probability_given_p(.3, 5)))

# We can build the above randomly with:
sample = np.random.binomial(5, 0.3, size=100000)
sums = np.bincount(sample)
print("Randomly generated binomial distribution: \n{}".format(sums/sums.sum()))