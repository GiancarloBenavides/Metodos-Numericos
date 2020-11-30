# test_02.py
''' ENTRADA Y SALIDA ESTÁNDAR 
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Entrada y salida estándar de python 3
""" En programación, los flujos estándar son canales de comunicación de entrada y salida.
Estos canales conectan el programa de computadora y su entorno.
Python incluye por defecto funciones que permiten Entrada/Salida.
Lo que hace posible introducir y recibir datos desde el programa. """

# Entrada estándar
x1 = input("Elige un número entero [1-9]:    ")

# Asignaciones y operaciones con números
x1 = int(x1)
y1 = pow(x1, 0.5)
y2 = pow(x1, 3)
y3 = 1/x1

# Salida estándar
""" La salida de números como cadena en la terminal se puede formatear a distintos tipos.
-------------------------
| Entero            | d |
| Punto flotante    | f |
| Exponencial       | e |
-------------------------
MODIFICADORES: En el caso de los tipos exponencial y coma flotante se puede elegir el número de decimales.
También es posible elegir el separador de miles y el numero de caracteres mínimo que ocupara la cadena. """

# Salida
print("---------------------------------------")
print(f"Elegiste el número:             {x1:4d}")
print(f"La raíz cuadrada del número es: {y1:7.2f}")
print(f"El cubo de tú número es:        {y2:6.1f}")
print(f"El inverso de tú número es:     {y3:10.1e}")
print("---------------------------------------")
