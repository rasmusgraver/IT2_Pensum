from random import randint
import matplotlib.pyplot as plt
import numpy as np

kast = []
for i in range(600):
    kast.append(randint(1,6))

bins = np.array(range(0,7))
# print(bins)
# print(kast)

kast = np.array(kast)
plt.hist(kast, bins=bins+0.5, width=0.8,color="seagreen", edgecolor="black")

plt.show()

