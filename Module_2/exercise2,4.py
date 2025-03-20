class Mahasiswa(object):
    """
        Class Mahasiswa dengan berbagai metode
    """
    
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
        
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) + '. Tinggal di ' + self.kota + '. Uang saku Rp ' + str(self.uangSaku) + ' tiap bulan.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku