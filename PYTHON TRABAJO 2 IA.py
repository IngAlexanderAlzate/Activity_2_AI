import networkx as nx

# Crear un grafo
G = nx.Graph()

# Agregar rutas (aristas) con pesos (distancias)
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('B', 'D', weight=3)

# Función para encontrar la mejor ruta
def mejor_ruta(grafo, inicio, fin):
    try:
        ruta = nx.shortest_path(grafo, source=inicio, target=fin, weight='weight')
        distancia = nx.shortest_path_length(grafo, source=inicio, target=fin, weight='weight')
        return ruta, distancia
    except nx.NetworkXNoPath:
        return None, float('inf')

# Ejecutar la función
if __name__ == "__main__":
    punto_a = 'A'
    punto_b = 'D'
    ruta, distancia = mejor_ruta(G, punto_a, punto_b)
    if ruta:
        print(f"La mejor ruta de {punto_a} a {punto_b} es: {ruta} con una distancia de {distancia}.")
    else:
        print(f"No hay ruta disponible de {punto_a} a {punto_b}.")