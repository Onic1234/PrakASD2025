# Definisi ulang fungsi tinggiPohon

def tinggiPohon(akar):
    if akar is None:
        return 0
    return 1 + max(tinggiPohon(akar.kiri), tinggiPohon(akar.kanan))

# Gunakan pohon yang sama dari pengujian sebelumnya:
#       A
#      / \
#     B   C
#    /     \
#   D       E

# Uji fungsi tinggiPohon
tinggi = tinggiPohon(akar)
tinggi
