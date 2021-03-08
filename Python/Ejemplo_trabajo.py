# Nombre Método
# Cedula Integrante 1 - Nombre de los Integrante
# Cedula Integrante 2 - Nombre de los Integrante
# Cedula Integrante 3 - Nombre de los Integrante

# importar todas las librerias necesarias
import math as m
import numpy as np


""" Resumen del Método.

Parametros de entrada:
f [func]:     la funcion ....
a [int]:
b [int]:
Imax [Int]:
Tmax [int]:

Devoluciones:
raíz:   fff...
error:   
tabla interaciones:

Funciones auxiliares:
_input_parametros:      Método que captura los parametros de entrada.
_output_texto:
_output_grafica:
_busqueda_intervalo:    Método para buscar intervalos en los que ocurra cambio de signo  
_funcion_metodo:        Método de la Bisección para encontrar raíces en un intervalo. """


def _input_parametros():
    """ Método que captura los parametros de entrada. """
    print("hola este es el método ... ")
    print("realizado por. fecha....")
    f = input("ingrese la funcion para el analisis de ....")
    a = input("ingrese el limite inferior para la busqueda")
    b = input("ingrese el limite superior para la busqueda")
    Imax = input("ingrese las iteraciones maximas para el analisis de ....")
    Tmax = input("ingrese la tolerancia deseada (...): [  ](modificabor bits, retroceso)")

def _output_texto():
    print(f"----------------------------------------")
    print(f"la raíz de la funcion es: {resultado[0]}")
    print(f"El error del método es: {resultado[1]}")
    print(f"----------------------------------------")
    print(resultado[3])
    print(f"----------------------------------------")


def _output_grafica():
    pass

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

# Defino el método iterativo de la Bisección
def _biseccion(Func, Xmin, Xmax, Imax, Tmax):
    """ Método de la Bisección para encontrar raíces en un intervalo.

        ## Parámetros:
            Func (int): función que depende de una variable.
            Xmin (int): limite inferior de intervalo.
            Xmax (int): limite superior de intervalo.
            Imax (int): número máximo de iteraciones.
            Tmax (int): exponente de tolerancia máxima, T = 1e^Tmax.
        
        ## Devoluciones:
            Km (float): valor de x encontrado.
            No (int)  : iteraciones.
            ea (float): error absoluto final
            Li (list): lista de las soluciones, los errores absolutos y la tabla con la evolución de iteraciones.
    """
    # Inicializar variables
    Xs = Xmax
    Xi = Xmin
    S = []
    E = []
    Tb = f"| I # | {'Xi':>8} | {'Xs':>8} | {'ΔX':>9} | {'Xm':>9} | {'Error Abs':>9} | {'Fm':>9} |\n"
    Tb += "-----------------------------------------------------------------------------\n"
    # Iteraciones
    for i in range(1, Imax + 1):
        ΔX = abs(Xs - Xi)
        Xm = (Xs + Xi) / 2
        ea = ΔX / 2
        S.append(Xm)
        E.append(ea)
        Fm = Func(Xm)
        Tb += f"| {i:3} | {Xi:8.5f} | {Xs:8.5f} | {ΔX:9.5f} | {Xm:9.5f} | {ea:9.5f} | {Fm:9.5f} |\n"
        if ea < (10**Tmax): break
        if Func(Xi) * Func(Xm) < 0:
            Xs = Xm
        else:
            Xi = Xm
            
    # Salida del método
    return i, Xm, ea, [S, E, Tb]

if __name__ == "__main__":
    _input_parametros()
    I = _busqueda_intervalo(f, a, b)
    resultado = _funcion_metodo(f, I[0], I[1], Imax, Tmax)
    _output_texto()
    _output_grafica()
