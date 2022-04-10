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
        s += ";"
        # print(s)
        #print(s)
        for c in s:
            #print("\tc =", c)
            if (c != ';'): 
                isi += c
            else:
                #print("\tj =", j)
                data[i][kolom[j]] = isi
                #print("\tdata[" + str(i) + "][" + kolom[j] + "] =", data[i][kolom[j]])
                isi = ""
                j += 1
        j = 0

    #print(data[0]["saldo"])
    return data


