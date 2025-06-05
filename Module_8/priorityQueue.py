class PriorityQueue:
    def __init__(self):
        self.qlist = []
        
    def __len__(self):
        return len(self.qlist)
    
    def isEmpty(self):
        return len(self) == 0
    
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
        
    def dequeue(self):
        """
        Menghapus dan mengembalikan item dengan prioritas tertinggi.
        Jika ada beberapa item dengan prioritas yang sama, item yang
        dimasukkan lebih awal akan dihapus terlebih dahulu.
        """
        if self.isEmpty():
            raise IndexError("dequeue from an empty priority queue")
        
        # Cari item dengan prioritas tertinggi
        highest_priority_index = 0
        for i in range(1, len(self.qlist)):
            if self.qlist[i].priority < self.qlist[highest_priority_index].priority:
                highest_priority_index = i
        
        # Hapus dan kembalikan item dengan prioritas tertinggi
        return self.qlist.pop(highest_priority_index)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

# Example usage
s = PriorityQueue()
s.enqueue("Mangga", 2)
s.enqueue("Duku", 1)
s.enqueue("Pepaya", 3)

print(s.dequeue().item)  # Output: "Duku" (priority 1)
print(s.dequeue().item)  # Output: "Mangga" (priority 2)
print(s.dequeue().item)  # Output: "Pepaya" (priority 3)