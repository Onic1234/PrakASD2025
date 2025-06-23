class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as it is an undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
            
    def dfs(self, verteks_awal):
        visited = [False] * self.V
        self._dfs_util(verteks_awal,visited)
        
    def _dfs_util(self, v, visited):
        visited[v] = True
        print(v, end= '')
        temp = self.graph[v]
        while temp:
            if not visited[temp.vertex]:
                self._dfs_util(temp.vertex, visited)
            temp = temp.next


    def bfs(self, verteks_awal):
        from collections import deque
        visited = [False] * self.V
        queue = deque()
        queue.append(verteks_awal)
        visited[verteks_awal] = True
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            temp = self.graph[v]
            while temp:
                if not visited[temp.vertex]:
                    queue.append(temp.vertex)
                    visited[temp.vertex] = True
                temp = temp.next
                
# Driver program to the above graph class
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(3, 0)

graph.print_graph()

# print("DFS")
# graph.dfs(0)
print("\nBFS")
graph.bfs(0)