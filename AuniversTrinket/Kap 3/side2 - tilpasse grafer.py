import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 50)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)

plt.grid()
plt.title("Funksjonen $f(x)=x^2$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 10)
plt.ylim(0, 150)

plt.show()


################################

import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(-2, 2, 20)
yverdier = xverdier**5

plt.axhline(0, color="black", zorder=0)
plt.axvline(0, color="black", zorder=0)
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)
plt.scatter(xverdier, yverdier, color="skyblue", marker="D", zorder=2)
plt.grid()

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()

################################
import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)
yverdier = xverdier**2

# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "bmh"
plt.style.use("bmh")

plt.plot(xverdier, yverdier)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(0, 400)

plt.show()

################################
import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 

plt.subplot(2, 1, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(2, 1, 2)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()

################################
