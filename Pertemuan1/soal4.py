angka = int(input("Masukkan nilai yang ingin dicek: "))

prima = True

for i in range(2, angka):
    if (angka % i == 0):
        prima = False
        break

if angka < 2 or prima == False:
    print(angka, "adalah bukan bilangan prima")
else:
    print(angka, "adalah bilangan prima")