import os
import sys
from baca import *

def help():
    print("Help")

def save(database):
    print("Save")

def keluar(database):
    clear()
    ans = input("Apakah anda ingin save data sebelum keluar? (y/n) ")
    if (ans == "y"):
        #Savedata
        save(database)
        sys.exit()
    elif (ans == "n"):
        sys.exit()
    else:
        keluar(database)

def isNumber(x): # Fungsi mengecek apakah string x adalah angka
    for c in x:
        if (c < "0" or c > "9"): return False
    return True