from re import X
from baca import *

def cekPemenang(kotak):
    print("\nProses Pengecekan")
    # Cek secara horizontal
    #print("\nhorizontal")
    for i in range(3):
        if (kotak[i][0] == "#"): continue
        horizontal = 1
        for j in range(1,3):
            if (kotak[i][j] == kotak[i][0]): horizontal += 1
        if (horizontal == 3): return kotak[i][0]

    # Cek secara vertikal
    for i in range(3):
        if (kotak[0][i] == "#"): continue
        vertikal = 1
        for j in range(1,3):
            if (kotak[j][i] == kotak[0][i]): vertikal += 1
        if (vertikal == 3): return kotak[0][i]

    # Cek secara diagonal 1
   
    if (kotak[0][0] != "#"):  
        diagonal = 1
        for i in range(1,3):
            if (kotak[i][i] == kotak[0][0]): diagonal += 1
        if (diagonal == 3): return kotak[0][0]

    # Cek secara diagonal 2
    if (kotak[0][2] != "#"): 
        diagonal = 1
        for i in range(1,3):
            if (kotak[i][2-i] == kotak[0][2]): diagonal += 1
        if (diagonal == 3): return kotak[0][2]

    return "-1" # Misal belum ada yang menang

def cekSeri(kotak):
    for i in kotak:
        for j in i:
            if (j == "#"):
                return False
    return True
    

def kosong(kotak, pemain1):
    print("Masukkan Kosong! Coba Ulangi")
    garis2(10)
    baca()
    play(kotak, pemain1)
    return

def play(kotak, pemain1):
    clear()  
    print("Tic Tac Toe")
    garis(10)
    print("Note: Indeks dimulai dari 1 sampai N")  
    print("X : Pemain 1")
    print("O : Pemain 2\n")
    print("Status Papan")
    for i in kotak:
        for j in i:
            print(j, end="")
        print()
    
    # Cek apakah permainan sudah selesai
    ans = cekPemenang(kotak)
    if (ans != "-1"):
        print("\nPemenang dari game ini adalah", ans + "!")
        garis2(10)
        baca()
        return
    
    if (cekSeri(kotak)):
        print("\nSeri. Tidak ada yang menang!")
        garis2(10)
        baca()
        return

    pemain = ""
    if (pemain1): pemain = "X"
    else: pemain = "O"
    print("\nGiliran Pemain", pemain)

    X = 0; Y = 0
    x = input("X : "); 
    if (x != ""):
        X=int(x)-1
    else:
        kosong(kotak, pemain1)
    y = input("Y : "); 
    if (y != ""):
        Y=int(y)-1
    else:
        kosong(kotak, pemain1)
    
    if ((0<=X<3) and (0<=Y<3)):
        if (kotak[X][Y] == "#"):
            if (pemain1): kotak[X][Y] = "X"
            else: kotak[X][Y] = "O"
        else:
            print("\nKotak sudah terisi. Silakan pilih kotak lain.") 
            garis2(10)
            baca()
            play(kotak, pemain1)
            return 
    else:
        print("\nKotak tidak valid!")
        garis2(10)
        baca()
        play(kotak, pemain1)
        return 
    
    play(kotak, not(pemain1))

#kotak = [["#" for j in range(3)] for i in range(3)]
#play(kotak, True)

            



