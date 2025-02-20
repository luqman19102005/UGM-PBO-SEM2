class persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas_persegi_panjang(self):
        print(f"luas persegi panjang dengan panjang {self.panjang} dan lebar {self.lebar} adalah {self.panjang*self.lebar}")

def main():
    x = persegi_panjang(int(input("Masukkan panjang sisi: ")), int(input("Masukkan lebar sisi: ")))
    x.luas_persegi_panjang()

if __name__ == "__main__":
    main()