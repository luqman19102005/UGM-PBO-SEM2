input = int(input("input angka terbesar: "))
i = input
x = []
while i <= input:
    x.append(i)
    if i <= 0:
        print(x)
        break
    else:
        i -= 1