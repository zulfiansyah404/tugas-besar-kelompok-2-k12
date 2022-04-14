from baca import *
from olah_csv import *
from fitur import isNumber

def register(database):
    # Petugas : Zulfiansyah
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
        database["user"] = data
        # Untuk Debug
        #for i in data:
        #    print(i)

        print("Data berhasil ditambahkan!")
        garis2(10)
        baca()
        return database
    else:
        print("Username sudah ada. Coba Ulangi!")
        garis(10)
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
            print("Top up berhasil. Saldo "+data[i]["nama"]+" bertambah menjadi"+data[i]["saldo"]+".")
        else:
            print("Masukkan tidak valid.")
    else:
        print("Masukkan tidak valid")
    garis2(10)
    baca()
    database["user"][i] = data[i]
    return database

