class manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_nama(self):
        print(f"Nama: {self.nama}")

    def cetak_umur(self):
        print(f"Umur: {self.umur}")

x = manusia(input("Masukkan nama: "), input("Masukkan umur: "))
x.cetak_nama()
x.cetak_umur()