class Mahasiswa:
    def __init__(self,db):
        self.db = db
        self.nama = ""
        self.nim = ""
        self.nilai = 0

    def load(self,nim):
        self.nim = nim
        self.nama = self.db[nim]['nama']
        self.nilai = self.db[nim]['nilai']

    def update(self):
        self.db[self.nim] = {
            "nama" : self.nama,
            "nilai" : self.nilai
        }

    def delete(self,nim):
        del self.db[nim]