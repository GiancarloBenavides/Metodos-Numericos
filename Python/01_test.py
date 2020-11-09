# test_01.py
''' OPERACIONES CON CADENAS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz. '''
# Operaciones con cadenas en python 3
""" Python usa la codificación Unicode en lugar de ASCII.
Lo que hace posibles mas de 100.000 Caracteres.
Type("x") → <class 'str'> → cadena Unicode. """
import sys
info = sys.version
version = info.split(" ")[0]
plataforma = info[info.find("[")+1:len(info)-1]
print("---------------------------------------")
print(f"la instalación de Python {version} fue exitosa")
print(f"Tu plataforma elegida es {plataforma}...")
print(f"buena suerte como pythonista", "...")
print("---------------------------------------")
