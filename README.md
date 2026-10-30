# 🖨️ Analizador de Consumo y Producción — Centro de Impresión 3D

**Proyecto académico de Álgebra Lineal y Sistemas de Ecuaciones**

Herramienta desarrollada en Python para analizar la producción de un centro de impresión 3D mediante matrices, sistemas de ecuaciones lineales y cálculos de ingresos económicos.

---

## 📌 Descripción del proyecto

El programa modela la producción de tres categorías de piezas:

- 🔹 Piezas básicas.
- 🔹 Piezas técnicas.
- 🔹 Piezas avanzadas.

A partir de una matriz de consumo de recursos y un vector de recursos disponibles, se calcula la cantidad de piezas que se pueden producir de cada categoría.

Posteriormente, se estiman los ingresos económicos según el precio de venta de cada tipo de pieza.

## 🎯 Objetivos

- Representar el consumo de recursos mediante matrices.
- Analizar la compatibilidad e invertibilidad de una matriz.
- Resolver un sistema de ecuaciones lineales utilizando la matriz inversa.
- Comprobar los resultados mediante la multiplicación de matrices.
- Calcular los ingresos por categoría y los ingresos totales.

## 🧮 Modelo matemático

### 1. Matriz de consumo

\[
A =
\begin{pmatrix}
3 & 2 & 1\\
1 & 2 & 3\\
2 & 1 & 2
\end{pmatrix}
\]

### 2. Vector de recursos disponibles

\[
B =
\begin{pmatrix}
100\\
80\\
75
\end{pmatrix}
\]

### 3. Sistema de ecuaciones

El modelo se expresa como:

\[
AX=B
\]

Donde:

- \(A\) representa la matriz de consumo.
- \(X\) representa las cantidades de piezas por producir.
- \(B\) representa los recursos disponibles.

La solución se obtiene mediante:

\[
X=A^{-1}B
\]

Como el determinante de la matriz es distinto de cero, existe una solución única.

## ⚙️ Tecnologías utilizadas

- Python 3
- Listas y matrices
- Ciclos y operaciones aritméticas
- Álgebra lineal
- Cálculos financieros

## 🚀 Cómo ejecutar el proyecto

### Requisitos

Tener Python 3 instalado.

### Ejecución

1. Descarga o clona este repositorio.
2. Abre una terminal dentro de la carpeta del proyecto.
3. instala las propiedades de panda para hacer el dashboard en HTML
4. descarga el documento como un .ZIP

```bash
pip install pandas plotly
```

ejecutar el proyecto con este comando desde la terminal:

```bash
python impresion3d.py
```

## 📊 Resultados obtenidos

Con los datos definidos en el programa, los resultados son:

| Categoría | Cantidad calculada | Precio unitario | Ingresos |
|---|---:|---:|---:|
| Piezas básicas | 20 | Q50.00 | Q1,000.00 |
| Piezas técnicas | 15 | Q80.00 | Q1,200.00 |
| Piezas avanzadas | 10 | Q120.00 | Q1,200.00 |
| **Total** | **45** | — | **Q3,400.00** |

Los resultados corresponden al modelo matemático y a los recursos definidos en el código.

## ✅ Validación

El programa realiza una comprobación mediante la operación:

\[
AX=B
\]

Esto permite verificar que las cantidades calculadas satisfacen el sistema de ecuaciones original, salvo posibles diferencias insignificantes debidas a la precisión numérica.

## 📚 Conclusiones

El proyecto demuestra cómo las matrices y los sistemas de ecuaciones lineales pueden utilizarse para modelar un proceso de producción.

La matriz inversa permite calcular las cantidades correspondientes a cada categoría de piezas. Posteriormente, los precios unitarios permiten determinar los ingresos estimados del centro de impresión 3D.

Este modelo constituye una herramienta académica para comprender la relación entre el álgebra lineal, la planificación de recursos y el análisis económico.

---

**Proyecto académico desarrollado en Python.**
