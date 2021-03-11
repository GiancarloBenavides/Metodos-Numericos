import math as m 
import numpy as np
from numpy import ndarray
from numpy.core.records import array
import pylab as plt



# función de la montante
def _montante(Ma, Mb):
    Filas = len(Ma)
    Columnas = len(Ma[0])

    # Comprobación de matriz cuadrada, y LI
    if Filas == Columnas:
        A = np.array(Ma)
        B = np.array(Mb)
        AB = np.append(A, np.array(np.matrix(B).T), axis=1)
        M = np.zeros_like(AB)

        for k in range(0, Filas):
            for i in range(0, Filas):
                if i == k:
                    M[i] = AB[k]
                else:
                    for j in range(0, Filas+1):
                        if (j == i) and (k > i):
                            M[i][j] = AB[k][k]
                        elif j == k:
                            M[i][j] = 0
                        elif k == 0:
                            M[i][j] = (AB[i][j] * AB[k][k] - AB[i][k] * AB[k][j])
                        else:
                            M[i][j] = (AB[i][j] * AB[k][k] - AB[i][k] * AB[k][j]) / AB[k-1][k-1] 
            
            AB = M.copy()  
        
        A = AB[:,:Columnas] 
        B = AB[:,Columnas:].T

        return A, B, AB

# Definimos el sistema en listas
# Ma = [[1., -2., 3., -4.], [-8., 7., -6, 5.], [2., 4., 6., 8.], [7., 5., 3., 1.]]
# Mb = [21., 30., 26., 19.]

Ma = [[3., -2., 1.], [4., 3., -5.], [2., 1., -1.]]
Mb = [2., 4., 3.]

A, B, AB = _montante(Ma, Mb)
print(AB)
print("----------")
print(A)
print("----------")
print(B)