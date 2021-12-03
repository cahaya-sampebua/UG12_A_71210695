#Soal 3
karakter = str(input("Input : "))
jum_Karakter = len(karakter)

print("Output :") 

for a in range(0, jum_Karakter):
    for b in range(0, a):
        print(karakter[b], end="")
    print("")

for a in range(jum_Karakter, 0, -1): 
    for b in range(0, a):
        print(karakter[b], end="")
    print("")


    
