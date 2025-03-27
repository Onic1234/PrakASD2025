class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        """
        Menambahkan elemen baru ke akhir linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def cari(self, item):
        """
        Mencari item dalam linked list.
        Mengembalikan True jika ditemukan, False jika tidak.
        """
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def cetak(self):
        """
        Mencetak semua elemen dalam linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Contoh penggunaan
ll = LinkedList()
ll.tambah(10)
ll.tambah(20)
ll.tambah(30)
ll.tambah(40)

print("Isi Linked List:")
ll.cetak()

# Mencari item
item = 30
if ll.cari(item):
    print(f"Item {item} ditemukan dalam linked list.")
else:
    print(f"Item {item} tidak ditemukan dalam linked list.")

item = 50
if ll.cari(item):
    print(f"Item {item} ditemukan dalam linked list.")
else:
    print(f"Item {item} tidak ditemukan dalam linked list.")