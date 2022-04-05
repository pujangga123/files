# class Puppy
# turunan dari Tamago, berarti mewarisi semua atribut dan fungsi dari Tamago
# dengan tambahan method play dan run
from tamago import Tamago

class Puppy(Tamago):    
    happy = 100

    # khusus pada deklarasi method pada class,
    #   parameter pertama selalu self, tapi ketika dipanggil, parameter ini dianggap kosong
    def play(self):
        self.life -=2
        self.happy += 20
        self.energy -= 15
        print(self.name," BERMAIN")

    def run(self, distance):
        self.life -=2
        self.happy += 5
        self.energy -= 2*distance
        print(self.name,"BERLARI SEJAUH",distance,"KM")

