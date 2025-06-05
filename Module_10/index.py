class _SimpulPohonBiner(object):
    def init(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.kiri)
        preorderTrav(subtree.kanan)

def inorderTrav(subtree):
    if subtree is not None:
        inorderTrav(subtree.kiri)
        print(subtree.data)
        inorderTrav(subtree.kanan)
        
def postorderTrav(subtree):
    if subtree is not None:
        postorderTrav(subtree.kiri)
        postorderTrav(subtree.kanan)
        print(subtree.data)


def treeSize(root):
    if root is None:
        return 0
    return 1 + treeSize(root.kiri) + treeSize(root.kanan)

def treeHeight(root):
    if root is None:
        return -1
    return 1 + max(treeHeight(root.kiri), treeHeight(root.kanan))

def cetakDataDanLevel(root, level=0):
    """
    Mencetak data dan level dari setiap simpul pohon biner
    dengan format: <data>, level <level>.
    """
    if root is not None:
        print(f"{root.data}, level {level}")
        cetakDataDanLevel(root.kiri, level + 1)
        cetakDataDanLevel(root.kanan, level + 1)


# Contoh penggunaan
if __name__ == "__main__":
    # Membuat simpul pohon biner
    root = _SimpulPohonBiner()
    root.init("Ambarawa")
    root.kiri = _SimpulPohonBiner()
    root.kiri.init("Bantul")
    root.kanan = _SimpulPohonBiner()
    root.kanan.init("Cimahi")
    root.kiri.kiri = _SimpulPohonBiner()
    root.kiri.kiri.init("Denpasar")
    root.kiri.kanan = _SimpulPohonBiner()
    root.kiri.kanan.init("Enrekang")
    root.kiri.kanan.kiri = _SimpulPohonBiner()
    root.kiri.kanan.kiri.init("Halmahera Timur")

    print("Data dan Level:")
    cetakDataDanLevel(root)