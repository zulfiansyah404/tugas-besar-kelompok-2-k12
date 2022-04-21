from array import array
from baca import *
from olah_csv import *
from fitur import isNumber, length, tahun
from cipher import *

def register(database):
    # Petugas : Zulfiansyah
    clear()
    print("Registrasi")
    garis2(10)
    data = database["user"]

    nama = input("Masukkan Nama: ")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    # Cek input apakah kosong
    if ((nama == "") or (username == "") or (password == "") ):
        print("\nHarap Masukkan Input. Coba Ulangi!")
        garis2(10)
        baca()
        return register(database)

    # Cek username valid atau tidak 
    for c in username:
        if (('a' <= c <= 'z') or ('A' <= c <= 'Z') or (c == "-") or (c == '_') or ("0" <= c <= "9")): continue
        else:
            print("\nUsername Tidak Valid. Coba Ulangi!")
            garis2(10)
            baca()
            return register(database)

    # Cek apakah username ada di dalam data atau tidak
    ada = False
    for arr in data:
        if (arr["username"] == username):
            ada = True
            break
    
    panjangDataBaru = hitungBaris(data) + 2
    if (not(ada)):  # Jika username belum pernah ada di database
        temp = ["" for i in range(panjangDataBaru)] # Buat data sementara yang baru dengan jumlah barisnya ditambah 1
        i = 0
        # Mula - mula tempelkan data yang sebelumnya ke array temp
        for arr in data:
            temp[i] = arr
            i += 1
        # Lalu buat directory array temp indeks paling bawah
        temp[i] = {
            "id" : str(panjangDataBaru),
            "username" : username,
            "nama" : nama,
            "password" : encrypt(password),
            "role" : "user",
            "saldo" : "0"
        }
        data = temp                 # Lalu salin array temp ke array data
        database["user"] = data     # Lalu salin array data ke database["user"]
        # Untuk Debug
        #for i in data:
        #    print(i)

        print("\nData berhasil ditambahkan!")
        garis2(10)
        baca()
        return database
    else:
        print("\nUsername sudah ada. Coba Ulangi!")
        garis2(10)
        baca()
        return register(database)
        
def topup(database):
    # Petugas : Zulfiansyah
    clear()
    print("Top Up")
    garis2(10)
    data = database["user"]

    username = input("Masukkan Username: ")
    saldo = input("Masukkan Saldo: ")
    print()

    # Cek apakah username tersedia
    ada = False
    i = 0
    for arr in data:
        if (arr["username"] == username):
            ada = True
            break
        else:
            i += 1
    
    if (not(ada)):
        print("Username tidak tersedia!")
        garis2(10)
        baca()
        return database

    saldo_user = int(data[i]["saldo"])
    # Cek apakah saldo positif atau negatif
    if (isNumber(saldo)):
        if (saldo_user + int(saldo) >= 0):
            data[i]["saldo"] = str(saldo_user + int(saldo))
            print("Top up berhasil. Saldo "+data[i]["nama"]+" bertambah menjadi "+data[i]["saldo"]+".")
        else:
            print("Masukkan tidak valid.")
    else:
        print("Masukkan tidak valid")
    garis2(10)
    baca()
    database["user"][i] = data[i]
    return database

def buy_game(database, user):
    clear()
    print("Membeli Game")
    garis2(10)
    print()
    data_user = database["user"][user]
    data_game = database["game"]
    data_kepemilikan = database["kepemilikan"]

    id_game = input("Masukkan ID Game: ")
    
    # Cari apakah id game termasuk di dalam data game
    ada = True
    game = []
    i_game = 0
    for arr in data_game:
        if (arr["id"] == id_game):
            if (int(arr["stok"]) <= 0):
                ada = False
            else:
                game = arr
            break
        i_game += 1

    # Apabila stok game habis
    if (not(ada)):
        print("\nStok game tersebut sedang habis!\n")
        baca()
        return
    
    # Apabila Saldo Tidak Cukup
    if (int(game["harga"]) > int(data_user["saldo"])):
        print("\nSaldo anda tidak cukup untuk membeli Game tersebut!\n")
        baca()
        return

    # Apabila sudah pernah beli
    for arr in data_kepemilikan:
        if (arr["user_id"] == data_user["id"]):
            if (arr["game_id"] == id_game):
                print("\nAnda Sudah Memiliki Game Tersebut!\n")
                baca()
                return

    database["game"][i_game]["stok"] = str(int(game["stok"]) - 1)
    database["user"][user]["saldo"] = str(int(data_user["saldo"]) - int(game["harga"]))

    # Buat tambahan data kepemilikan
    len = length(data_kepemilikan)
    temp = ["" for i in range(len)]

    i = 0
    for arr in database["kepemilikan"]:
        temp[i] = arr
        i += 1
    
    temp[i] = {
        "game_id": id_game,
        "user_id": data_user["id"]
    }

    database["kepemilikan"] = temp

    # Buat tambahan data riwayat
    len = length(database["riwayat"])
    temp = ["" for i in range(len)]

    i = 0
    for arr in database["riwayat"]:
        temp[i] = arr
        i += 1
    
    temp[i] = {
        "game_id":id_game,
        "nama":game["nama"],
        "harga":game["harga"],
        "user_id": data_user["id"],
        "tahun_beli":tahun()
    }

    database["riwayat"] = temp

    print('Game "' + game["nama"] + '" berhasil dibeli!')
    return database

    

    
    