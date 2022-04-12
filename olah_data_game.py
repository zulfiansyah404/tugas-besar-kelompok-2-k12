from baca import *
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
        while (int(data[pLeft][indeks]) < int(pivot)):
            pLeft += 1
        while (int(data[pRight][indeks]) > int(pivot)):
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
    
    ans = input("Urut Berdasarkan: ")
    print()
    inp = ["harga", "tahun_rilis", "stok"]

    inputValid = False
    for i in inp:
        if (ans == i): 
            inputValid = True
            break
    
    if (inputValid):
        quick_sort(data, 0, hitungBaris(data), ans)

        # Output data
        print("id | nama | kategori | tahun rilis | harga | stok\n")
        for i in data:
            print(i["id"], end=" | ")
            print(i["nama"], end=" | ")
            print(i["kategori"], end=" | ")
            print(i["tahun_rilis"], end=" | ")
            print(i["harga"], end=" | ")
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
    # Petugas : Sjora

def buy_game():
    clear()
    # Tulis Kode Disini
    # Petugas : Sjora

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
