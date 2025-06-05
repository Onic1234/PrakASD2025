class Stack(object):
    def __init__(self):  # Membuat stack kosong.
        self.items = []  # List untuk menyimpan stack.

    def isEmpty(self):  # Mengembalikan True kalau kosong,
        return len(self) == 0  # selain itu False

    def __len__(self):  # Mengembalikan banyaknya item di stack.
        return len(self.items)

    def peek(self):  # Mengembalikan nilai posisi atas tanpa menghapus.
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        return self.items[-1]

    def pop(self):  # Mengembalikan nilai posisi atas lalu menghapus.
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        return self.items.pop()

    def push(self, data):  # Mendorong item baru ke stack.
        self.items.append(data)


def cetakBiner(d):
    """
    Mengubah bilangan basis 10 ke basis 2 (biner).
    """
    f = Stack()

    if d == 0:
        f.push(0)

    while d != 0:
        sisa = d % 2
        d = d // 2
        f.push(sisa)

    st = ""
    while not f.isEmpty():
        st += str(f.pop())

    return st


# Contoh penggunaan
print("Cetak Biner")
d = 30
biner = cetakBiner(d)
print(f"Biner dari {d} adalah {biner}")