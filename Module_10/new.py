class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data  # Menyimpan data pada simpul
        self.kiri = None  # Link ke anak kiri, awalnya kosong
        self.kanan = None # Link ke anak kanan, awalnya kosong


# --- Fungsi untuk Soal Nomor 6 ---
def ukuranPohon(akar):
    """Menghitung dan mengembalikan jumlah total simpul (ukuran) dari pohon."""
    if akar is None:
        return 0
    else:
        # Ukuran adalah 1 (simpul saat ini) + ukuran sub-pohon kiri + ukuran sub-pohon kanan
        return 1 + ukuranPohon(akar.kiri) + ukuranPohon(akar.kanan)

# --- Fungsi untuk Soal Nomor 7 ---
def tinggiPohon(akar):
    """Menghitung dan mengembalikan tinggi (jumlah level) dari pohon."""
    if akar is None:
        return 0
    else:
        # Tinggi adalah 1 (level saat ini) + tinggi maksimum dari sub-pohon kiri atau kanan
        tinggi_kiri = tinggiPohon(akar.kiri)
        tinggi_kanan = tinggiPohon(akar.kanan)
        return 1 + max(tinggi_kiri, tinggi_kanan)

# --- Fungsi untuk Soal Nomor 8 ---
def cetakDataDanLevel(akar):
    """Fungsi utama untuk mencetak data dan level setiap simpul."""
    # Memanggil fungsi pembantu rekursif dengan level awal 0
    _cetakDataDanLevelBantu(akar, 0)

def _cetakDataDanLevelBantu(subpohon, level):
    """Fungsi pembantu yang melakukan penelusuran preorder secara rekursif."""
    if subpohon is not None:
        # 1. Kunjungi simpul (cetak data dan levelnya)
        print(subpohon.data, ", level", level)
        # 2. Telusuri sub-pohon kiri di level berikutnya
        _cetakDataDanLevelBantu(subpohon.kiri, level + 1)
        # 3. Telusuri sub-pohon kanan di level berikutnya
        _cetakDataDanLevelBantu(subpohon.kanan, level + 1)
        
if __name__ == "__main__":
    
    # --- Membuat Pohon Contoh ---
    # Struktur pohon ini dibuat sama persis dengan contoh pada halaman 121 di buku. 
    print("Membangun pohon dari contoh buku...")
    A = _SimpulPohonBiner('Ambarawa') 
    B = _SimpulPohonBiner('Bantul')
    C = _SimpulPohonBiner('Cimahi')
    D = _SimpulPohonBiner('Denpasar') 
    E = _SimpulPohonBiner('Enrekang') 
    F = _SimpulPohonBiner('Flores')
    G = _SimpulPohonBiner('Garut')
    H = _SimpulPohonBiner('Halmahera Timur') 
    I = _SimpulPohonBiner('Indramayu')
    
    # Menghubungkan simpul-simpul sesuai struktur pohon di buku 
    A.kiri = B; A.kanan = C
    B.kiri = D; B.kanan = E
    C.kiri = F; C.kanan = G 
    E.kiri = H
    G.kanan = I
    print("Pohon berhasil dibuat.\n")

    # --- Memanggil Fungsi dan Menampilkan Hasil ---
    
    # Memanggil fungsi ukuranPohon
    ukuran = ukuranPohon(A)
    print("--- Hasil Soal 6: Ukuran Pohon ---")
    print("Ukuran pohon adalah:", ukuran, "simpul\n")

    # Memanggil fungsi tinggiPohon
    tinggi = tinggiPohon(A)
    print("--- Hasil Soal 7: Tinggi Pohon ---")
    print("Tinggi pohon adalah:", tinggi, "level\n")
    
    # Memanggil fungsi cetakDataDanLevel
    print("--- Hasil Soal 8: Cetak Data dan Level (Preorder) ---")
    cetakDataDanLevel(A)