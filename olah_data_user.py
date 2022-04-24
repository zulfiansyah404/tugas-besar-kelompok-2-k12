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
    
    if (not(ada)):  # Jika username belum pernah ada di database      
        database["user"] = push_data("user", database, [str(len(database["user"]) + 1), username, nama, encrypt(password, [7, 1]), "user", "0"])

        for i in database["user"]:
            print(i)

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

