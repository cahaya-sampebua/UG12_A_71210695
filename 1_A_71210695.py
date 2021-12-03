#Soal 1
elemen_1 = []
elemen_2 = []
bilangan_awal = 0
deret_bil = list(input("Masukkan deret angka : ").split(","))
print("Total: ", end="")
for i in deret_bil:
    while (bilangan_awal < 1):
        elemen_2.append(int(i))

        if int(i) % 2 != 0:
            Ganjil = int(i) * (-1)
            elemen_1.append(Ganjil)
            print(" - ", i, end="")          

        elif int(i) % 2 == 0:
            Genap = int(i)      
            elemen_1.append(Genap)           
            print(" + ",Genap, end="")
            
        bilangan_awal = bilangan_awal + 1

    if int(i) in elemen_2:
           continue

    elif int(i) % 2 != 0:
        Ganjil = int(i) * (-1)
        elemen_1.append(Ganjil)
        print(" - ", i, end="")
         
    elif int(i) % 2 == 0:
        Genap = int(i)      
        elemen_1.append(Genap)           
        print(" + ",Genap, end="")

print("\nHasil Perhitungan diatas ialah ", sum(elemen_1))
