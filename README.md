# Descripción del Proyecto

Este repositorio contiene el código y los recursos asociados con un proyecto académico para la asignatura de Sistemas Inteligentes. El objetivo del proyecto es encontrar rutas óptimas que partan de un lugar específico en una ciudad y visiten, sin un orden establecido, un conjunto de puntos de interés. El proyecto utiliza un archivo de OpenStreetMap en formato XML y GraphML para leer el archivo XML generado.

## Contenido del Repositorio

-   **src/**: Contiene el código fuente del proyecto.
-   **grafos/**: Almacena los archivos de OpenStreetMap en formato XML.
-   **resultados/**: Resultados obtenidos durante la ejecución del proyecto.
-   **graph/**: Clases para el manejo de grafos.

## Problema del Laboratorio

### Definición del Problema

El problema consiste en encontrar rutas óptimas en un grafo que representa la red de calles de una ciudad. Se parte de un nodo específico en el grafo y se deben visitar, sin un orden predefinido, un conjunto de puntos de interés.

### Especificaciones del Problema

-   **Espacio de Estado**: Estados + Acciones.
-   **Estado Inicial**: Nodo del grafo correspondiente al punto de partida.
-   **Función Objetivo**: Visitar todos los puntos de interés.

## Estrategias de Búsqueda

Para recorrer el grafo y encontrar la mejor ruta posible, se han implementado diversas estrategias de búsqueda, incluyendo:

-   Búsqueda en Profundidad.
-   Búsqueda en Anchura.
-   Costo Uniforme.
-   A* (A estrella).
-   Búsqueda Voraz.

## Heurísticas

Además, el proyecto incorpora dos tipos de heurísticas:

1.  **Euclidiana**: Calcula la distancia euclidiana entre dos puntos en el plano.
2.  **Arco Mínimo**: Utiliza la longitud del arco mínimo para estimar la distancia entre dos puntos.
