from index import menu
from baca import *
from olah_csv import *

def buatDatabase(data_user, dir_file):
    database = {
        "user" : data_user,
        "game" : csv_to_array("game", dir_file),
        "riwayat" : csv_to_array("riwayat", dir_file),
        "kepemilikan" : csv_to_array("kepemilikan", dir_file)
    }
    
    return database

def login(dir_file):
    clear()
    logo()
    garis(20); 
    print()

    print("LOGIN")
    garis2(10)
    username = input("Username : ")
    password = input("Password : ")
    print()

    # Proses Pencarian Username
    data_user = csv_to_array("user", dir_file)
    i = 0
    for data in data_user:
        if (data["username"] == username):
            if (data["password"] == password):
                print("Selamat datang," + data["nama"] + "!")
                garis2(10)
                print()
                baca()
                database = buatDatabase(data_user, dir_file)
                if (data["role"] == "admin"):
                    menu(database, i, True)
                else:
                    menu(database, i, False)
                return
            else:
                print("Password Salah. Ulangi Lagi!")
                input()
                login(dir_file)
                return
        else:
            i += 1
    print("Username tidak ditemukan. Ulangi Lagi!")
    input()
    login(dir_file)
    return