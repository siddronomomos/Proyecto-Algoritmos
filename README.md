# Proyecto de Algoritmos: Análisis de Rutas Óptimas y Árboles de Expansión Mínima en Redes Urbanas

## Descripción

En su proyecto final de clases, ustedes construirán y analizarán un grafo urbano basado en las rutas de una ciudad real utilizando datos obtenidos con la librería `osmnx`. A partir de este grafo, seleccionarán 3 puntos de interés (como intersecciones o ubicaciones específicas) dentro de la ciudad y aplicarán los algoritmos de Dijkstra y Prim para realizar un análisis detallado de rutas óptimas y árboles de expansión mínima.

El objetivo es observar el comportamiento de estos algoritmos en el contexto de redes urbanas y evaluar sus limitaciones, como escalabilidad, precisión y eficiencia, permitiendo reflexionar sobre el impacto de estas técnicas en problemas reales de transporte y redes.

## Objetivos Específicos

- Aplicar el algoritmo de Dijkstra para encontrar rutas óptimas entre puntos de interés seleccionados.
- Implementar el algoritmo de Prim para construir árboles de expansión mínima en el grafo urbano.
- Analizar las limitaciones y el desempeño de ambos algoritmos en términos de eficiencia, escalabilidad y precisión.
- Relacionar los resultados con posibles aplicaciones prácticas en la investigación de redes urbanas y transporte.

## Actividades a Realizar

1. **Construcción del Grafo Urbano**:

   - Selecciona una ciudad real, como "Guadalajara, México", "New York, USA", o cualquier otra de interés.
   - Utiliza la librería `osmnx` para descargar el grafo de rutas urbanas y convertirlo en un grafo donde las aristas estén representadas por las longitudes de las calles.

2. **Aplicación de Algoritmos**:

   - Implementa el algoritmo de Dijkstra para calcular rutas óptimas entre al menos dos pares de nodos seleccionados.
   - Implementa el algoritmo de Prim para obtener el Árbol de Expansión Mínima (MST) del grafo completo.

3. **Visualización**:

   - Usa herramientas de visualización como `matplotlib` o las funciones gráficas de `osmnx` para:
     - Mostrar las rutas calculadas por Dijkstra en el mapa urbano.
     - Representar el MST generado por Prim sobre el grafo.

4. **Análisis de Tiempos de Ejecución**:

   - Mide los tiempos de ejecución de los algoritmos de Dijkstra y Prim en subgrafos de diferentes tamaños.
   - Grafica los resultados obtenidos para analizar cómo varía el tiempo de ejecución según el tamaño del grafo.
     - El eje X representará el número de nodos/aristas del grafo.
     - El eje Y representará el tiempo de ejecución (en segundos).

5. **Análisis Crítico**:

   - Evalúa los algoritmos en términos de:
     - ¿Cómo se comportan al aumentar el número de nodos y aristas?
     - Considera aspectos como cambios dinámicos en los datos de las rutas y la viabilidad de aplicar estos algoritmos en tiempo real.

6. **Reporte**:
   - Redacción de reporte conforme a la guía.

## Entregables

- Código Fuente.
- Resultados Visuales (Gráficas claras).
- Reporte de Análisis.

## Requisitos

- Python 3.x
- Librerías: `osmnx`, `networkx`, `matplotlib`

Puedes instalar las librerías necesarias utilizando pip:

```bash
pip install osmnx networkx matplotlib
```
