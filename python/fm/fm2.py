import os
import random

# inisialisasi dictionary db
db = {}

# act digunakan untuk menu
act = 0

# deklarasi class Club
class Club:
    id = ""
    nama = ""
    win = 0
    lost = 0
    draw  = 0

    # constructor
    def __init__(self, id):
        self.id = id

        # periksa id, kalau ada di database maka load data
        if id in db:
            self.nama = db[id]['nama']
            self.win = db[id].get('win',0)
            self.lost = db[id].get('lost',0)
            self.draw = db[id].get('draw',0)

    # function menang
    def menang(self):
        self.win += 1
        db[self.id]['win'] = self.win # update ke database

    # function kalah
    def kalah(self):
        self.lost += 1
        db[self.id]['lost'] = self.lost # update ke database
    
    # function seri
    def seri(self):
        self.draw += 1
        db[self.id]['draw'] = self.draw # update ke database

    def update(self):
        db[self.id] = {'nama':self.nama }

# fungsi untuk mencetak menu
def cetakmenu():
    os.system("cls")  # membersihkan layar

    # Cetak Header Tabel
    print("Code","Nama".ljust(20),"Win ","Lost","Draw")
    for i in db:        
        print(str(i).rjust(4),db[i]['nama'].ljust(20), str(db[i].get('win',0)).rjust(4),str(db[i].get('lost',0)).rjust(4),str(db[i].get('draw',0)).rjust(4))
    print("="*30)
    print("1. Club baru/edit")
    print("2. Hapus Club")
    print("3. Set Pertandingan")
    print("Q. Quit")
    print("="*30)
    print()

while True:
    random.seed()

    cetakmenu()
    
    # meminta user memasukan angka sesuai menu
    act = input("Pilihan?")

    # tambah/edit club
    if act == "1":
        print()
        kode = input("Kode:")
        nama = input("Nama:")

        #buat objek club dari class Club
        club = Club(kode)
        club.nama = nama  # set nama
        club.update()     # simpan ke database

    # hapus club
    if act == "2":
        print()
        kode = input("Kode:")
        del db[kode]

    # set pertandingan
    if act == "3":
        kode1 = input("Tim 1, Kode:")  # tanya kode tim 1
        kode2 = input("Tim 2, Kode:")  # tanya kode tim 2

        # buat objek untuk masing-masing tim
        tim1 = Club(kode1)
        tim2 = Club(kode2)
        print("Pertandingan",tim1.nama,"melawan",tim2.nama)

        # generate score secara random
        score1 = random.randint(0,5)
        score2 = random.randint(0,5)
        print("Score:", score1,"vs",score2)

        # jika score tim 1 lebih besar dari score tim 2, maka pemenang adalah tim 1
        if score1>score2:
            print("Pemenang:",tim1.nama)
            tim1.menang()            
            tim2.kalah()

        # jika score tim 1 lebih kecil dari score tim 2, maka pemenang adalah tim 2
        if score1<score2:
            print("Pemenang:",tim2.nama)
            tim1.kalah()
            tim2.menang()

        # jika score tim 1 sama dengan score tim 2, maka seri
        if score1==score2:
            print("Hasil: Draw")
            tim1.seri()
            tim2.seri()
        print()
        input("ENTER untuk melanjutkan...")

    if act == 'q':
        exit()
