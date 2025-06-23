

class TreeNode:
    def __init__(self, kiri=None, kanan=None):
        self.kiri = kiri
        self.kanan = kanan

# ukuran
def ukuranPohon(akar):
    if akar is None:
        return 0
    return 1 + ukuranPohon(akar.kiri) + ukuranPohon(akar.kanan)

akar = TreeNode(
    kiri=TreeNode(
        kiri=TreeNode(),  # D
        kanan=None        # None
    ),
    kanan=TreeNode(
        kiri=None,
        kanan=TreeNode()  # E
    )
)

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


# Uji fungsi ukuranPohon
ukuran = ukuranPohon(akar)
ukuran
