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

    if (not(os.path.exists("C:/Users/zulfi/OneDrive/Dokumen/ITB/Daspro/tugas-besar/repo/tugas-besar-kelompok-2-k12/savedata/"+nama_folder))): 
        os.mkdir("C:/Users/zulfi/OneDrive/Dokumen/ITB/Daspro/tugas-besar/repo/tugas-besar-kelompok-2-k12/savedata/"+nama_folder)

    #Inisialisasi Data
    data_user = array_to_string(database, "user")
    data_game = array_to_string(database, "game")
    data_riwayat = array_to_string(database, "riwayat")
    data_kepemilikan = array_to_string(database, "kepemilikan")
    
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
    for c in x:
        if (c < "0" or c > "9"): return False
    return True