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

        for k in range(0, Filas):
            pivote = AB[k][k]
            if k > 0:
                AB[k-1][k-1] = pivote

            for i in range(k+1, Filas):
                for j in range(k+1, Filas+1):
                    if k == 0:
                        AB[i][j] = (AB[i][j] * AB[k][k] - AB[i][k] * AB[k][j])
                    else:
                        AB[i][j] = (AB[i][j] * AB[k][k] - AB[i][k] * AB[k][j]) / AB[k-1][k-1]
                    
            column = np.zeros_like(B)
            column[k] = pivote
            AB = np.insert(np.delete(AB, k, axis=1), k, column.T, axis=1)
            print(AB)     
        
        return AB

# Definimos el sistema en listas
# Ma = [[1., -2., 3., -4.], [-8., 7., -6, 5.], [2., 4., 6., 8.], [7., 5., 3., 1.]]
# Mb = [21., 30., 26., 19.]

Ma = [[3, -2, 1], [4, 3, -5], [2, 1, -1]]
Mb = [2, 4, 3]

_montante(Ma, Mb)