class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString

    def cetakIni(self):
        print(self.teks)    

    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))

    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))

    def jumKar(self):
        return len(self.teks)

    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai", len(self.teks), "karakter.")

    def perbarui(self, stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, substring):
        return substring in self.teks

    def hitungKonsonan(self):
        konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for char in self.teks if char in konsonan)

    def hitungVokal(self):
        vokal = "aeiouAEIOU"
        return sum(1 for char in self.teks if char in vokal)

# Contoh penggunaan
p9 = Pesan('Indonesia adalah negeri yang indah')
print(p9.apakahTerkandung('ege'))  
print(p9.apakahTerkandung('eka')) 

p10 = Pesan('Surakarta')
print(p10.hitungKonsonan())  
print(p10.hitungVokal())     