# test_10.py
''' ARCHIVOS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Instalar módulos
''' Python proporciona funciones y métodos básicos para manipular archivos.
Estos están disponibles en la biblioteca estándar de forma predeterminada. '''

# Importar módulos
import os
import runpy
from matplotlib.pyplot import flag
import test

# defino una función para limpiar la salida estándar
def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Declaración de variables
Path_base = os.getcwd()
Base = "/Python"
Path1 = f".{Base}/01_test.py"
Path2 = f".{Base}/08_test.py"
Cadena_inicio = "# Importar"
Cadena_fin = "# Salida"
Modulo = "algebraico.py"

# Operaciones con archivos
limpiar()
print(">>>")
print(f" Ejecutando el script {Path1}")
runpy.run_path(path_name=Path1)
print(">>>")
print(f" Eliminando modulo {Modulo}")
if os.path.exists(Modulo):
    os.remove(Modulo)

# Lectura y escritura de archivos
print(">>>")
archivo_lectura = open(Path2, "rt", encoding="utf8")
archivo_escritura = open(Modulo, "a", encoding="utf8")
Guardar = False
Texto = ""
Contador = 0
Inicio = 0
Hash = 0
for Linea in archivo_lectura:
    Contador = Contador + 1
    if Cadena_inicio in Linea:
        print(f" Inicia la escritura desde: {Contador}")
        Inicio = Contador
        Guardar = True
    if Cadena_fin in Linea:
        print(f"::END::")
        print(f" Finaliza la escritura del archivo")
        print(f" Lineas escritas: {Contador-Inicio} Lineas")
        Guardar = False
        break

    if Guardar:
        Hash = Hash + 1
        if Hash < 40:
            print(f"-", end="")
        else:
            Hash = 0
            print(f"-")
        archivo_escritura.write(Linea)


archivo_lectura.close()
archivo_escritura.close()

# Importando archivos
print("---------------------------------------")
print(f" Importando el script {Modulo}")
print("---------------------------------------")
import numpy as np      # Importando dependencias
import algebraico       # Importar el archivo creado

# Operaciones con el archivo importado
A = np.array([[1, 1], [-1, -3]])
D = algebraico.det(A)

print(f" creando vector de prueba:")
print(">>>")
print(f"\n{A}\n")
print(f" Calculando el determinante:")
print(">>>")
print(f"\n{D}\n")
print("---------------------------------------")
