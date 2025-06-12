# %%
# Greedy TSP untuk graf pada gambar (H1=0, H2=1, ..., H8=7)

def greedy_tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    path = [start]
    total_cost = 0
    current = start
    visited[current] = True

    for _ in range(n - 1):
        next_node = None
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and 0 < graph[current][j] < min_dist:
                min_dist = graph[current][j]
                next_node = j
        if next_node is not None:
            path.append(next_node)
            total_cost += min_dist
            visited[next_node] = True
            current = next_node

    # Kembali ke titik awal
    if graph[current][start] > 0:
        path.append(start)
        total_cost += graph[current][start]
    else:
        # Tidak bisa kembali ke awal (bukan siklus Hamiltonian)
        return path, float('inf')

    return path, total_cost

# Matriks adjacency sesuai gambar
graph = [
    # H1 H2 H3 H4 H5 H6 H7 H8
    [ 0, 5, 0, 6, 8, 4, 0, 7],  # H1
    [ 5, 0, 2, 4, 3, 0, 0, 0],  # H2
    [ 0, 2, 0, 1, 0, 0, 0, 0],  # H3
    [ 6, 4, 1, 0, 7, 0, 0, 0],  # H4
    [ 8, 3, 0, 7, 0, 0, 6, 4],  # H5
    [ 4, 0, 0, 0, 0, 0, 3, 0],  # H6
    [ 0, 0, 0, 0, 6, 3, 0, 2],  # H7
    [ 7, 0, 0, 0, 4, 0, 2, 0]   # H8
]

start_node = 0  # H1
path, cost = greedy_tsp(graph, start_node)

node_names = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
path_names = [node_names[i] for i in path]

print(f"Greedy TSP dari {node_names[start_node]}:")
print(f"Jalur: {' -> '.join(path_names)}")
print(f"Total jarak: {cost}")