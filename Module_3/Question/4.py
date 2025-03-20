class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def cetakDepan(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def cetakBelakang(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def tambahDepan(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def tambahAkhir(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

# Contoh penggunaan
dll = DoublyLinkedList()
dll.tambahDepan(3)
dll.tambahDepan(2)
dll.tambahDepan(1)
dll.cetakDepan()
dll.cetakBelakang()  

dll.tambahAkhir(4)
dll.cetakDepan()  
dll.cetakBelakang()  
