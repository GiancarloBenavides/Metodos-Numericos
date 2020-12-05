# test_10.py
''' FUNCIONES
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' Las funciones en Python se definen con la palabra clave def, seguida del nombre de la función.
Sus parámetros se escriben entre parentesis y pueden incluir valores por defecto.
Otra forma de escribir funciones, aunque menos utilizada, es con la palabra clave lambda.
El valor devuelto en las funciones con def será el dado con la instrucción return. '''

# DECLARACIÓN:
# Importar módulos que requieren instalación
import numpy as np
from numpy import ndarray
from numpy.core.records import array

# Definiciones de nuevas funciones con la palabra clave Def
def _menor(A: ndarray, i: int, j: int):
    ''' Define el menor de la matriz A como Ă(i, j). 
    
        ## Parámetros:
            A (array): una matriz.
            i (int): el primer indice.
            j (int): el segundo indice.
        
        ## Devoluciones:
            B (array): retorna el menor. 
    '''
    B = np.delete(A, i-1, axis=0)
    C = np.delete(B, j-1, axis=1)
    return C


def _cofactor(A: ndarray, i: int, j: int):
    ''' Define el cofactor A(i, j) de una matriz A dada. 
        
        ## Parámetros:
            A (array): una matriz.
            i (int): el primer indice.
            j (int): el segundo indice.
        
        ## Devoluciones:
            B (float): retorna el cofactor. 
    '''
    B = _menor(A, i, j)
    C = pow(-1, i+j) * round(np.linalg.det(B), 3)
    return C


def _matriz_de_cofactores(A: ndarray):
    ''' Define la matriz de cofactores, que se obtiene de sustituir cada termino de A(i,j) por el C(i,j).
    
        ## Parámetros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (array): la matriz de cofactores. 
    '''
    filas = A.shape[0]
    columnas = A.shape[1]
    B = np.zeros_like(A)
    for i in range(filas):
        for j in range(columnas):
            B[i, j] = _cofactor(A, i+1, j+1)
    return B


def _matriz_adjunta(A: ndarray):
    ''' Define la matriz de adjunta, que se obtiene de la transpuesta de la matriz de cofactores.
    
        ## Parámetros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (array): la matriz adjunta. 
    '''
    B = np.transpose(_matriz_de_cofactores(A))
    return B


def _determinante(A: ndarray):
    ''' Define el determinante de una matriz A dada.
    
        ## Parámetros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (float): el determinante de la matriz. 
    '''
    filas = A.shape[0]
    columnas = A.shape[1]
    if (filas != columnas):
        return f"ERROR: Determinante no esta definido para matrices {filas}x{columnas}"
    if (filas == 1):
        return A[0][0]
    sum = 0
    for i in range(filas):
        C = pow(-1, i+2) * A[i][0]
        M = _menor(A, i+1, 1)
        D = C * _determinante(M)
        sum = D + sum
    return sum

# Definiciones de nuevas funciones con la palabra clave Lambda
cof = lambda A: _matriz_de_cofactores(A)
adj = lambda A: _matriz_adjunta(A)
det = lambda A: _determinante(A)
inv = lambda A: (1/det(A))*adj(A)

# Asignación y llamado a funciones declaradas en el script
def _calcular_matrices(A):
    ''' Imprimir en pantalla una demostración de la funcionalidad.
    '''
    # funciones definidas en el script
    Matriz_Cofactores = cof(A)
    Matriz_Adjunta = adj(A)
    Matriz_Inversa = inv(A)              
    return Matriz_Cofactores, Matriz_Adjunta, Matriz_Inversa

# Función que no retorna ningún valor
def demo(Array):
    ''' Imprimir en pantalla una demostración de la funcionalidad.
    '''
    M13 = _menor(Array, 1, 3)
    C13 = _cofactor(Array, 1, 3)
    
    # Asignación multiple usando una función que retorna múltiples valores
    Cof, Adj, Inv = _calcular_matrices(Array)

    # función incorporada en NumPy para comparar
    Inv_np = np.linalg.inv(Array)           
    
    # Salida Estándar
    print(f"--------------------------------------------------------")
    print(f"Dada una matriz de entrada A en R³:")
    print(f">>>")
    print(f"\n{Array}\n")
    print(f"--------------------------------------------------------")
    print(f"Se tiene que cada matriz  Ă(i,j) se define como el menor")
    print(f"que resulta  de eliminar  la i-ésima fila  y  la j-ésima")
    print(f"columna, por ejemplo A₁₃ es:")
    print(f">>>")
    print(f"\n{M13}\n")
    print(f"--------------------------------------------------------")
    print(f"El cofactor se define como C(i,j) =(-1)²det(Ă(i,j)), por")
    print(f"ejemplo C₁₃ es igual a {C13};  finalmente se tiene que la")
    print(f"matriz de  cofactores de A en R³ definida como Cof(A) es")
    print(f"aquella  que resulta de  reemplazar cada elemento por su") 
    print(f"cofactor:")
    print(f">>>")
    print(f"\n{Cof}\n")
    print(f"--------------------------------------------------------")
    print(f"Y la matriz adjunta  definida  como la transpuesta de la")
    print(f"matriz de cofactores es Adj(A) =trs(Cof(A)) que resulta:")
    print(f">>>")
    print(f"\n{Adj}\n")
    print(f"--------------------------------------------------------")
    print(f"Finalmente dado que inv(A) = (1/det(A)).adj(A) se  tiene")
    print(f"que la inversa definida en el script y la de NumPy son:")
    print(f">>>")
    print(f"\n{Inv}\n")
    print(f">>>")
    print(f"\n{Inv_np}\n")

# EJECUCIÓN:
# Definición de un vector de prueba en R³ usando un tipo de dato de NumPy
Array_de_prueba = np.array([[1, 1, 1], [-1, 2, -3], [3, 0, 2]])
demo(Array_de_prueba)
