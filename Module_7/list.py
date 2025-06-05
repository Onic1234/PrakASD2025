class Stack(object):
    def __init__(self): # Membuat stack kosong.
        self.items = [] # List untuk menyimpan stack.

    def isEmpty(self): # Mengembalikan True kalau kosong,
        return len(self)==0 # selain itu False

    def __len__(self): # Mengembalikan banyaknya item di stack.
        return len(self.items) #

    def peek(self): # Mengembalikan nilai posisi atas tanpa menghapus.
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        return self.items[-1]

    def pop(self): # Mengembalikan nilai posisi atas lalu menghapus.
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        return self.items.pop()

    def push(self, data): # Mendorong item baru ke stack.
        self.items.append(data)
        
print("Contoh penggunaan Stack")
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Stack setelah push:", s.items)