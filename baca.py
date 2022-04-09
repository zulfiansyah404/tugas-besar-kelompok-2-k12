import os

def logo():
    print("=====  =   =  =     =  =====")
    print("=   =  =   =  =     =  =   =")
    print("=====  ==  =  ==   ==  =   =")
    print("=   =  = = =  = = = =  =   =")
    print("=====  =  ==  =  =  =  =====")
    print()

def garis(x):
    for i in range(x):
        print("=", end='')
    print()

def garis2(x):
    for i in range(x):
        print("-")
    print()

def baca():
    print("Tekan 'Enter' untuk melanjutkan")
    input()

def clear():
    os.system('cls')