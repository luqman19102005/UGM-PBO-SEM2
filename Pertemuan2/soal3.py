class persegi:
    def __init__(self, sisi):
       self.sisi = sisi

    def luas_persegi(self):
        print(f"luas persegi dengan panjang sisi {self.sisi} adalah {self.sisi**2}")

    def keliling_persegi(self):
        print(f"keliling persegi dengan panjang sisi {self.sisi} adalah {self.sisi*4}")

x = persegi(int(input("Masukkan panjang sisi persegi: ")))
x.luas_persegi()
x.keliling_persegi()