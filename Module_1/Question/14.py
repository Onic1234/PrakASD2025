def formatRupiah(angka):
    return "Rp " + "{:,}".format(angka).replace(",", ".")

# Contoh penggunaan
print(formatRupiah(1500))      # Rp 1.500
print(formatRupiah(2560000))   # Rp 2.560.000