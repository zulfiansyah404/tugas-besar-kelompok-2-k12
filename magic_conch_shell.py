from baca import *
from time import *

def kerangajaib():
    clear()
    print("Magic Conch Shell")
    garis(10)
    inp = input("Apa Pertanyaanmu? ")
    if (inp != ""):
        x = int(time()) 
        a = x % 10; c = int(process_time_ns()); m = 19
        lcg = ((a*x)+c) % m 
        n = abs((lcg % 6))

        jawaban = ['Ya', 'Tidak','Bisa Jadi','Mungkin','Tentunya','Tidak mungkin']
        print(jawaban[n])

        print()
        baca()
        kerangajaib()