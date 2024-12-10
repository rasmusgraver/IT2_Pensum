# -*- coding: utf-8 -*-

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Definerer en funksjon som regner ut gjenværende mengde
def N(t):
    return N0*(1/2)**(t/H)


# Sr-89
N0 = 50 # antall gram ved start
H = 51  # halveringstid i dager

# Lager arrays
t_array = np.linspace(0, 3*H, 1001)
N_array = N(t_array)


# Plotting
plt.plot(t_array, N_array, color="red")
plt.title("Halveringskurve til strontium-89")
plt.xlabel("Tid i dager") # horisontal aksetittel
plt.ylabel("Gjenværende mengde Sr-89 i gram")     # vertikal aksetittel
plt.grid()              # slår på rutenettet
plt.show()              # her skal plottet være

