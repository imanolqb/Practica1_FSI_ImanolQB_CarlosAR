# Search methods

import search
import time

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

# print(str(search.breadth_first_graph_search(ab).path()))
# search.breadth_first_graph_search(ab).path()

print("\n")
titulo = "---------------ID 1 --> Arad to Bucharest---------------"
print(titulo)
ab = search.GPSProblem('A', 'B',
                       search.romania)
print("--AMPLITUD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.breadth_first_graph_search(ab).path()))
print("Tiempo de ejecución del algoritmo de amplitud: " + str(time.time() - initial_time))
print("--PROFUNDIDAD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.depth_first_graph_search(ab).path()))
print("Tiempo de ejecución del algoritmo de profundidad: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound(ab).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound_with_heuristic(ab).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación con subestimación: " +
      str(time.time() - initial_time) + "\n\n")


titulo = "---------------ID 2 --> Oradea to Eforie---------------"
print(titulo)
oe = search.GPSProblem('O', 'E',
                       search.romania)
print("--AMPLITUD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.breadth_first_graph_search(oe).path()))
print("Tiempo de ejecución del algoritmo de amplitud: " + str(time.time() - initial_time))
print("--PROFUNDIDAD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.depth_first_graph_search(oe).path()))
print("Tiempo de ejecución del algoritmo de profundidad: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound(oe).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound_with_heuristic(oe).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación con subestimación: " +
      str(time.time() - initial_time) + "\n\n")

titulo = "---------------ID 3 --> Giurgiu to Zerind---------------"
print(titulo)
gz = search.GPSProblem('G', 'Z',
                       search.romania)
print("--AMPLITUD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.breadth_first_graph_search(gz).path()))
print("Tiempo de ejecución del algoritmo de amplitud: " + str(time.time() - initial_time))
print("--PROFUNDIDAD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.depth_first_graph_search(gz).path()))
print("Tiempo de ejecución del algoritmo de profundidad: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound(gz).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound_with_heuristic(gz).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación con subestimación: " +
      str(time.time() - initial_time) + "\n\n")

titulo = "---------------ID 4 --> Neamt to Dobreta---------------"
print(titulo)
nd = search.GPSProblem('N', 'D',
                       search.romania)
print("--AMPLITUD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.breadth_first_graph_search(nd).path()))
print("Tiempo de ejecución del algoritmo de amplitud: " + str(time.time() - initial_time))
print("--PROFUNDIDAD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.depth_first_graph_search(nd).path()))
print("Tiempo de ejecución del algoritmo de profundidad: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound(nd).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound_with_heuristic(nd).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación con subestimación: " +
      str(time.time() - initial_time) + "\n\n")

titulo = "---------------ID 5 --> Mehadia to Faragas---------------"
print(titulo)
mf = search.GPSProblem('M', 'F',
                       search.romania)
print("--AMPLITUD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.breadth_first_graph_search(mf).path()))
print("Tiempo de ejecución del algoritmo de amplitud: " + str(time.time() - initial_time))
print("--PROFUNDIDAD--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.depth_first_graph_search(mf).path()))
print("Tiempo de ejecución del algoritmo de profundidad: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound(mf).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación: " + str(time.time() - initial_time))
print("--RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN--".center(len(titulo)))
initial_time = time.time()
print("Ruta: \t\t\t\t" + str(search.branch_and_bound_with_heuristic(mf).path()))
print("Tiempo de ejecución del algoritmo de ramificación y acotación con subestimación: " +
      str(time.time() - initial_time) + "\n\n")
