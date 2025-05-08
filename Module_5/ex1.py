def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

k = [1, 2, 3, 4, 5]
swap(k, 0, 4)
print(k) 

def cariPosisiYangTerkecil(A, darisini, sampaiSini):
    posisiTerkecil = darisini
    for i in range(darisini+1, sampaiSini+1):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

A = [5, 4, 3, 2, 1]
j = cariPosisiYangTerkecil(A, 0, len(A)-1)
print("Posisi terkecil dari A[0] sampai A[4] adalah A[{}]".format(j))

def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                swap(A, j, j+1)
    return A

A = [5, 4, 3, 2, 1]
print("Sebelum diurutkan:", A)
A = bubbleSort(A)
print("Setelah diurutkan:", A)

def selectionSort(B):
    n = len(B)
    for i in range(n-1):
        posisiTerkecil = cariPosisiYangTerkecil(B, i, n)
        swap(B, i, posisiTerkecil)
    return B

B = [5, 4, 3, 2, 1]
print("Sebelum diurutkan:", B)
B = selectionSort(B)
print("Setelah diurutkan:", B)

def insertionSort(C):
    n = len(C)
    for i in range(1, n):
        key = C[i]
        pos = i
        while pos > 0 and C[pos-1] > key:
            C[pos] = C[pos-1]
            pos -= 1
        C[pos] = key
    return C    


C = [5, 4, 3, 2, 1]
C = insertionSort(C)
print("Setelah diurutkan:", C)