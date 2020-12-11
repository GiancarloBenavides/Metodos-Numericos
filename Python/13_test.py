# Importar librerías
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
        elif fun(i) * fun(i+1) < 0:
            I.append((i, i+1))
        else:
            pass
    return I

# Función de trabajo
def F(x):
    y = x**2 - 2 # np.exp(3*x - 12) + x * np.cos(3*x) - x**2 + 7.15
    return  y

def pos(inicio, final, porcentaje):
    delta = final - inicio
    pos = inicio + delta*porcentaje/100
    return pos

# Intervalo de estudio
a = -4
b = 4
Fa = F(a)
Fb = F(b)

x = np.linspace(a, b, 1024)
Intervalos = _buscar_intervalos(F, a, b)

# Gráfica
plt.axhline(y = 0, color="gray")
plt.plot(x, F(x))
plt.text(pos(a, b, 5), pos(Fa, Fb, 95), f"Intervalos = {Intervalos}")
plt.grid()
plt.show()

# Método de la bisección
# ----------------------
Tolerancia = 1e-4
Iteraciones = 20

# Limites
Xi=Intervalos[0][0]
Xs=Intervalos[0][1]

# Iteraciones
for No in range(Iteraciones):
    if abs(Xs-Xi) < Tolerancia: break
    Xm = (Xs+Xi)/2
    ea = abs(Xs-Xi)/2
    plt.axhline(y = 0, color="gray")
    plt.plot(x, F(x))
    plt.axvline(x = Xs, color="#F00")
    plt.axvline(x = Xm, color="#00F")
    plt.axvline(x = Xi, color="#F00")
    plt.text(pos(a, b, 40), pos(Fa, Fb, 90), f"Xm = {Xm}\nea = {ea}")
    plt.grid()
    plt.show()
    if F(Xi)*F(Xm) < 0:
        Xs = Xm
    else:
        Xi = Xm
