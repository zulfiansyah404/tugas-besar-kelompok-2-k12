def length(x): # Fungsi Mencari panjang string/array
    length = 0
    for c in x:
        length += 1
    return length
# Fungsi CSV
def hitungBaris(arr):
    ans = 0
    for i in arr:
        if (i == arr[0]): continue
        ans += 1
    return ans

def csv_to_array(nama_csv, dirs):
    database = open(dirs + nama_csv + ".csv")
    arr = database.readlines()
    baris = hitungBaris(arr)     
    data = ["" for i in range(baris)]
    
    j = 0
    if (nama_csv == "user"): kolom = ["id", "username", "nama", "password", "role", "saldo"]
    elif (nama_csv == "game"): kolom = ["id", "nama", "kategori", "tahun_rilis", "harga", "stok"]
    elif (nama_csv == "riwayat"): kolom = ["game_id", "nama", "harga", "user_id", "tahun_beli"]
    elif (nama_csv == "kepemilikan"): kolom = ["game_id", "user_id"]

    for i in range(baris):
        #print("i =", i)
        # Buat dictonary di dalam data
        if (nama_csv == "user"): 
            data[i] = {
                "id" : 0,
                "username": "",
                "nama": "",
                "password": "",
                "role": "",
                "saldo": 0
            }
        elif (nama_csv == "game"): 
            data[i] = {
                "id" : 0,
                "nama": "",
                "kategori": "",
                "tahun_rilis": 0,
                "harga": "",
                "stok": 0
            }
        elif (nama_csv == "riwayat"): 
            data[i] = {
                "game_id" : "",
                "nama" : "",
                "harga" : 0,
                "user_id" : "",
                "tahun_beli" : 0
            }
        elif (nama_csv == "kepemilikan"): 
            data[i] = {
                "game_id" : "",
                "user_id" : ""
            }

        isi = ""
        # Definisikan setiap Dictonary
        s = arr[i+1]
        # print(s)
        #print(s)
        for c in s:
            if (c == "\n"): break
            if (c != ';'): 
                isi += c
            elif (c == ";"):
                #print("\tdata[", i, "][", kolom[j], "] =" ,isi)
                data[i][kolom[j]] = isi
                isi = ""
                j += 1
            else:
                break
        data[i][kolom[j]] = isi
        #print("\tdata[", i, "][", kolom[j], "] =" ,isi)
        j = 0
        

    #print(data[0]["saldo"])
    return data

def array_to_string(database, file):
    ans = ""
    i = 0
    for a in database[file]:
        b = ";"
        if (i != 0): ans += "\n"
        if (file == "game"):
            ans += a["id"]+b+a["nama"]+b+a["kategori"]+b+a["tahun_rilis"]+b+a["harga"]+b+a["stok"]
        elif (file == "user"):
            ans += a["id"]+b+a["username"]+b+a["nama"]+b+a["password"]+b+a["role"]+b+a["saldo"]
        elif (file == "riwayat"):
            ans += a["game_id"]+b+a["nama"]+b+a["harga"]+b+a["user_id"]+b+a["tahun_beli"]
        elif (file == "kepemilikan"):
            ans += a["game_id"]+b+a["user_id"]
        i += 1
    
    return ans

def string_to_csv(file, direc, data):
    f = open(direc+file+".csv", "w")
    f.write(data)
    f.close()

def push_data(nama, database, data):

    len = length(database[nama]) + 1
    temp = ["" for i in range(len)]

    i = 0
    for arr in database[nama]:
        temp[i] = arr
        i += 1
    
    if (nama == "kepemilikan"):
        temp[i] = {
            "game_id": data[0],
            "user_id": data[1]
        }
    
    elif (nama == "riwayat"):
        temp[i] = {
            "game_id": data[0],
            "nama": data[1],
            "harga": data[2],
            "user_id": data[3],
            "tahun_beli": data[4]
        }
    
    elif (nama == "user"):
        temp[i] = {
            "id" : data[0],
            "username" : data[1],
            "nama" : data[2],
            "password" : data[3],
            "role" : data[4],
            "saldo" : data[5]
        }

    elif (nama == "game"):
        temp[i] = {
            "id" : data[0],
            "nama" : data[1],
            "kategori" : data[2],
            "tahun_rilis" : data[3],
            "harga" : data[4],
            "stok" : data[5]
        }

    database[nama] = temp
    return database[nama]