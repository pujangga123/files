import os

db = {}
act = 0

class Club:
    id = ""
    nama = ""
    win = 0
    lost = 0
    draw  = 0

    def __init__(self, id):
        self.id = id
        if id in db:
            self.nama = db[id]['nama']
            self.win = db[id]['win']
            self.lost = db[id]['lost']
            self.draw = db[id]['draw']
        

    def update(self):
        db[self.id] = {'nama':self.nama }

def cetakmenu():
    os.system("cls")
    for i in db:        
        print(i,db[i]['nama'])
    print("===============================")
    print("1. Club baru/edit")
    print("2. Hapus Club")
    print("Q. Quit")

while True:
    cetakmenu()
    
    act = input("Pilihan?")

    if act == "1":
        print()
        kode = input("Kode:")
        nama = input("Nama:")
        club = Club(kode)
        club.nama = nama
        club.update()

    if act == 'q':
        exit()
