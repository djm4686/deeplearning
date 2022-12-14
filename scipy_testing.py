from scipy.stats import ttest_ind
import numpy as np

# gaussian curve, normal curve. randomly selected values
# params: average value, standard deviation, count
a = np.random.normal(0, 1, 1000)
b = np.random.normal(0, 0.5, 1000)
c = np.random.normal(0.1, 1, 1000)

print("==ttest==")
# a ttest is a statistical method to test whether two sets of data were generated by the same process.
print(ttest_ind(a,b))
print(ttest_ind(a,c))

