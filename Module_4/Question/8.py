import math
import random

def tebak_angka():
    print("Permainan Tebak Angka")
    
    # Memilih rentang angka
    print("Pilih rentang angka:")
    print("1. 1 sampai 100")
    print("2. 1 sampai 1000")
    pilihan = int(input("Masukkan pilihan (1/2): "))
    
    if pilihan == 1:
        batas_atas = 100
    elif pilihan == 2:
        batas_atas = 1000
    else:
        print("Pilihan tidak valid.")
        return
    
    # Menentukan jumlah tebakan maksimum berdasarkan log2
    max_tebakan = math.ceil(math.log2(batas_atas))
    print(f"Anda memiliki maksimal {max_tebakan} tebakan.")
    
    # Komputer memilih angka secara acak
    angka_rahasia = random.randint(1, batas_atas)
    
    # Memulai permainan
    tebakan = None
    jumlah_tebakan = 0
    
    while jumlah_tebakan < max_tebakan:
        jumlah_tebakan += 1
        try:
            tebakan = int(input(f"Tebakan ke-{jumlah_tebakan}: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        
        if tebakan < angka_rahasia:
            print("Terlalu kecil. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu besar. Coba lagi.")
        else:
            print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar dalam {jumlah_tebakan} tebakan.")
            return
    
    print(f"Maaf, Anda kehabisan tebakan. Angka rahasia adalah {angka_rahasia}.")

# Menjalankan permainan
if __name__ == "__main__":
    tebak_angka()