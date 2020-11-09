# test_02.py
''' ENTRADA Y SALIDA ESTÁNDAR 
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Entrada y salida estándar de python 3
""" En programación, los flujos estándar son canales de comunicación de entrada y salida.
Estos canales conectan el programa de computadora y su entorno.
Permiten introducir y recibir datos desde el programa. """
# Entrada estándar
x1 = input("Elige un número entero [1-9]:    ")

# Operaciones con números
x1 = int(x1)
y1 = pow(x1, 3)
y2 = pow(x1, 0.5)

# Salida estándar
print("---------------------------------------")
print(f"Elegiste el número:      {x1:7.2f}")
print(f"El cubo de tu número es: {y1:7.2f}")
print(f"La raíz de tu número es: {y2:7.2f}")
print("---------------------------------------")
