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
            "password" : encrypt(password, [7, 1]),
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
        
