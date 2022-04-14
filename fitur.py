import os
import sys
from baca import *
from olah_csv import array_to_string, string_to_csv

def help():
    print("Help")

def save(database):
    nama_folder = input("Masukkan nama folder: ")
    
    found_folder = False
    # Cek apakah ada folder di dalam savedata
    for (root,dirs,files) in os.walk('savedata', topdown=True):
        if (root == 'savedata'):
            for folder in dirs:
                if (folder == nama_folder):
                    found_folder = True
                    break
        else:
            break

    direc = "savedata\\" + nama_folder + "\\"

    if (not(found_folder)): 
        os.system("cd savedata")
        os.system("mkdir "+nama_folder)
        os.system("cd ..")
        csv_user = open(direc+"user.csv","x"); csv_user.close()
        csv_game = open(direc+"game.csv","x"); csv_game.close()
        csv_kepemilikan = open(direc+"kepemilikan.csv","x"); csv_kepemilikan.close()
        csv_riwayat = open(direc+"riwayat.csv","x"); csv_riwayat.close()

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