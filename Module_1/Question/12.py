import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0

    print("Permainan tebak angka.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")

    while tebakan != angka_rahasia:
        jumlah_tebakan += 1
        tebakan = int(input(f"Masukkan tebakan ke-{jumlah_tebakan}:> "))

        if tebakan < angka_rahasia:
            print("Itu terlalu kecil. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Itu terlalu besar. Coba lagi.")
        else:
            print("Ya. Anda benar")

if __name__ == "__main__":
    tebak_angka()