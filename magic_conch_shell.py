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

        jawaban = ['iya kali ya', 'nggak.','bisa jadi sih','mungkin','ya iya lah','udah gausah ngarep']
        print(jawaban[n])

        print()
        baca()
        kerangajaib()
