import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    prev = [None] * n
    
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

def get_path  