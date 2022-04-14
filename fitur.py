import os
import sys
from baca import *
from olah_csv import array_to_string, string_to_csv

def help():
    print("Help")

def save(database):
    clear()
    print("Save")
    garis2(5)
    nama_folder = input("Masukkan nama folder: ")
    
    # Cek apakah ada folder di dalam savedata
    direc = "savedata\\" + nama_folder + "\\"

    if (not(os.path.exists("savedata/"+nama_folder))): 
        os.mkdir("savedata/"+nama_folder)

    #Inisialisasi Data
    data_user = "id;username;nama;password;role;saldo\n" + array_to_string(database, "user")
    data_game = "id;nama;kategori;tahun_rilis;harga;stok\n" + array_to_string(database, "game")
    data_riwayat = "game_id;nama;harga;user_id;tahun_beli\n"+array_to_string(database, "riwayat")
    data_kepemilikan = "game_id;user_id\n" + array_to_string(database, "kepemilikan")
    
    string_to_csv("user", direc, data_user)
    string_to_csv("game", direc, data_game)
    string_to_csv("riwayat", direc, data_riwayat)
    string_to_csv("kepemilikan", direc, data_kepemilikan)

    

def keluar(database):
    clear()
    ans = input("Apakah anda ingin save data sebelum keluar? (y/n) ")
    if (ans == "y"):
        #Savedata
        save(database)
        sys.exit()
    elif (ans == "n"):
        sys.exit()
    else:
        keluar(database)

def isNumber(x): # Fungsi mengecek apakah string x adalah angka
    i = 0
    for c in x:
        #print(i)
        if (c == "-"):
            #print("\tnegatif")
            if (i > 0): return False
            else: continue
        if (c < "0" or c > "9"): return False
        i += 1
    return True

def length(x): # Fungsi Mencari panjang string
    length = 0
    for c in x:
        length += 1
    return length