import numpy as np
import matplotlib.pyplot as plt

#number of sides for each dice
S1 = 4
S2 = 6

#The random number resulting from the sum of the random variables A and B
random_sum = np.array([float(f) for f in range(2, S1+S2+1)])
probability_distribution = np.zeros(S1+S2-1, float)

for f in range(2, S1+S2+1):
    for a in range(1, S1+1):
        for b in range(1, S2+1):
            if f == a+b: #Kronecker delta
                probability_distribution[f-2] += 1.0
    probability_distribution[f-2] /= (S1*S2)

fig, ax = plt.subplots()
ax.scatter(random_sum, probability_distribution)
plt.show()