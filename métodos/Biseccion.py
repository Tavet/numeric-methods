# Método de la secante
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)

import numpy as np


def secante_tabla(fx, xa, tolera):
    dx = 4 * tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo >= tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa * (xb - xa) / (fb - fa)
        tramo = abs(xc - xa)

        tabla.append([xa, xb, xc, tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return (tabla)


# PROGRAMA ---------------------
# INGRESO
fx = lambda x: np.sin(x)

a = 1
b = 4
xa = 1.5
tolera = 10 ** -3
tramos = 100

# PROCEDIMIENTO
tabla = secante_tabla(fx, xa, tolera)
n = len(tabla)
raiz = tabla[n - 1, 2]

# SALIDA
np.set_printoptions(precision=4)
print('[xa ,\t xb , \t xc , \t tramo]')
for i in range(0, n, 1):
    print(tabla[i])
print('raiz en: ', raiz)