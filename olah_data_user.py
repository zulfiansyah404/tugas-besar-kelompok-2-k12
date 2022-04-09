import os
from baca import *
from olah_csv import *

def tambah_user(nama, username, password, data):
    for i in data:
        if (i["username"] == username):
            return False
    print(data)
    N = hitungBaris(data) + 2
    #print(N)
    paket = [str(N), username, nama, password, "user", "0"]
    tambah_data(paket, "user")
    return True

def register(data):
    os.system('cls')
    print("Registrasi")
    print("----------\n")

    nama = input("Masukkan Nama: ")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if (tambah_user(nama, username, password, data)):
        print("Data User berhasil ditambahkan!")
        input()
    else:
        print("Username pernah ada sebelumnya. Coba Masukkan Lagi!")
        input()
        register(data)

    return data

def topup(database, user):
    print()

a = csv_to_array("user")
print(register(a))