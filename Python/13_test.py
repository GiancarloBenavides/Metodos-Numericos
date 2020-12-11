
import numpy as np
from matplotlib import pyplot as plt

# Definir e incluir nuevas funciones al cuaderno
def _buscar_intervalos(fun, ini, fin):
    """ Método para buscar intervalos en los que ocurra cambio de signo.

        ## Parámetros:
            fun (function): función para analizar.
            ini (int): inicio del análisis.
            fin (int): limite final del análisis.
        
        ## Devoluciones:
            I (list): Lista de tuplas con los intervalos donde hay un cero.
    """
    i = ini - 1 # Variable para contar iteraciones
    I = []      # Variable para almacenar los intervalos
    
    while i < fin:
        i += 1
        if fun(i) == 0:
            I.append((i, i))
        elif fun(i+1) == 0:
            I.append((i+1, i+1))
        elif fun(i) * fun(i+1) < 0:
            I.append((i, i+1))
        else:
            pass
    return I

x = np.linspace(-4, 5.5, 1024)

def F(x):
    y = np.exp(3*x - 12) + x * np.cos(3*x) - x**2 + 7.15
    return  y

I = _buscar_intervalos(F,-4, 6)

print(I)

Tolerancia = 1e-1
Iteraciones = 20

# Método de la bisección
# ----------------------
# Limites
Xi=I[0][0]
Xs=I[0][1]


# Gráfica
plt.axhline(y = 0, color="gray")
plt.plot(x, F(x))
plt.grid()
plt.show()

# Iteraciones
for No in range(Iteraciones):
    if abs(Xs-Xi) < Tolerancia: break
    Xm = (Xs+Xi)/2
    ea = abs(Xs-Xi)/2
    plt.axhline(y = 0, color="gray")
    plt.plot(x, F(x))
    plt.axvline(x = Xs, color="#f00")
    plt.axvline(x = Xm, color="#00F")
    plt.axvline(x = Xi, color="#f00")
    plt.text(1, 1, f"Xm = {Xm}\nea = {ea}")
    plt.grid()
    plt.show()
    if F(Xi)*F(Xm) < 0:
        Xs = Xm
    else:
        Xi = Xm
