from baca import *
from olah_csv import *

def register(database):
    clear()
    print("Registrasi")
    garis2(10)
    data = database["user"]

    nama = input("Masukkan Nama: ")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    # Cek apakah username ada di dalam data atau tidak
    ada = False
    for arr in data:
        if (arr["username"] == username):
            ada = True
            break
    
    panjangDataBaru = hitungBaris(data) + 2
    if (not(ada)):  # Jika username belum pernah ada di database
        temp = ["" for i in range(panjangDataBaru)] # Buat data sementara
        i = 0
        for arr in data:
            temp[i] = arr
            i += 1
        temp[i] = {
            "id" : str(panjangDataBaru),
            "username" : username,
            "nama" : nama,
            "password" : password,
            "role" : "user",
            "saldo" : "0"
        }

        data = temp

        # Untuk Debug
        #for i in data:
        #    print(i)

        print("Data berhasil ditambahkan!")
        garis2(10)
        baca()
    else:
        print("Username sudah ada. Coba Ulangi!")
        garis(10)
        baca()
        register(database)
        

def topup(database, user):
    print()