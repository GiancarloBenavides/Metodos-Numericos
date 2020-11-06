# test_01.py 
''' para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Importando módulos
import sys

# Operaciones con cadenas
info = sys.version
version = info.split(" ")[0]
plataforma = info[info.find("[")+1:len(info)-1]
print("---------------------------------------") 
print(f"la instalación de Python {version} fue exitosa")
print(f"Tu plataforma elegida es {plataforma}...")
print(f"buena suerte como pythonista", "...")
print("---------------------------------------") 