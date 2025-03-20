def cariSemuaIndex(x, data):
    """
    Mencari semua index yang mengandung nilai x dalam data.
    Mengembalikan list berisi index-index tersebut.
    Jika tidak ditemukan, mengembalikan list kosong.
    """
    hasil = []
    for i in range(len(data)):
        if data[i] == x:
            hasil.append(i)
    return hasil

# Contoh penggunaan
Daftar = [
    ["Ayu", "Surakarta"], 
    ["Bagyo", "Sragen"],
    ["Chandra", "Surakarta"],
    ["Dini", "Surakarta"],
    ["Ela", "Boyolali"],
    ["Fani", "Salatiga"],
    ["Gilang", "Klaten"],
    ["Heru", "Karanganyar"],
    ["Ika", "Klaten"],
    ["Joko", "Boyolali"]
]

def cariKota(kota, data):
    """
    Mencari semua index mahasiswa yang berasal dari kota tertentu.
    """
    return cariSemuaIndex(kota, [mhs[1] for mhs in data])

# Test fungsi
print(cariKota("Klaten", Daftar))  # Output: [6, 8]
print(cariKota("Jakarta", Daftar))  # Output: []
print(cariKota("Surakarta", Daftar))  # Output: [0, 2, 3]