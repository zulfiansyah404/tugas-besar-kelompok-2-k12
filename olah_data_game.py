from baca import *
from fitur import length, tahun
from olah_csv import *

def quick_sort(data, left, right, indeks):
    if (left >= right): return

    tengah = int((left + right)/2)
    #print(tengah, type(tengah))
    #print(data[tengah][indeks])
    pivot = data[tengah][indeks]
    pLeft = left
    pRight = right

    while (pLeft <= pRight):
        while ((data[pLeft][indeks]) < (pivot)):
            pLeft += 1
        while ((data[pRight][indeks]) > (pivot)):
            pRight -= 1
        if (pLeft <= pRight):
            # Operasi Swab
            temp = data[pLeft]
            data[pLeft] = data[pRight]
            data[pRight] = temp

            pLeft += 1
            pRight -= 1
    
    quick_sort(data, left, pRight, indeks)
    quick_sort(data, pLeft, right, indeks)

def quick_sort_dec(data, left, right, indeks):
    if (left >= right): return

    tengah = int((left + right)/2)
    #print(tengah, type(tengah))
    #print(data[tengah][indeks])
    pivot = data[tengah][indeks]
    pLeft = left
    pRight = right

    while (pLeft <= pRight):
        while ((data[pLeft][indeks]) > (pivot)):
            pLeft += 1
        while ((data[pRight][indeks]) < (pivot)):
            pRight -= 1
        if (pLeft <= pRight):
            # Operasi Swab
            temp = data[pLeft]
            data[pLeft] = data[pRight]
            data[pRight] = temp

            pLeft += 1
            pRight -= 1
    
    quick_sort_dec(data, left, pRight, indeks)
    quick_sort_dec(data, pLeft, right, indeks)


def tambah_game():
    clear()
    a = True

    while a:
        nama = input('Masukkan nama game: ')
        kategori = input('Masukkan kategori: ')
        tahun = input('Masukkan tahun rilis: ')
        harga = input('Masukkan harga: ')
        stok = input('Masukkan stok awal: ')

        if (nama != '') and (kategori != '') and (tahun != '') and (harga != '') and (stok != ''):
            print('Selamat! Berhasil menambahkan game BNMO - Play Along With Crypto.')
            a = False
        else:
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')

def ubah_game():
    clear()
    # Tulis Kode Disini
    # Petugas : Malik

def ubah_stok():
    clear()
    # Tulis Kode Disini
    # Petugas : Fadhil

def list_game_toko(data):
    clear()
    # Tulis Kode Disini
    # Petugas : Zulfiansyah
    print("List Game Toko")
    garis2(10)
    print()

    #print("| id | nama | kategori | tahun rilis | harga | stok |")
    #for i in data:
    #    print("|",i["id"],"|",i["nama"],"|",i["kategori"],"|",i["tahun_rilis"],"|",i["harga"],"|",i["stok"],"|")
    up = True
    ans = input("Urut Berdasarkan: ")
    print()
    inputValid = True
    cek = ""
    if (ans != ""):
        inp = ["harga", "tahun_rilis", "stok"]    

        len = length(ans)
        if (ans[len-1] == "-" or ans[len-1] == "+"): cek = ans[0:len-1]
        else: cek = ans
        
        inputValid = False
        for i in inp:
            if (cek == i): 
                inputValid = True
                break

    if (inputValid):
        if (ans == ""):
            quick_sort(data, 0, hitungBaris(data), "id")
        elif (ans == cek+"+" or ans == cek):
            quick_sort(data, 0, hitungBaris(data), cek)
        elif (ans == cek+"-"):
            quick_sort_dec(data, 0, hitungBaris(data), cek)
            

        # Output data
        print("id \t| nama \t| kategori \t| tahun rilis \t| harga \t| stok\n")
        for i in data:
            print(i["id"], end=" \t| ")
            print(i["nama"], end=" \t| ")
            print(i["kategori"], end=" \t| ")
            print(i["tahun_rilis"], end=" \t| ")
            print(i["harga"], end=" \t| ")
            print(i["stok"], end="")
            print("\n")
        garis2(10)
        print()
        baca()
    else:
        print("Masukkan Tidak Valid!")
        garis2(10)
        baca()
    
def search_game_at_store():
    clear()
    # Tulis Kode Disini
    # Petugas : Fadhil

def list_game(database, user):
    clear()
    # Tulis Kode Disini
    # Petugas : Anjani
    data_user = database["user"][user]
    data_game = database["game"]
    len = 0

    for arr in database["kepemilikan"]:
        if (arr["user_id"] == data_user["id"]):
            game_id = arr["game_id"]
            for game in data_game:
                if (game["id"] == game_id):
                    if (len == 0):
                        print("Daftar game:")
                    print(len+1, end="\t| ")
                    print(game["id"], end=" \t| ")
                    print(game["nama"], end=" \t| ")
                    print(game["kategori"], end=" \t| ")
                    print(game["tahun_rilis"], end=" \t| ")
                    print(game["harga"], end=" \t| ")
                    print("\n")
            len += 1

    print()
    if (len == 0):
        print("Maaf, kamu belum membeli game. :(\n")
    
    baca()


def search_my_game(database, user):
    clear()
    # Tulis Kode Disini
    # Petugas : Malik

def riwayat():
    clear()
    # Tulis Kode Disini
    # Petugas : Sjora

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
    len = length(data_kepemilikan) + 1
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
    len = length(database["riwayat"]) + 1
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

    print('\nGame "' + game["nama"] + '" berhasil dibeli!\n')
    baca()
    return database

    

    
    