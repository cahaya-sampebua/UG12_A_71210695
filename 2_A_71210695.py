#Soal 2
datanama = []
datakursi = []
mulai = 1
while (mulai <= 1): 
    nama = input("Masukkan nama: ")  
    
    if nama == "STOP":
        break
    kursi = int(input("Masukkan nomor kursi {} : ".format(nama)))
        
    if kursi in datakursi:  
        print("Mohon maaf kursi tersebut telah terisi!")

    elif kursi not in datakursi:
        datanama.append(nama)
        datakursi.append(kursi)
    
print("List kursi yang telah terisi : ")

for i in range(0,len(datakursi),1):
    print("Kursi nomor {} telah diisi oleh {}" .format(datakursi[i], datanama[i]))
