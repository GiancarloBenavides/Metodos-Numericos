# Métodos-Numéricos
Notas y algoritmos para el curso de Métodos Numéricos 2020-B
Creado por Giancarlo Ortiz con Python en Jupyter Notebook.

## Teoría del Error
El error es inherente a los métodos numéricos, por tanto es fundamental hacer  seguimiento de la propagación de los errores cometidos a fin de poder estimar el grado de aproximación de la solución que se obtiene.

* _Tipos de Redondeo_
    * _Aproximación_
    * _Truncamiento_
* _Tipos de Error_
    * _Error absoluto_
    * _Error relativo_
* _Propagación del Error_
    * _Estabilidad_
    * _Convergencia_

## Raíces de ecuaciones
El objetivo de este apartado es la determinación de los valores de la variable independiente x para los que se cumple:
<div align="center">
<img class="formula" alt="Ecuación" src = "https://render.githubusercontent.com/render/math?math=\Large \begin{align*} f(x) = 0 \end{align*}">
</div>

### Métodos:
* _Método de Bisección_
* _Método de Falsa Posición_
* _Método de la Secante_
* _Método de Newton_
* _Raíces de un polinomio_

## Solución de Sistemas de Ecuaciones Lineales
El objetivo de este apartado es examinar los aspectos numéricos que se presentan al resolver sistemas de ecuaciones lineales de la forma:
<div align="center">
<img class="formula" src="https://render.githubusercontent.com/render/math?math=%5CLarge%0A%5Cbegin%7Balign*%7D%0A%5Cbegin%7Bpmatrix%7D%0Aa_%7B11%7D%26a_%7B12%7D%26...%26a_%7B1n%7D%5C%5Ca_%7B21%7D%26a_%7B22%7D%26...%26a_%7B2n%7D%5C%5C%20%5Cvdots%26%5Cvdots%26%5Cddots%26%5Cvdots%5C%5Ca_%7Bm1%7D%26a_%7Bm2%7D%26...%26a_%7Bmn%7D%5C%5C%0A%5Cend%7Bpmatrix%7D%0A%5Cbegin%7Bpmatrix%7Dx_%7B1%7D%20%5C%5C%20x_%7B2%7D%20%5C%5C%20%5Cvdots%20%5C%5Cx_%7Bn%7D%20%5C%5C%20%5Cend%7Bpmatrix%7D%20%3D%0A%5Cbegin%7Bpmatrix%7Db_%7B1%7D%20%5C%5C%20b_%7B2%7D%20%5C%5C%20%5Cvdots%20%5C%5Cb_%7Bn%7D%20%5C%5C%20%5Cend%7Bpmatrix%7D%0A%5Cend%7Balign*%7D%20%0A">
</div>

### Métodos:
* _Método de Gauss_
* _Método de Gauss-Jordan_
* _Método de Inversión de matrices_
* _Regla de Kramer_
* _Método de Montante_

## Integración Numérica
Dada una función en R² definida en un intervalo [a,b], estamos interesados en calcular:
<div align="center">
<img class="formula" src="https://render.githubusercontent.com/render/math?math=%5CLarge%20Y%20%3D%20%5Cint_%7Ba%7D%5E%7Bb%7D%20f(x)%20dx%0A">
</div>

### Métodos:
* _Introducción_
* _Método del punto medio_
* _Método del trapecio_
* _Regla Simpson_
* _Manejo del error_
