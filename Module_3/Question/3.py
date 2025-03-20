class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def cari(self, yang_dicari):
        current = self.head
        while current is not None:
            if current.data == yang_dicari:
                return True
            current = current.next
        return False

    def tambahDepan(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambahAkhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tambah(self, data, posisi):
        new_node = Node(data)
        if posisi == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(posisi - 1):
            if current is None:
                raise IndexError("Posisi di luar jangkauan")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def hapus(self, posisi):
        if self.head is None:
            raise IndexError("List kosong")
        if posisi == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(posisi - 1):
            if current.next is None:
                raise IndexError("Posisi di luar jangkauan")
            current = current.next
        if current.next is None:
            raise IndexError("Posisi di luar jangkauan")
        current.next = current.next.next

    def cetak(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Contoh penggunaan
ll = LinkedList()
ll.tambahDepan(3)
ll.tambahDepan(2)
ll.tambahDepan(1)
ll.cetak() 
ll.tambahAkhir(4)
ll.cetak()  
ll.tambah(1.5, 1)
ll.cetak()  
ll.hapus(1)
ll.cetak()  
print(ll.cari(3))  
print(ll.cari(5))  