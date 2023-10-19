import matplotlib.pyplot as plt

import sympy as symbols
import moduloanalisi
import moduloanalisi as mm
import numpy as np
import scipy as sp

V0 = 16
R1 = 100.3
R2 = 2*R1
DeltaY = []

ER1 = moduloanalisi.incertezzadigitale(1.2, R1, 2, 0.1)
ER2 = 2*ER1

# Definizione delle variabili simboliche
R1, R2 = symbols('R1 R2')
Alfa = (2 * R2) / (2 * R2 + R1 + np.sqrt(R1**2 + 4 * R1 * R2))

# Calcolo del valore Alfa
Alfa_valore = Alfa.subs({R1: R1_valore, R2: R2_valore})

# Calcolo dell'errore propagato
Alfa_errore = Alfa.diff(R1) * ER1 + Alfa.diff(R2) * ER2

print("Valore di Alfa:", Alfa_valore)
print("Errore di Alfa:", Alfa_errore)

Vn = [15.96, 7.92 , 3.96, 1.98, 0.99]
Nstadi = [1,2,3,4,5]

ErrVn = mm.incertezzadigitale(1, np.array(Vn), 3, 0.01)

print(ErrVn)



def line(x, a, b):
    return a * np.array(x) + b


# Crea il grafico a dispersione (scatter plot) dei dati
plt.scatter(Nstadi, Vn, label='Dati', color='b', marker='o')
plt.errorbar(Nstadi, Vn, ErrVn, 0, fmt="o", markersize=4)
# Mostra il grafico
plt.show()


log_Vn = np.log(Vn)
DeltaY = ErrVn/Vn


popt, pcov = sp.optimize.curve_fit(line, Nstadi, log_Vn)
plt.errorbar(Nstadi, log_Vn, DeltaY, 0, fmt="o", markersize=4)
print(popt, pcov)
plt.plot(Nstadi, line(Nstadi, popt[0], popt[1]))
plt.show()