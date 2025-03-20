def is_matrix_consistent(matrix):
    """
    Memastikan bahwa isi dan ukuran matriks konsisten.
    """
    if not matrix or not isinstance(matrix, list):
        return False
    row_length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != row_length:
            return False
    return True

def matrix_size(matrix):
    """
    Mengambil ukuran matriks.
    """
    if not is_matrix_consistent(matrix):
        raise ValueError("Matriks tidak konsisten")
    return len(matrix), len(matrix[0])

def add_matrices(matrix1, matrix2):
    """
    Menambahkan dua matriks (pastikan ukurannya sama).
    """
    if not (is_matrix_consistent(matrix1) and is_matrix_consistent(matrix2)):
        raise ValueError("Salah satu atau kedua matriks tidak konsisten")
    
    rows1, cols1 = matrix_size(matrix1)
    rows2, cols2 = matrix_size(matrix2)
    
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Ukuran matriks tidak sama")
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def multiply_matrices(matrix1, matrix2):
    """
    Mengalikan dua matriks (pastikan ukurannya sesuai).
    """
    if not (is_matrix_consistent(matrix1) and is_matrix_consistent(matrix2)):
        raise ValueError("Salah satu atau kedua matriks tidak konsisten")
    
    rows1, cols1 = matrix_size(matrix1)
    rows2, cols2 = matrix_size(matrix2)
    
    if cols1 != rows2:
        raise ValueError("Ukuran matriks tidak sesuai untuk perkalian")
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def determinant(matrix):
    """
    Menghitung determinan dari matriks persegi.
    """
    if not is_matrix_consistent(matrix):
        raise ValueError("Matriks tidak konsisten")
    
    rows, cols = matrix_size(matrix)
    
    if rows != cols:
        raise ValueError("Matriks bukan persegi")
    
    if rows == 1:
        return matrix[0][0]
    
    if rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(cols):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    
    return det

# Contoh penggunaan
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Penjumlahan Matriks:", add_matrices(matrix1, matrix2))
print("Perkalian Matriks:", multiply_matrices(matrix1, matrix2))
print("Determinan Matriks 1:", determinant(matrix1))