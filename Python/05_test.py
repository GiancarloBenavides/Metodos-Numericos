# test_05.py
''' FUNCIONES INCLUIDAS - "BUILT-IN"
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Funciones incorporadas en el modulo estándar builtins
""" En programación, una función es una sección reutilizable y aislada de un programa.
Python Dispone de 67 funciones internas que siempre se están disponibles.
Estas están incluidas en un modulo que no necesita importarse.
Naturalmente siempre se pueden sobreescribir estas o definir nuevas funciones. """

# Declaración de variables
tipos, lista = [], []       # Asignación multiple
items = 5                   # Asignación simple

# Entrada estándar
print(f"Ingrese {items} números decimales [\u00b1dd.dd] →")

# Estructuras de control - ciclo for
for x in range(items):
    texto = input(f"Elija el número {x + 1} de {items}:      ")
    largo = len(texto)
    tipos.append(str(type(texto)).split("'")[1])
    valor = float(texto)
    lista.append(valor)

# Mostrar valores ingresados por salida estándar
print(f"Lista de valores      :    → {lista}")
print(f"Lista de tipos        :    → {tipos}")

# Asignaciones y llamado a funciones de la biblioteca estándar
suma = sum(lista)
largo = len(lista)
promedio = suma/largo
absoluto = abs(promedio)
entero = int(promedio)
decimal = promedio - entero
binario = bin(entero)
octal = oct(entero)
hexadecimal = hex(entero)

# Salida estándar
print("-----------------------------------------")
print(f"La suma exacta de los valores ingresados es |     {suma}")
print(f"Si formateamos la suma a dos decimales es   | {suma:9.2f}")
print(f"El promedio de los valores ingresados es    | {promedio:9.2f}")
print("-----------------------------------------")
print(f"la parte entera del promedio es             | {entero:9.2f}")
print(f"la parte decimal del promedio es            | {decimal:9.2f}")
print("-----------------------------------------")
print(f"la parte entera del promedio en binario     |     {binario}")
print(f"la parte entera del promedio en octal       |     {octal}")
print(f"la parte entera del promedio en hexadecimal |     {hexadecimal}")
print("-----------------------------------------")
