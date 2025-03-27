def cariMahasiswaUangSakuTerkecil(daftar):
    """
    Mencari mahasiswa dengan uang saku terkecil dari daftar mahasiswa.
    Jika ada lebih dari satu mahasiswa dengan uang saku terkecil, semua dikembalikan.
    """
    if not daftar:  # Jika daftar kosong
        return []
    
    # Cari uang saku terkecil
    terkecil = daftar[0][2]
    for mahasiswa in daftar:
        if mahasiswa[2] < terkecil:
            terkecil = mahasiswa[2]
    
    # Cari semua mahasiswa dengan uang saku terkecil
    hasil = [mahasiswa for mahasiswa in daftar if mahasiswa[2] == terkecil]
    return hasil

# Contoh penggunaan
Daftar = [
    ["Ayu", "Surakarta", 250000],
    ["Bagyo", "Sragen", 275000],
    ["Oky", "Klaten", 20000],
    ["Chandra", "Surakarta", 235000],
    ["Dini", "Surakarta", 240000],
    ["Ela", "Boyolali", 245000],
    ["Fani", "Salatiga", 245000],
    ["Gilang", "Klaten", 245000],
    ["Heru", "Karanganyar", 265000],
    ["Ika", "Klaten", 275000],
    ["Joko", "Boyolali", 260000],
    ["Naufal", "Klaten", 20000]
]

# Test fungsi
mahasiswa_terkecil = cariMahasiswaUangSakuTerkecil(Daftar)
print("Mahasiswa dengan uang saku terkecil:")
for mhs in mahasiswa_terkecil:
    print(mhs)