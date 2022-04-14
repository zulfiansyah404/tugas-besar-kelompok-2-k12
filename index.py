import login
from baca import *
from olah_data_user import *
from olah_data_game import *
from fitur import *

# database = array berisi data pada user.csv
# user = indeks posisi user pada elemen array

def User(database, user):
    print("1. List Game Toko")
    print("2. Beli Game")
    print("3. Game yang Dimiliki")
    print("4. Cari Game yang Dimiliki")
    print("5. Cari Game di Toko")
    print("6. Riwayat Pembelian")
    print("7. Help")
    print("8. Save")
    print("9. Exit")
    garis2(10)
    inp = input("Input = ")
    
    if (inp == '1'): list_game_toko(database["game"])
    elif (inp == '2'): database = buy_game(database, user)
    elif (inp == '3'): list_game(database["game"])
    elif (inp == '4'): search_my_game(database["game"], user)
    elif (inp == '5'): search_game_at_store(database["game"])
    elif (inp == '6'): riwayat(database["riwayat"]) 
    elif (inp == '7'): help()
    elif (inp == '8'): save(database)
    elif (inp == '9'): keluar(database)  

def admin(database, user):
    print("1. Register")
    print("2. Tambah Game ke Toko Game")
    print("3. Ubah Game ke Toko Game")
    print("4. Ubah Stok Game di Toko")
    print("5. List Game Toko")
    print("6. Cari Game di Toko")
    print("7. Top Up Saldo")
    print("8. Help")
    print("9. Save")
    print("10. Exit")
    garis2(10)
    inp = input("Input = ")
    
    if (inp == '1'): database = register(database)
    elif (inp == '2'): database = tambah_game(database)
    elif (inp == '3'): database = ubah_game(database)
    elif (inp == '4'): database = ubah_stok(database)
    elif (inp == '5'): list_game_toko(database["game"])
    elif (inp == '6'): search_game_at_store(database["game"])
    elif (inp == "7"): database = topup(database)   
    elif (inp == '8'): help()
    elif (inp == '9'): save(database)
    elif (inp == "10"): keluar(database)

def menu(database, user, isAdmin):
    clear()
    logo()
    garis(20); 
    print()
    print("Halo,", database["user"][user]["nama"] + "!\n")
    print("Menu"); 
    garis2(10)

    # Jika login sebagai admin
    if (isAdmin):
        admin(database, user)
    # Jika login sebagai user
    else:
        User(database, user)
    
    menu(database, user, isAdmin)    


    



