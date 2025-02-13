niu = int(input("Masukkan 6 digit NIU: "))
tugas = int(input("Masukkan nilai tugas: "))
laporan = int(input("Masukkan nilai laporan: "))

nilai_awal = (tugas + laporan)/2
if nilai_awal <= 40:
    print("K")
else:
    ujian = int(input("Masukkan nilai ujian: "))
    nilai = tugas*0.25 + laporan*0.25 + ujian*0.5
    if 80 <= nilai <= 100:
        print("A")
    elif 70 <= nilai < 80:
        print("B")
    elif 60 <= nilai < 70:
        print("C")
    elif 50 <= nilai < 60:
        print("D")
    elif nilai < 50:
        print("E")