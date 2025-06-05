class Queue(object):
    def __init__(self):
        self.qlist = []
        
    def isEmpty(self):
        return len(self)  == 0
    
    def __len__(self):
        return len(self.qlist)
    
    def enqueue(self, data):
        self.qlist.append(data)
        
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop(0)
    
    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[0]
    
    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[-1]
    
# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    print(q.getFrontMost())  
    print(q.getRearMost())   
    
    print(q.dequeue())       
    print(q.dequeue())       
    print(q.dequeue())   

# Q = Queue()
# Q.enqueue(28)
# Q.enqueue(19)
# Q.enqueue(45)
# Q.enqueue(13)
# Q.enqueue(7)
# Q.dequeue() #Perhatikan urutan hasilnya.
# Q.dequeue() #Apakah sesuai dengan urutan masuknya?
# Q.dequeue()
# Q.dequeue() #Apakah ada pesan error?
# Q.enqueue(98)
# Q.enqueue(54)
# Q.dequeue()