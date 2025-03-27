def cariMahasiswaUangSakuKurang(daftar, batas):
    """
    Mencari semua mahasiswa dengan uang saku kurang dari batas tertentu.
    """
    hasil = [mahasiswa for mahasiswa in daftar if mahasiswa[2] < batas]
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
mahasiswa_kurang = cariMahasiswaUangSakuKurang(Daftar, 250000)
print("Mahasiswa dengan uang saku kurang dari 250000:")
for mhs in mahasiswa_kurang:
    print(mhs)