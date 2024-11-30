import osmnx as ox
import random
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time

ciudad = "Guadalajara, Mexico"
G = ox.graph_from_place(ciudad, network_type="drive")

for edge in G.edges:
    maxspeed = 40
    if "maxspeed" in G.edges[edge]:
        maxspeed = G.edges[edge]["maxspeed"]
        if type(maxspeed) == list:
            speeds = [int(speed) for speed in maxspeed]
            maxspeed = min(speeds)
        elif type(maxspeed) == str:
            maxspeed = int(maxspeed)
    G.edges[edge]["maxspeed"] = maxspeed
    G.edges[edge]["weight"] = G.edges[edge]["length"] / maxspeed

def estilo_arista_no_visitada(edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def estilo_arista_visitada(edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def estilo_arista_activa(edge):
    G.edges[edge]["color"] = '#e8a900'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def estilo_arista_camino(edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def graficar_grafo():
    ox.plot_graph(
        G,
        node_size=[G.nodes[node]["size"] for node in G.nodes],
        edge_color=[G.edges[edge]["color"] for edge in G.edges],
        edge_alpha=[G.edges[edge]["alpha"] for edge in G.edges],
        edge_linewidth=[G.edges[edge]["linewidth"] for edge in G.edges],
        node_color="white",
        bgcolor="#18080e"
    )

def dijkstra(origen, destino, graficar=False):
    for node in G.nodes:
        G.nodes[node]["visited"] = False
        G.nodes[node]["distance"] = float("inf")
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
    for edge in G.edges:
        estilo_arista_no_visitada(edge)
    G.nodes[origen]["distance"] = 0
    G.nodes[origen]["size"] = 50
    G.nodes[destino]["size"] = 50
    pq = [(0, origen)]
    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == destino:
            if graficar:
                print("Iteraciones:", step)
                graficar_grafo()
            return
        if G.nodes[node]["visited"]: continue
        G.nodes[node]["visited"] = True
        for edge in G.out_edges(node):
            estilo_arista_visitada((edge[0], edge[1], 0))
            neighbor = edge[1]
            weight = G.edges[(edge[0], edge[1], 0)]["weight"]
            if G.nodes[neighbor]["distance"] > G.nodes[node]["distance"] + weight:
                G.nodes[neighbor]["distance"] = G.nodes[node]["distance"] + weight
                G.nodes[neighbor]["previous"] = node
                heapq.heappush(pq, (G.nodes[neighbor]["distance"], neighbor))
                for edge2 in G.out_edges(neighbor):
                    estilo_arista_activa((edge2[0], edge2[1], 0))
        step += 1

def distancia(nodo1, nodo2):
    x1, y1 = G.nodes[nodo1]["x"], G.nodes[nodo2]["y"]
    x2, y2 = G.nodes[nodo2]["x"], G.nodes[nodo2]["y"]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def reconstruir_camino(origen, destino, graficar=False, algoritmo=None):
    for edge in G.edges:
        estilo_arista_no_visitada(edge)
    dist = 0
    velocidades = []
    curr = destino
    while curr != origen:
        prev = G.nodes[curr]["previous"]
        if prev is None:
            raise ValueError(f"No se encontró un camino de {origen} a {destino}")
        dist += G.edges[(prev, curr, 0)]["length"]
        velocidades.append(G.edges[(prev, curr, 0)]["maxspeed"])
        estilo_arista_camino((prev, curr, 0))
        if algoritmo:
            G.edges[(prev, curr, 0)][f"{algoritmo}_uses"] = G.edges[(prev, curr, 0)].get(f"{algoritmo}_uses", 0) + 1
        curr = prev
    dist /= 1000
    if graficar:
        print(f"Distancia: {dist}")
        print(f"Velocidad promedio: {sum(velocidades)/len(velocidades)}")
        print(f"Tiempo total: {dist/(sum(velocidades)/len(velocidades)) * 60}")
        graficar_grafo()

puntos_interes = random.sample(list(G.nodes), 3)

for i in range(2):
    origen, destino = puntos_interes[i], puntos_interes[i+1]
    dijkstra(origen, destino, graficar=True)
    reconstruir_camino(origen, destino, graficar=True, algoritmo="dijkstra")

def medir_tiempos_ejecucion(G, origen, destino):
    start_time = time.time()
    dijkstra(origen, destino)
    dijkstra_time = time.time() - start_time
    return dijkstra_time

nodos = list(G.nodes)
subgrafos = [G.subgraph(nodos[:i]) for i in range(100, len(nodos), 100)]
tiempos_dijkstra = []

for subgrafo in subgrafos:
    origen, destino = random.sample(list(subgrafo.nodes), 2)
    dijkstra_time = medir_tiempos_ejecucion(subgrafo, origen, destino)
    tiempos_dijkstra.append(dijkstra_time)

plt.plot(range(100, len(nodos), 100), tiempos_dijkstra, label="Dijkstra")
plt.xlabel("Número de nodos/aristas")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.show()

def prim_mst(G):
    mst = nx.Graph()
    visited = set()
    edges = [(0, list(G.nodes)[0], None)]
    while edges:
        weight, node, prev = heapq.heappop(edges)
        if node not in visited:
            visited.add(node)
            if prev is not None:
                mst.add_edge(prev, node, weight=weight)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    heapq.heappush(edges, (G.edges[node, neighbor, 0]['weight'], neighbor, node))
    return mst

mst = prim_mst(G)

def graficar_mst(mst):
    pos = {node: (G.nodes[node]['x'], G.nodes[node]['y']) for node in mst.nodes}
    edge_colors = ['white' for _ in mst.edges]
    edge_widths = [1 for _ in mst.edges]
    node_colors = ['orange' for _ in mst.nodes]
    plt.figure(figsize=(10, 10))
    nx.draw(mst, pos, edge_color=edge_colors, width=edge_widths, node_color=node_colors, with_labels=False, node_size=10)
    for edge in mst.edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        plt.plot([x0, x1], [y0, y1], 'black')
    plt.show()

graficar_mst(mst)