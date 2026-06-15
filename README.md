# Sistema de Gestión de Países 

# Descripción 

Este programa fue desarrollado en Python y permite gestionar información de países almacenada en un archivo CSV.

El sistema funciona mediante un menú interactivo en consola que permite consultar, agregar, actualizar, ordenar y filtrar países según distintos criterios que el usuario puede seleccionar.

Los datos se almacenan de forma permanente en el archivo "paises.csv".

______________________________

# Objetivo

Desarrollar una aplicación que permita administrar información básica de distintos países utilizando estructuras de datos, modularización y persistencia de datos mediante archivos CSV.

# Archivos

- **menu_main.py**
  - Contiene el menú principal y el flujo general del programa.

- **funciones_principales.py**
  - Contiene las funcionalidades principales del sistema.

- **funciones_secundarias.py**
  - Contiene funciones auxiliares y validaciones.

- **paises.csv**
  - Archivo donde se almacenan los datos de los países.

______________________________

# Funcionalidades

# 1. Mostrar país

Permite buscar un país por nombre.

- Coincidencia exacta.
- Coincidencia parcial.

# 2. Agregar país

Permite agregar un nuevo país indicando:

- Nombre
- Población
- Superficie
- Continente

Los datos se guardan tanto en memoria como en el archivo CSV.

# 3. Mostrar estadísticas

Muestra:

- País con mayor población.
- País con menor población.
- Promedio de población.
- Promedio de superficie.
- Cantidad de países por continente.

# 4. Ordenar países

Permite ordenar por:

- Nombre
- Población
- Superficie

En orden:

- Ascendente
- Descendente

# 5. Filtrar países

Permite filtrar por:

- Continente
- Rango de población
- Rango de superficie

# 6. Actualizar país

Permite modificar:

- Continente
- Población
- Superficie

Los cambios se guardan en el archivo CSV.

# 7. Salir

Finaliza la ejecución del programa.

______________________________

# Estructura de Datos

La información de cada país se almacena mediante diccionarios, y todos los diccionarios se almacenan en una lista

Ejemplo:

{
    "nombre": "Argentina",
    "poblacion": 47000000,
    "superficie": 2780400,
    "continente": "America"
}

______________________________

# Ejemplo de Uso de la opción 1 (Mostrar país)

-Entrada

-> Ingresar el nombre del país: Argentina


-Salida

-> País: Argentina | Población: 47000000 | Superficie: 2780400 | Continente: America

______________________________

# Dataset

El archivo "paises.csv" contiene inicialmente dos países de ejemplo.

El usuario puede completar el resto de los registros utilizando la opción de agregar países disponible en el menú.

______________________________

# Integrantes

Facundo Nahuel Leiva


Links: 

Video: https://youtu.be/8iiPxyAjZ8g

Pdf : https://docs.google.com/document/d/e/2PACX-1vRmIondz4Z7uFuL9L1wX6njdpcEOkTQz_YEyLhVUyqMl1WR2BFursqQ8SPRBjx-nisr54xvulMPAOiE/pub
