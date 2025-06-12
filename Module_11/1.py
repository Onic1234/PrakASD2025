import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    prev = [None] * n  # Untuk menyimpan jalur terpendek

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor in range(n):
            if graph[current_node][neighbor] != 0:
                distance = current_distance + graph[current_node][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    prev[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
    return distances, prev

def get_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]

# Matriks adjacency sesuai graf pada gambar
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],  # 0
    [4, 0, 8, 0, 0, 0, 0, 11, 0], # 1
    [0, 8, 0, 7, 0, 4, 0, 0, 2],  # 2
    [0, 0, 7, 0, 9, 14, 0, 0, 0], # 3
    [0, 0, 0, 9, 0, 10, 0, 0, 0], # 4
    [0, 0, 4, 14, 10, 0, 2, 0, 0],# 5
    [0, 0, 0, 0, 0, 2, 0, 1, 6],  # 6
    [8, 11, 0, 0, 0, 0, 1, 0, 7], # 7
    [0, 0, 2, 0, 0, 0, 6, 7, 0]   # 8
]

start_node = 0
end_node = 4

distances, prev = dijkstra(graph, start_node)
path = get_path(prev, end_node)

print(f"Jarak terpendek dari node {start_node} ke node {end_node}: {distances[end_node]}")
print(f"Jalur terpendek: {path}")