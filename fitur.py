import os
import sys
from baca import *
from olah_csv import array_to_string, string_to_csv
import time

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

    print("\nData Berhasil Disimpan!")
    garis(10)
    baca()

def keluar(database):
    clear()
    ans = input("Apakah anda ingin save data sebelum keluar? (y/n) ")
    if (ans == "y" or ans == "Y"):
        #Savedata
        save(database)
        sys.exit()
    elif (ans == "n" or ans == "N"):
        sys.exit()
    else:
        keluar(database)

def isNumber(x): # Fungsi mengecek apakah string x adalah angka
    if (length(x) == 0): return False
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

def tahun():
    named_tuple = time.localtime()
    return time.strftime("%Y", named_tuple)
    
def kosong(x):
    if (length(x) > 0):
        return False
    else:
        print("\nInput Tidak Boleh Kosong")
        return True

def help(role):
    clear()
    print("Help")
    print("-----\n")
    if (role == "admin"):
        # Admin
        print("Untuk input di dalam menu")
        print("1 --> Untuk melakukan registrasi user baru")
        print("2 --> Untuk menambah data game yang baru - ")
        print("3 --> Untuk mengganti data suatu game ")
        print("4 --> Menambah atau mengurangi stok suatu game")
        print("5 --> Menampilkan list game berdasarkan permintaan")
        print("6 --> Mencari game di dalam toko")
        print("7 --> Menambah atau mengurangi saldo salah satu user")
        print("8 --> Untuk menampilkan menu 'help'")
        print("9 --> Menyimpan data user, game, riwayat, dan kepemilikan ke dalam csv dalam suatu folder")
        print("10 --> Keluar dari program (bisa menyimpan data juga)")
        print("A --> Memainkan game Magic Conch Shell")
        print("B --> Memainkan Game Tic-Tac-Toe")
        garis2(30)
    else:
        print("Untuk input di dalam menu")
        print("1 --> Menampilkan list game berdasarkan permintaan")
        print("2 --> Membeli Game yang tersedia di dalam toko")
        print("3 --> Menampilkan list game yang dimiliki oleh user")
        print("4 --> Mencari game yang dimiliki oleh user berdasarkan spesifikasi tertentu")
        print("5 --> Mencari game di dalam toko")
        print("6 --> Menampilkan riwayat pembelian game oleh user")
        print("7 --> Untuk menampilkan menu 'help'")
        print("8 --> Menyimpan data user, game, riwayat, dan kepemilikan ke dalam csv dalam suatu folder")
        print("9 --> Keluar dari program (bisa menyimpan data juga)")
        print("A --> Memainkan game Magic Conch Shell")
        print("B --> Memainkan Game Tic-Tac-Toe")
        garis2(30)

    print("Note : ")
    print("- Input program menu akan selalu berulang sampai inputnya valid")
    print("- Untuk menyimpan perubahan data seperti register, tambah game, dll, disarankan untuk melakukan save terlebih dahulu")
    print("  Agar perubahan data tersimpan di dalam csv")
    print("  Jika melakukan perubahan data tanpa save, maka perubahan tersebut akan hilang ketika membuka program kembali.")

    print()
    baca()