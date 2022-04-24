from baca import *
from time import *

def kerangajaib():
    clear
    print("Magic Conch Shell")
    garis(10)
    inp = input("Apa Pertanyaanmu? ")
    x = int(time.time()) 
    a = x % 10; c = int(time.process_time_ns()); m = 18
    lcg = ((a*x)+c) % m 
    n = abs((lcg % 9))

    jawaban = ['Ya', 'Tidak','Bisa Jadi','Mungkin','Tentunya','Tidak mungkin']
    print(jawaban[n])

    print()
    baca()
    if (inp != ""): kerangajaib()