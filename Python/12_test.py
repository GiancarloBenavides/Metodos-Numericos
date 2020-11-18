# test_12.py
''' ARCHIVOS
Ejemplo para el curso de métodos numéricos
por Ing. Giancarlo Ortiz '''
# Manipular directorios y archivos en Python
''' Python proporciona funciones y métodos básicos para manipular archivos.
Estos están disponibles en la biblioteca estándar de forma predeterminada. '''

# Importar colores
import colorama
NORMAL = colorama.Fore.WHITE
EXTERNO = colorama.Fore.YELLOW
ELIMINADO = colorama.Fore.RED
ESCRITURA = colorama.Fore.GREEN

# Importar módulos
import os
import shutil
import runpy as rp
from matplotlib.pyplot import flag
import test

# Defino una función para limpiar la salida estándar
def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Declaración de variables
Path_base = os.getcwd()
PROMPT = ">>> "
Base = "/Python"
Path1 = f".{Base}/01_test.py"       # Versiones
Path2 = f".{Base}/10_test.py"       # Funciones
Cadena_inicio = "# DECLARACIÓN:"
Cadena_fin = "# EJECUCIÓN:"
Modulo = "LabMath.py"

# limpiar la salida por el terminal
limpiar()

# Ejecutando un script externo
print(NORMAL, PROMPT, f" Ejecutando el script {Path1}")
print(EXTERNO); rp.run_path(path_name=Path1)

# Eliminando un archivo
print(NORMAL, PROMPT, f" Eliminando Archivo {Modulo}")
if os.path.exists(Modulo):
    os.remove(Modulo)
    print(EXTERNO,f"---------------------------------------\n"
                + f"        {Modulo} Eliminado             \n"
                + f"---------------------------------------")


# Lectura y escritura de archivos
print(NORMAL, PROMPT, f" Ejecutando el script {Path1}")
print(ESCRITURA, f"---------------------------------------")
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
        print(f"---------------------------------------")
        print(f" Finaliza la escritura del archivo")
        print(f" Lineas escritas: {Contador-Inicio} Lineas")
        print(f"---------------------------------------")
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

# Cerrar archivos abiertos
archivo_lectura.close()
archivo_escritura.close()

# Moviendo archivos
print(NORMAL, PROMPT, f" Moviendo el archivo creado a {Path1}")
if os.path.exists(Modulo):
    shutil.move(Modulo, f".{Base}/{Modulo}")
    print(ELIMINADO,  f"---------------------------------------\n"
                    + f"        {Modulo} Copiado               \n"
                    + f"---------------------------------------")

# Importando archivos
print(NORMAL, PROMPT, f" Importando el Modulo {Modulo}")
import numpy as np          # Importando dependencias
import LabMath as al        # Importar el archivo creado
print(ESCRITURA,  f"---------------------------------------\n"
                + f"        {Modulo} importado             \n"
                + f"---------------------------------------")

print(NORMAL, PROMPT, f" Probando el Modulo {Modulo}")
# Operaciones con el archivo importado
A = np.array([[1, 1], [-1, -3]])
D = al.det(A)

# Salida estándar
print(EXTERNO,    f"---------------------------------------\n"
                + f"       Creando vector de prueba:       \n"
                + f"---------------------------------------")

print(ESCRITURA, f"\n{A}\n")

print(EXTERNO,    f"---------------------------------------\n"
                + f"      Calculando el Determinante:      \n"
                + f"---------------------------------------")

print(ESCRITURA, f"\n{D}\n")

print(EXTERNO, "---------------------------------------")
print(NORMAL, PROMPT, f" FIN DE CURSO (no olvides practicar)...")
