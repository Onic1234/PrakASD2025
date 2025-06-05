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


def cetakHexa(d):
    """
    Mengubah bilangan basis 10 ke basis 16 (heksadesimal).
    """
    f = Stack()
    hexa_map = "0123456789ABCDEF"  # Pemetaan angka ke simbol heksadesimal

    if d == 0:
        f.push(0)

    while d != 0:
        sisa = d % 16
        d = d // 16
        f.push(hexa_map[sisa])  # Pemetaan sisa ke simbol heksadesimal

    hasil = ""
    while not f.isEmpty():
        hasil += str(f.pop())  # Menggabungkan simbol dari stack

    return hasil


# Contoh penggunaan
print(cetakHexa(12))      # Output: 'C'
print(cetakHexa(31))      # Output: '1F'
print(cetakHexa(229))     # Output: 'E5'
print(cetakHexa(255))     # Output: 'FF'
print(cetakHexa(31519))   # Output: '7B1F' 