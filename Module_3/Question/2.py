def buatNol(m, n=None):
    """
    Menghasilkan matriks yang berisi semua nol.
    Jika hanya satu argumen diberikan, menghasilkan matriks persegi m x m.
    """
    if n is None:
        n = m
    return [[0 for _ in range(n)] for _ in range(m)]

def buatIdentitas(m):
    """
    Menghasilkan matriks identitas berukuran m x m.
    """
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

# Contoh penggunaan
print("Matriks Nol 3x3:")
print(buatNol(3))
print("\nMatriks Nol 2x4:")
print(buatNol(2, 4))
print("\nMatriks Identitas 3x3:")
print(buatIdentitas(3))