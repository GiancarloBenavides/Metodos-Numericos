# test_09.py
''' FUNCIONES
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' Las funciones en Python se definen con la palabra clave def, seguida del nombre de la función.
Sus parámetros se escriben entre parentesis y pueden incluir valores por defecto.
Otra forma de escribir funciones, aunque menos utilizada, es con la palabra clave lambda.
El valor devuelto en las funciones con def será el dado con la instrucción return. '''

# Importar módulos que requieren instalación
import numpy as np
from numpy import ndarray

# Definiciones de nuevas funciones con la palabra clave Def
def menor(A: ndarray, i: int, j: int):
    ''' Define el menor de la matriz A como Ă(i, j). 
    
        ## Parametros:
            A (array): una matriz.
            i (int): el primer indice.
            j (int): el segundo indice.
        
        ## Devoluciones:
            B (array): retorna el menor. 
    '''
    B = np.delete(A, i-1, axis=0)
    C = np.delete(B, j-1, axis=1)
    return C


def cofactor(A: ndarray, i: int, j: int):
    ''' Define el cofactor A(i, j) de una matriz A dada. 
        
        ## Parametros:
            A (array): una matriz.
            i (int): el primer indice.
            j (int): el segundo indice.
        
        ## Devoluciones:
            B (float): retorna el cofactor. 
    '''
    B = menor(A, i, j)
    C = pow(-1, i+j) * round(np.linalg.det(B), 3)
    return C


def matriz_de_cofactores(A: ndarray):
    ''' Define la matriz de cofactores, que se obtiene de sustituir cada termino de A(i,j) por el C(i,j).
    
        ## Parametros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (array): la matriz de cofactores. 
    '''
    filas = A.shape[0]
    columnas = A.shape[1]
    B = np.zeros_like(A)
    for i in range(filas):
        for j in range(columnas):
            B[i, j] = cofactor(A, i+1, j+1)
    return B


def matriz_adjunta(A: ndarray):
    ''' Define la matriz de adjunta, que se obtiene de la transpuesta de la matriz de cofactores.
    
        ## Parametros:
            A (array): una matriz.
        
        ## Devoluciones:
            B (array): la matriz adjunta. 
    '''
    B = np.transpose(matriz_de_cofactores(A))
    return B


def determinante(A: ndarray):
    ''' Define el determinante de una matriz A dada.
    
        ## Parametros:
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
        M = menor(A, i+1, 1)
        D = C * determinante(M)
        sum = D + sum
    return sum

# Definiciones de nuevas funciones con la palabra clave Lambda
cof = lambda A: matriz_de_cofactores(A)
adj = lambda A: matriz_adjunta(A)
det = lambda A: determinante(A)
inv = lambda A: (1/det(A))*adj(A)

# Definición de un vector de prueba en R³ usando un tipo de dato de NumPy
A = np.array([[1, 1, 1], [-1, 2, -3], [3, 0, 2]])

# Asignación y llamado a funciones declaradas en el script
A13 = menor(A, 1, 3)
C13 = cofactor(A, 1, 3)
Cof = cof(A)
Adj = adj(A)
Inv = inv(A)              # función definida en el script
Inv_np = np.linalg.inv(A) # función incorporada en NumPy

# Salida estándar
print(f"--------------------------------------------------------")
print(f"Dada una matriz de entrada A en R³:")
print(f">>>")
print(f"\n{A}\n")
print(f"--------------------------------------------------------")
print(f"Se tiene que cada matriz  Ă(i,j) se define como el menor")
print(f"que resulta  de eliminar  la i-ésima fila  y  la j-ésima")
print(f"columna, por ejemplo A₁₃ es:")
print(f">>>")
print(f"\n{A13}\n")
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
