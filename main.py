import osmnx as ox
import networkx as nx
import time

def construir_grafo_urbano(ciudad):
    # Descargar el grafo de la ciudad
    G = ox.graph_from_place(ciudad, network_type='drive')
    return G

def aplicar_dijkstra(G, origen, destino):
    # Calcular la ruta óptima usando Dijkstra
    ruta = nx.shortest_path(G, source=origen, target=destino, weight='length', method='dijkstra')
    return ruta

def aplicar_prim(G):
    # Convertir el grafo dirigido a no dirigido
    G_undirected = G.to_undirected()
    # Calcular el Árbol de Expansión Mínima usando Prim
    mst = nx.minimum_spanning_tree(G_undirected, weight='length', algorithm='prim')
    return mst

def visualizar_ruta(G, ruta):
    # Visualizar la ruta en el grafo
    ox.plot_graph_route(G, ruta, route_linewidth=6, node_size=0, bgcolor='k')

def visualizar_mst(mst):
    # Visualizar el MST en el grafo
    fig, ax = ox.plot_graph(mst, node_size=0, bgcolor='k')
    return fig, ax

def medir_tiempos_ejecucion(G, origen, destino):
    # Medir el tiempo de ejecución de Dijkstra
    start_time = time.time()
    aplicar_dijkstra(G, origen, destino)
    dijkstra_time = time.time() - start_time

    # Medir el tiempo de ejecución de Prim
    start_time = time.time()
    aplicar_prim(G)
    prim_time = time.time() - start_time

    return dijkstra_time, prim_time

def main():
    ciudad = "G, Mexico"
    G = construir_grafo_urbano(ciudad)

    # Seleccionar nodos de interés
    origen = list(G.nodes())[0]
    destino = list(G.nodes())[1]

    # Aplicar y visualizar Dijkstra
    ruta = aplicar_dijkstra(G, origen, destino)
    visualizar_ruta(G, ruta)

    # Aplicar y visualizar Prim
    mst = aplicar_prim(G)
    visualizar_mst(mst)

    # Medir tiempos de ejecución
    dijkstra_time, prim_time = medir_tiempos_ejecucion(G, origen, destino)
    print(f"Tiempo de ejecución de Dijkstra: {dijkstra_time} segundos")
    print(f"Tiempo de ejecución de Prim: {prim_time} segundos")

if __name__ == "__main__":
    main()