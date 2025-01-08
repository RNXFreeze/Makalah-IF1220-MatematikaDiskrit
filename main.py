# PROGRAM K01-MIF2123-F01

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : main.py
# Topik     : Makalah Matematika Diskrit 2024 (IF1220-24)
# Tanggal   : Rabu, 8 Januari 2025
# Deskripsi : Subprogram F01 - Main Program

# KAMUS
# main : procedure
# __name__ : string

# ALGORITMA
from src.graph import *

def main() :
    # DESKRIPSI LOKAL
    # Fungsi utama main program.

    # KAMUS LOKAL
    # arg : integer
    # query , database : string

    # ALGORITMA LOKAL
    arg = 1
    print("Selamat Datang!!")
    while (arg != 3) :
        print("====================================")
        print("Pilihan Menu :")
        print("1. Pencarian Rute Terpendek")
        print("2. Pencarian Pohon Merentang Minimum")
        print("3. Exit Program")
        print("====================================")
        arg = int(input("Masukkan pilihan Anda (1 / 2 / 3) : "))
        while (not(1 <= arg <= 3)) :
            print("Maaf, input Anda tidak valid!")
            arg = int(input("Masukkan pilihan Anda (1 / 2) : "))
        if (arg == 1) :
            print("===================================================")
            print("Selamat Datang di Menu 1 : Pencarian Rute Terpendek")
            print("===================================================")
            query = str(input("Masukkan path data graph : "))
            a = int(input("Masukkan id titik awal : "))
            b = int(input("Masukkan id titik akhir : "))
            graph = Graph(query)
            resd = graph.dijkstra(a , b)
            resa = graph.a_star(a , b)
            print(f"Hasil Dijkstra = {resd}.")
            print(f"Hasil A-Star = {resa}.")
        elif (arg == 2) :
            print("============================================================")
            print("Selamat Datang di Menu 2 : Pencarian Pohon Merentang Minimum")
            print("============================================================")
            query = str(input("Masukkan path data graph : "))
            graph = Graph(query)
            _ , resp = graph.prim()
            _ , resk = graph.kruskal()
            print(f"Hasil Prim = {resp}.")
            print(f"Hasil Kruskal = {resk}.")
        else :
            print("============================================")
            print("Menu 3 : Terima Kasih & Sampai Jumpa Kembali")
            print("============================================")
            break

if (__name__ == "__main__") :
    main()