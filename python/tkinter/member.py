from datetime import date

class Member:
    def __init__(self, db):
        self.id = ""
        self.nama = ""
        self.jenis_keanggotaan = ""
        self.tanggal_pembayaran = ""
        self.iuran = 0
        self.kedatangan = 0
        self.trainer = ""

        self.db = db

    def load(self,id):
        self.id = id
        self.nama = self.db[id]['nama']
        self.kedatangan = int(self.db[id]['kedatangan'])
        self.tanggal_pembayaran = self.db[id]['tanggal_pembayaran']
        self.trainer = self.db[id]['trainer']
        self.jenis_keanggotaan = self.db[id]['jenis_keanggotaan']
        self.iuran = int(self.db[id]['iuran'])

    def update(self):
        if self.jenis_keanggotaan == 'reguler':
            self.iuran = 500000
        else:
            self.iuran = 1200000

        # update hanya bisa menyimpan nama, jenis keanggotaan dan nama trainer
        print(self.kedatangan)
        self.db[self.id] = {
            "nama" : self.nama,
            "jenis_keanggotaan" : self.jenis_keanggotaan,
            "iuran" : int(self.iuran),
            "trainer": self.trainer,
            "kedatangan": int(self.kedatangan),
            "tanggal_pembayaran" : self.tanggal_pembayaran
        }
        print(self.db)


    def tambah_kedatangan(self):
        self.kedatangan = self.kedatangan + 1

        self.db[self.id]["kedatangan"] =  self.kedatangan

    def bayar(self):
        self.tanggal_pembayaran = date.today().strftime("%Y-%m-%d")

        self.db[self.id]["tanggal_pembayaran"] = self.tanggal_pembayaran