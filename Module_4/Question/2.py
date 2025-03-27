def cariUangSakuTerkecil(daftar):
    """
    Mencari uang saku terkecil dari daftar mahasiswa.
    Mengasumsikan setiap mahasiswa memiliki data: [nama, kota, uang_saku]
    """
    if not daftar:  # Jika daftar kosong
        return None
    
    # Inisialisasi dengan uang saku mahasiswa pertama
    terkecil = daftar[0][2]  # Mengambil uang saku dari data pertama
    
    # Mencari uang saku terkecil
    for mahasiswa in daftar:
        if mahasiswa[2] < terkecil:
            terkecil = mahasiswa[2]
    
    return terkecil

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
    ["Naufal", "Klaten", 10000]
]

# Test fungsi
uang_terkecil = cariUangSakuTerkecil(Daftar)
print(f"Uang saku terkecil adalah: Rp {uang_terkecil}")  