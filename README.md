<img src="https://www.eii.ulpgc.es/sites/default/files/eii-acron-mod.png" alt="EII-ULPGC" align="right" width="516" height="150" />

# PRÁCTICA 1 DE FSI
> Búsqueda de rutas por la red de carreteras de Rumanía

El siguiente repositorio tiene como objetivo la implementación de cuatro algoritmos de búsqueda no informada, utilizados para recorrer o buscar elementos ponderados en un grafo. Para ello, haremos uso de un grafo que representa la red de carreteras de Rumanía.

## Módulos
El proyecto consta de tres módulos principales:
- [utils.py](https://github.com/imanolqb/Practica1_FSI_ImanolQB_CarlosAR/blob/master/code/utils.py) : en este módulo se crean los métodos para las pilas LIFO y colas FIFO que usaremos para los algoritmos de búsqueda en anchura (BFS), en profundidad (DFS) y acotación y ramificación (Branch & Bound). En definitiva, cómo logramos extraer y extender en las listas a medida que generamos nodos.
- [search.py](https://github.com/imanolqb/Practica1_FSI_ImanolQB_CarlosAR/blob/master/code/search.py) : aquí se encuentra el algoritmo, que hará uso de todos los métodos contenidos en [utils.py](https://github.com/imanolqb/Practica1_FSI_ImanolQB_CarlosAR/blob/master/code/utils.py). También aquí, se hallan definidos los valores de las diferentes ciudades y las clases ***Problem*** y ***Node***.
- [run.py](https://github.com/imanolqb/Practica1_FSI_ImanolQB_CarlosAR/blob/master/code/run.py) : programa principal. Se ponen en marcha los programas de búsqueda, que se muestran como salida. Para realizar búsquedas con cada uno de los distintos algoritmos de búsqueda, ya sea BFS, DFS o Branch & Bound con y sin heurística, debemos definir en este módulo el problema, desde dónde queremos empezar hasta dónde queremos llegar, y que viene dado, en el módulo [search.py](https://github.com/imanolqb/Practica1_FSI_ImanolQB_CarlosAR/blob/master/code/search.py), por GPSProblem, sus atributos ***initial*** (nodo inicial) y ***goal*** (nodo objetivo), y los métodos ***sucessor*** (nodos hijo del padre), ***path_cost*** (coste desde el nodo inicial hasta el nodo actual) y ***h***, que define la heurística.

## Resultados esperados y obtenidos
> Resultados esperados

|  ID  |  Origen  |  Destino  |   Amplitud   |   Profundidad   |   Ramificación y acotación | Ramificación y acotación con subestimación |
|:----:|:--------:|:---------:|:------------:|:---------------:|:--------------------------:|:------------------------------------------:|
| 1 |Arad|Bucharest|**Generados**: 21 <br> **Visitados**: 16 <br> **Costo total**: 450 <br> **Ruta**:[\<Node B>,\<Node F>,\<Node S>,\<Node A>]|**Generados**: 18 <br> **Visitados**: 10 <br> **Costo total**: 733 <br> **Ruta**:[\<Node B>,\<Node P>,\<Node C>,\<Node D>,\<Node M>,\<Node L>,\<Node T>,\<Node A>]|**Generados**: 31 <br> **Visitados**: 24 <br> **Costo total**: 418 <br> **Ruta**:\[<Node B>, \<Node P>, \<Node R>, \<Node S>, \<Node A>]|**Generados**: 16 <br> **Visitados**: 6 <br> **Costo total**: 418 <br> **Ruta**:[\<Node B>, \<Node P>, \<Node R>, \<Node S>, \<Node A>]|
| 2 |Oradea|Eforie|**Generados**: 45 <br> **Visitados**: 43 <br> **Costo total**: 730 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node F>, \<Node S>, \<Node O>]|**Generados**: 41 <br> **Visitados**: 31 <br> **Costo total**: 698 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node P>, \<Node R>, \<Node S>, \<Node O>]|**Generados**: 43 <br> **Visitados**: 40 <br> **Costo total**: 698 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node P>, \<Node R>, \<Node S>, \<Node O>]|**Generados**: 32 <br> **Visitados**: 15 <br> **Costo total**: 698 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node P>, \<Node R>, \<Node S>, \<Node O>]|
| 3 |Giurgiu|Zerind|**Generados**: 41 <br> **Visitados**: 34 <br> **Costo total**: 615 <br> **Ruta**:[\<Node Z>, \<Node A>, \<Node S>, \<Node F>, \<Node B>, \<Node G>]|**Generados**: 45 <br> **Visitados**: 43 <br> **Costo total**: 730 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node F>, \<Node S>, \<Node O>]|**Generados**: 45 <br> **Visitados**: 43 <br> **Costo total**: 730 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node F>, \<Node S>, \<Node O>]|**Generados**: 45 <br> **Visitados**: 43 <br> **Costo total**: 730 <br> **Ruta**:[\<Node E>, \<Node H>, \<Node U>, \<Node B>, \<Node F>, \<Node S>, \<Node O>]|
| 4 |Neamt|Dobreta|3|4|5|6|
| 5 |Mehadia|Fagaras|3|4|5|6|
