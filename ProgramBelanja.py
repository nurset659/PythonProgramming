import sys
total = []
print("""
Toko Veryhanzai
-----------------------------
""")
print("Nama : Nuk")
print("Nim : 1234")

def daftar_barang():
    print(" NO | NAMA BARANG | HARGA ")
    print(" 1 | Ale-Ale | 1000 ")
    print(" 2 | Aqua | 3000 ")
    print(" 3 | Le Mineral | 3500 ")
    print(" 4 | Susu Beruang | 4500 ")
    print(" 5 | Coca Cola | 5000 ")
    print(" 6 | Pulpy Orange | 5500 ")
    kode = int(input("Masukan angka barang : "))
    if kode == 1:
        jumlah1 = int(input("masukan jumlah barang :"))
        total1 = 1000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("masukan jumlah barang :"))
        total2 = 3000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("masukan jumlah barang :"))
        total3 = 3500 * jumlah3
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("masukan jumlah barang :"))
        total4 = 4500 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("masukan jumlah barang :"))
        total5 = 5000 * jumlah5
        total.append(total5)
        tanya()
    elif kode == 6:
        jumlah6 = int(input("masukan jumlah barang :"))
        total6 = 5500 * jumlah6
        total.append(total6)
        tanya()
    return

def tanya():
    print("\n---------------")
    tanya = input("ingin tambah barang lagi? [y/t] : ")
    print("---------------------")
    if tanya == "y" :
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print(" pilihan yang anda masukan salah! ")

def akhir():
    for harga in total:
        print("subtotal : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 100000:
            diskon = a * 8/100
        elif a > 500000:
            diskon = a * 5/100
        else:
            diskon = 0
        print("potongan harga :", diskon)
        totalakhir = a - diskon
        print("total : ", totalakhir)
        print("---------------")
        bayar = int(input("bayar : "))
        kembalian = bayar - totalakhir
        print("kembalian : ", kembalian)

daftar_barang()
