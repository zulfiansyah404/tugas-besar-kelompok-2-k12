import argparse
import os
from baca import *
from login import *

parser = argparse.ArgumentParser()
parser.add_argument("echo", nargs="?")
args = parser.parse_args()

if __name__ == "__main__":
    os.system("title Program Binomo (Kelompok II K12)")
    if (args.echo == None):
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python program_binomo.py <nama_folder>")
    else:
        for (root,dirs,files) in os.walk('savedata', topdown=True):
            if (root == 'savedata'):
                for folder in dirs:
                    if (folder == args.echo):
                        clear()
                        hijau()
                        logo()
                        print('Selamat Datang di antarmuka "Binomo"')
                        print()
                        dir_file = root + "\\" + args.echo + "\\"
                        baca()
                        
                        login(dir_file)
            else:
                print('Folder "' + args.echo + '" tidak ditemukan.')
                break