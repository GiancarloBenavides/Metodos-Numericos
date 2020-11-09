# test_04.py
''' FUNCIONES INCLUIDAS - "BUILT-IN"
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Funciones incorporadas en el modulo estándar builtins
""" Python cuenta con un modulo que no necesita importarse.
Dispone de 67 funciones internas que siempre se están disponibles.
Naturalmente siempre se pueden sobreescribir estas o definir nuevas funciones. """
# Entrada estándar
lista = []
items = 5
print(f"Ingrese {items} números decimales [-1.1] →")

for x in range(items):
    texto = input(f"Elige un número {x + 1}:    ")
    largo = len(texto)
    tipo = type(texto)
    print(f"Se ingreso un dato tipo → {tipo} de {largo} caracteres →")
    valor = float(texto)
    lista.append(valor)

# Funciones estándar
suma = sum(lista)
largo = len(lista)
promedio = suma/largo
absoluto = abs(promedio)
entero = int(promedio)
decimal = promedio - entero
entero_binario = bin(entero)
entero_octal = oct(entero)
entero_hexadecimal = hex(entero)

# Salida estándar
print("-----------------------------------------")
print(f"La suma exacta de los valores ingresados es |     {suma}")
print(f"Si formateamos la suma a dos decimales es   | {suma:9.2f}")
print(f"El promedio de los valores ingresados es    | {promedio:9.2f}")
print("-----------------------------------------")

print(f"la parte entera del promedio es             | {entero:9.2f}")
print(f"la parte decimal del promedio es            | {decimal:9.2f}")
print("-----------------------------------------")
print(f"la parte entera del promedio en binario     |     {entero_binario}")
print(f"la parte entera del promedio en octal       |     {entero_octal}")
print(f"la parte entera del promedio en hexadecimal |     {entero_hexadecimal}")
print("-----------------------------------------")
