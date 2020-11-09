# test_01.py
''' para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Declaraciones
directorio = dir(__builtins__)
callables, noCallables, funciones = [], [], []
contador1, contador2 = 0, 0

# Estructuras de control
definiciones = len(directorio)
for i in directorio:
    if callable(eval(i)) == True:
        callables.append(i)
    else:
        noCallables.append(i)


for i in callables:
    if type(eval(i)).__itemsize__ == 0:
        funciones.append(i)

# Salida estándar
print("---------------------------------------")
print(f"Número de definiciones:  {len(directorio)}")
print(f"Número de llamables:     {len(callables)}")
print(f"Número de funciones:     {len(funciones)}")
print(noCallables)
