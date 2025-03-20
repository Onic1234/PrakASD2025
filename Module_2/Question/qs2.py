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
    
    def ambilKotaTinggal(self):
        return self.kota
    
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kota = kotaBaru
    
    def tambahUangSaku(self, jumlah):
        self.uangSaku += jumlah

# Contoh penggunaan
m9 = Mahasiswa('Budi', 12345, 'Surabaya', 300000)
print(m9.ambilKotaTinggal())  # Surabaya
m9.perbaruiKotaTinggal('Sleman')
print(m9.ambilKotaTinggal())  # Sleman

m7 = Mahasiswa('Ani', 67890, 'Jakarta', 270000)
print(m7.ambilUangSaku())  # 270000
m7.tambahUangSaku(50000)
print(m7.ambilUangSaku())  # 320000