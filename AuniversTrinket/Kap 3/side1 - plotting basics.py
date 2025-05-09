import matplotlib.pyplot as plt

xverdier = [0, 1, 2, 3, 4]   # Liste med x-verdier
yverdier = [0, 1, 4, 9, 16]  # Liste med y-verdier

plt.plot(xverdier, yverdier)  # Lager grafen
plt.show()                    # Viser grafen


####################

import matplotlib.pyplot as plt

xverdier = [0, 1, 2, 3, 4]   # Liste med x-verdier
yverdier = [0, 1, 4, 9, 16]  # Liste med y-verdier

plt.scatter(xverdier, yverdier)  # Lager grafen
plt.show()                       # Viser grafen


####################

import matplotlib.pyplot as plt

def f(x):
  return x**2

xverdier = []
yverdier = []

for xverdi in range(10):
  xverdier.append(xverdi)
  yverdier.append(f(xverdi))

plt.plot(xverdier, yverdier)
plt.show()

####################

import matplotlib.pyplot as plt

def f(x):
  return x**2

xverdier = [xverdi for xverdi in range(10)]
yverdier = [f(xverdi) for xverdi in xverdier]

plt.plot(xverdier, yverdier)
plt.show()

####################

import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 11)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()
