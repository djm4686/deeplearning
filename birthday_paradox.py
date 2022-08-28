import matplotlib.pylab as plt
import math
import numpy as np

bins = []
orderings = 0
for x in range(350):
    y = (364/365)**x
    bins.append(y)
    if y < .5:
        orderings = x
        break


print("Number of orderings for <.5 chance: {}".format(orderings))

def find_orderings(n, k=2):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

bins2 = []
n = 0
for x in range(2, 50):
    y = find_orderings(x)
    bins2.append(y)
    if y >= orderings:
        n = x
        break


xs = []
ys = []
n_people = 50
min_people = 2
trials = 10000
for m in range(min_people, n_people):
    matches = 0
    for n in range(trials):
        match = False
        b = np.random.randint(0, 364, m)
        for i in range(m):
            for j in range(i+1, m):
                if b[i] == b[j]:
                    match = True
                    break
        if match:
            matches += 1
    xs.append(m)
    ys.append(matches/trials)
    print("%2d %0.6f" % (m, matches/trials))
plt.title("Birthday Paradox")
plt.xlabel("Number of people in a room")
plt.ylabel("Probability that two randomly selected people share a birthday")
plt.plot(xs, ys)
plt.show()