# 1. Buatlah suatu program untuk mengurutkan array mahasiswa berdasarkan NIM, yang elemennya terbuat dari class MhsTIF, yang telah kamu buat sebelumnya.
class MhsTIF:
    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        
    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Prodi: {self.prodi}"
    
    def __repr__(self):
        return f"MhsTIF({self.nim}, '{self.nama}', '{self.prodi}')"
    
def urutkan_mahasiswa(mahasiswa_list):
    return sorted(mahasiswa_list, key=lambda m: m.nim)

mahasiswa_list = [
    MhsTIF("L200234230", "Andi", "TI"),
    MhsTIF("L200234291", "Budi", "TI"),
    MhsTIF("L200234275", "Tino", "TI"),
    MhsTIF("L200234276", "Budi", "TI"),
    MhsTIF("L200234277", "Siti", "TI")
]      
print("Sebelum diurutkan:", mahasiswa_list)
mahasiswa_list = urutkan_mahasiswa(mahasiswa_list)
print("Setelah diurutkan:", mahasiswa_list)



# Misal terdapat dua buah array yang sudah urut A dan B. Buatlah suatu program untukmenggabungkan, secara efisien, kedua array itu menjadi suatu array C yang urut.
def gabungkan_array_urut(A, B):
    C = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C.extend(A[i:])
    C.extend(B[j:])
    return C

# Contoh penggunaan
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
print("Array A:", A)
print("Array B:", B)
C = gabungkan_array_urut(A, B)
print("Array C (gabungan):", C)

# 3. Membandingkan waktu bubble sort, selection sort, dan insertion sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


from time import time as detak
from random import shuffle as kocok
# Membandingkan waktu eksekusi
k = list(range(1, 6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); bubbleSort(u_bub); ak = detak(); print('bubble: %g detik' % (ak-aw))
aw = detak(); selectionSort(u_sel); ak = detak(); print('selection: %g detik' % (ak-aw))
aw = detak(); insertionSort(u_ins); ak = detak(); print('insertion: %g detik' % (ak-aw))
    