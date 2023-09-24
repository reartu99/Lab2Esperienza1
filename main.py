import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def line(x, a, b):
    return a * np.array(x) + b


deltavolt = 0.02
deltacorr = 0.000005

ddpmano = [0.06, 0.12, 0.2, 0.26, 0.32, 0.38, 0.44, 0.5, 0.56, 0.62, 0.68, 0.74, 0.8, 0.86, 0.92, 0.98, 1.04, 1.12]
corrmano = [20, 40, 65, 85, 105, 130, 150, 175, 200, 220, 240, 265, 290, 310, 330, 355, 375, 400]
ncorrmano = np.array(corrmano) / 1000000
ra = 588  # In Ohms
rv = 40000  # In Omhs
era = 0
erv = 0  # Non sappiamo se gli errori sulle resistenze interne siano veramente 0 quindi mettiamo dei placeholder

plt.errorbar(ncorrmano, ddpmano, fmt="o", xerr=deltacorr, yerr=deltavolt, markersize=2)
plt.title("A valle")
plt.xlabel("Corrente")
plt.ylabel("Differenza di potenziale")

popt, pcov = sp.optimize.curve_fit(line, ncorrmano, ddpmano)
ex, ey = np.sqrt(np.diag(pcov))
print("Il fit a valle vale y = " + "(" + str(round(popt[0], 1)) + "+/-" + str(round(ex, 1)) + ")" + "x + " + str(
    round(popt[1], 2)) + "+/-" + str(round(ey, 4)))

plt.plot(ncorrmano, line(ncorrmano, popt[0], popt[1]), color="red")
plt.xticks(np.arange(0.0, 0.0005, step=0.0001))

plt.show()

rxvalle = popt[0] - ra
erxvalle = ex + era
print("rx valle = " + str(round(rxvalle, 1)) + "+/-" + str(round(erxvalle, 1)))

# Adesso facciamo lo stesso lavoro con la configurazione a monte
ddpmanomonte = [0.04, 0.09, 0.14, 0.2, 0.24, 0.3, 0.34, 0.4, 0.44, 0.5, 0.54, 0.6, 0.64, 0.68, 0.74, 0.79, 0.84, 0.88]
corrmanomonte = [20, 45, 70, 90, 115, 140, 165, 190, 210, 235, 260, 285, 310, 330, 355, 380, 400, 430]
ncorrmanomonte = np.array(corrmanomonte) / 1000000

plt.errorbar(ncorrmanomonte, ddpmanomonte, fmt="o", xerr=deltacorr, yerr=deltavolt, markersize=2, color="orange")
plt.title("A monte")

popt2, pcov2 = sp.optimize.curve_fit(line, ncorrmanomonte, ddpmanomonte)
ex2, ey2 = np.sqrt(np.diag(pcov2))
print("Il fit a valle vale y = " + "(" + str(round(popt2[0], 1)) + "+/-" + str(round(ex2, 1)) + ")" + "x + " + str(
    round(popt2[1], 3)) + "+/-" + str(round(ey2, 3)))

plt.plot(ncorrmanomonte, line(ncorrmanomonte, popt2[0], popt2[1]), color="green")
plt.xlabel("Corrente")
plt.ylabel("Differenza di potenziale")
plt.show()

rxmonte = (popt2[0] * rv) / (rv - popt2[0])
erxmonte = ((rv*rv)*ex2)/(pow((rv+popt2[0]), 2))  # Tramite derivate parziali
print("rx monte = " + str(round(rxmonte, 1)) + "+/-" + str(round(erxmonte, 1)))

# grafico unificato
plt.errorbar(ncorrmano, ddpmano, fmt="o", xerr=deltacorr, yerr=deltavolt, markersize=2)
plt.errorbar(ncorrmanomonte, ddpmanomonte, fmt="o", xerr=deltacorr, yerr=deltavolt, markersize=2)
plt.title("A confronto")
plt.plot(ncorrmanomonte, line(ncorrmanomonte, popt2[0], popt2[1]))
plt.plot(ncorrmano, line(ncorrmano, popt[0], popt[1]))
plt.xlabel("Corrente")
plt.ylabel("Differenza di potenziale")
plt.show()
