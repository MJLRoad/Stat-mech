import numpy as np
import matplotlib.pyplot as plt

#number of sides for each dice
S1 = 6
S2 = 3
S3 = 9

#The random number resulting from the sum of the random variables A and B
random_sum = np.array([f for f in range(3, S1+S2+S3+1)])
probability_distribution = np.zeros(S1+S2+S3-2, float)

for f in range(3, S1+S2+S3+1):
    for a in range(1, S1+1):
        for b in range(1, S2+1):
            for c in range(1, S3+1):
                if f == a+b+c: #Kronecker delta
                    probability_distribution[f-3] += 1.0
    probability_distribution[f-3] /= (S1*S2*S3)

fig, ax = plt.subplots()
ax.scatter(random_sum, probability_distribution)
plt.show()