class Graph(object):
    # Inisialisasi matriks
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size

    # Tambah edge
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Verteks yang sama %d dan %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Hapus edge
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("Tidak terdapat edge antara %d dan %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end="")
            print()

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

g.print_matrix()