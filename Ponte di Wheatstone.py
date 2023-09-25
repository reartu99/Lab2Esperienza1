import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def line(x, a, b):
    return a * np.array(x) + b


def tdc(x1, y1, ex1, ey1):
    return abs(x1-y1)/np.sqrt((pow(ex1, 2) + pow(ey1, 2)))


R2 = 120
R1 = 220
dR1 = 0
dR2 = 0
assex = np.arange(0, 700, 10)
assey = [300, 280, 260, 245, 230, 210, 200, 185, 170, 160, 145, 135, 120, 110, 100, 90, 85, 80, 70, 60, 50, 40, 35, 30,
         20, 15, 10, 5, 0, -5, -10, -15, -25, -30, -35, -40, -45, -50, -50, -55, -60, -65, -70, -70, -75, -80, -85, -90,
         -90, -95, -100, -100, -105, -110, -110, -115, -115, -120, -120, -125, -130, -130, -130, -135, -140, -140, -140,
         -145, -145, -150]
assexminimizzata = np.array(np.arange(240, 321, 10))
asseyminimizzata = assey[24:33:]
popt, pcov = sp.optimize.curve_fit(line, assexminimizzata, asseyminimizzata)
fitypoints = line(assexminimizzata, popt[0], popt[1])

plt.errorbar(assex, assey, fmt="o")
plt.show()

plt.errorbar(assexminimizzata, asseyminimizzata, fmt="o", markersize=2)
plt.plot(assexminimizzata, fitypoints, color="red")
plt.show()

R3 = round(-popt[1]/popt[0])
R4 = round(R2*R3/R1, 1)
sigmaA, sigmaB = np.sqrt(np.diag(pcov))

sigmaR3 = np.sqrt(1/pow(popt[0], 2)*sigmaB + pow(popt[1], 2)/pow(popt[0], 4)*sigmaA -
                  2*popt[1]/pow(popt[1], 3)*pcov[0][1])
# Viene un risultato strano, un numero altissimo e non so perchè, forse ho sbagliato la formula
sigmaR4 = R4*np.sqrt(pow(dR1/R1, 2) + pow(dR2/R2, 2) + pow(sigmaR3/R3, 2))
# Gli errori dR1 e 2 non so proprio dove andarli a prendere, quelli del multimetro digitale forse?
print("La resistenza variabile (3) al punto richiesto quindi misura:", R3, "+/-", sigmaR3, "Omhs")
print("La resistenza 4 al punto richiesto misura:", R4, "+/-", sigmaR4, "Omhs")

# mancano solo i test di consistenza con i valopri del multimetro digitale.
# Con il tester digitale abbiamo ottenuto 2184
# pm 1.0% + 2 cifre trovato sul manuale del costruttore
# Errore massimo con formula dall' ultima slide 21.8409
# Per trasformarlo in errore relativo dicono le slide di dividerlo per 2.59 facendolo diventare 8.432
