import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,5)
y = 2*x
y1= y+1
plt.plot(x,y,'-.', label="$y$=2$x$")
plt.plot(x,y1,'--',label="$y$=2$x$+1")
plt.title("Rette linjer")
plt.legend() # Viser en "liten boks" med navnene på grafene
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.xlabel("$x$")
plt.ylabel("$y$")


plt.show()

