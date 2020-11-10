# test_08.py
''' FUNCIONES
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' Las funciones en Python se definen con la palabra clave def, seguida del nombre de la función.
Sus parámetros se escriben entre parentesis y pueden incluir valores por defecto.
Otra forma de escribir funciones, aunque menos utilizada, es con la palabra clave lambda.
El valor devuelto en las funciones con def será el dado con la instrucción return. '''
# Importar módulos instalados
import numpy as np
from numpy import ndarray
# Definiciones de funciones
def matriz_cofactor(A:ndarray, i:int, j:int):
    ''' Define la matriz cofactor A(i, j) de una matriz A dada. 
    
        ## Parametros:
            A (array): una matriz.
            i (int): el primer indice.
            j (int): el segundo indice.
        
        ## Devoluciones:
            B (array): retorna la matriz de cofactores. 
    '''
    B = np.delete(A, i, axis=1)
    B = np.delete(B, j, axis=0)
    return B


def cofactor(A:ndarray, i:int, j:int):
    ''' Define el cofactor A(i, j) de una matriz A dada. 
        
        ## Parametros:
            A (array): una matriz.
            i (int): el primer indice.
            j (int): el segundo indice.
        
        ## Devoluciones:
            B (array): retorna la matriz de cofactores. 
    '''
    B = matriz_cofactor(A, i, j)
    return np.linalg.det(B)


def matriz_de_cofactores(A:ndarray):
    ''' Define la matriz de cofactores, que se obtiene de sustituir cada termino de A(i,j) por el C(i,j).
    
        ## Parametros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (array): la matriz de cofactores. 
    '''
    B = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i, j] = cofactor(A, i, j)
    return B

def matriz_adjunta(A:ndarray):
    ''' Define la matriz de adjunta, que se obtiene de la transpuesta de la matriz de cofactores.
    
        ## Parametros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (array): la matriz adjunta. 
    '''
    B = np.transpose(matriz_de_cofactores(A))
    return B


# Funciones Lambda
adjunta = lambda A: matriz_adjunta(A)

# Definiciones de funciones
A = np.array([[1, 3, 2], [4, 7, 9], [5, 6, 8]])
C = np.array([[1, 3, 2], [5, 6, 8]])

# Salida estándar
print("----------------------------------------------------")
print("Sea una matriz entrada A:\n")
print(A)
print("\nSe tiene que la matriz de cofactores es:\n")
print(matriz_de_cofactores(A))
print("\nY la matriz adjunta es:\n")
print(adjunta(A))
print("\n----------------------------------------------------\n")
