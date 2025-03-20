def katakan(angka):
    satuan = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"]
    
    def terbilang(n):
        if n < 12:
            return satuan[n]
        elif n < 20:
            return terbilang(n - 10) + " belas"
        elif n < 100:
            return terbilang(n // 10) + " puluh" + ("" if n % 10 == 0 else " " + terbilang(n % 10))
        elif n < 200:
            return "seratus" + ("" if n % 100 == 0 else " " + terbilang(n % 100))
        elif n < 1000:
            return terbilang(n // 100) + " ratus" + ("" if n % 100 == 0 else " " + terbilang(n % 100))
        elif n < 2000:
            return "seribu" + ("" if n % 1000 == 0 else " " + terbilang(n % 1000))
        elif n < 1000000:
            return terbilang(n // 1000) + " ribu" + ("" if n % 1000 == 0 else " " + terbilang(n % 1000))
        elif n < 1000000000:
            return terbilang(n // 1000000) + " juta" + ("" if n % 1000000 == 0 else " " + terbilang(n % 1000000))
        else:
            return terbilang(n // 1000000000) + " milyar" + ("" if n % 1000000000 == 0 else " " + terbilang(n % 1000000000))
    
    return terbilang(angka)

# Contoh penggunaan
print(katakan(3125750))  