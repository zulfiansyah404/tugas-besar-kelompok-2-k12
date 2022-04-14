from baca import *
from fitur import length
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

def buy_game():
    clear()
    # Tulis Kode Disini
    # Petugas : Sjora
    print('Beli Game')
    garis2(10)
    id_game = input('Masukkan ID Game: ')
    print()

    #id game dari game.csv
        #if (id_game gaada di game.csv) and (saldo_user cukup) and (ada stok pada toko)
            #print('Game berhasil dibeli!')
        #elif (id_game udh ada di game.csv) and (saldo_user cukup) and (ada stok pada toko)
            #print('Game sudah Anda miliki!')
        #elif (id_game gaada di game.csv) and (saldo_user ga cukup) and (ada stok pada toko)
            #print('Saldo Anda tidak cukup untuk membeli Game tersebut!')
        #elif (id_game gaada di game.csv) and (saldo_user cukup) and (gaada stok pada toko)
            #print('Stok Game tersebut habis!')

def list_game():
    clear()
    # Tulis Kode Disini
    # Petugas : Anjani

def search_my_game():
    clear()
    # Tulis Kode Disini
    # Petugas : Malik

def riwayat():
    clear()
    # Tulis Kode Disini
    # Petugas : Sjora
