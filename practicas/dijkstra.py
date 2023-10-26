import sys

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    vertices = list(graph)

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight

            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route

    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'D': 3, 'E': 2},
        'D': {'E': 8},
        'E': {}
    }

    start_vertex = 'A'
    result = dijkstra(graph, start_vertex)

    for vertex, distance in result.items():
        print(f'Shortest distance from {start_vertex} to {vertex} is {distance}')
