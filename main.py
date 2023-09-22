import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def line(x, a, b):
    return a*np.array(x)+b

ddpmano = [0.06, 0.12, 0.2, 0.26, 0.32, 0.38, 0.44, 0.5, 0.56, 0.62, 0.68, 0.74, 0.8, 0.86, 0.92, 0.98, 1.04, 1.12]
corrmano = [20, 40, 65, 85, 105, 130, 150, 175, 200, 220, 240, 265, 290, 310, 330, 355, 375, 400]
ncorrmano = np.array(corrmano)/1000000
ra = 588 #Ohms
rv = 40000 #Omhs


plt.plot(ncorrmano, ddpmano, ".")
plt.title("A valle")

popt, pcov = sp.optimize.curve_fit(line, ncorrmano, ddpmano)
print(popt[0])

plt.plot(ncorrmano, line(ncorrmano, popt[0], popt[1]))

plt.show()

rxvalle = popt[0] - ra

#Adesso facciamo lo stesso lavoro con la configurazione a monte
ddpmanomonte = [0.04, 0.09, 0.14, 0.2, 0.24, 0.3, 0.34, 0.4, 0.44, 0.5, 0.54, 0.6, 0.64, 0.68, 0.74, 0.79, 0.84, 0.88]
corrmanomonte = [20, 45, 70, 90, 115, 140, 165, 190, 210, 235, 260, 285, 310, 330, 355, 380, 400, 430]
ncorrmanomonte = np.array(corrmanomonte)/1000000

plt.plot(ncorrmanomonte, ddpmanomonte, ".")
plt.title("A monte")

popt2, pcov2 = sp.optimize.curve_fit(line, ncorrmanomonte, ddpmanomonte)
print(popt2[0])

plt.plot(ncorrmanomonte, line(ncorrmanomonte, popt2[0], popt2[1]))

plt.show()
rxmonte = (popt2[0]*rv)/(rv-popt2[0])

print("Questo è rxmonte", rxmonte)
print("Questo è rxvalle", rxvalle)


plt.plot(ncorrmano, ddpmano, ".")
plt.plot(ncorrmanomonte, ddpmanomonte, ".")
plt.title("A confronto")
plt.plot(ncorrmanomonte, line(ncorrmanomonte, popt2[0], popt2[1]))
plt.plot(ncorrmano, line(ncorrmano, popt[0], popt[1]))
plt.show()
