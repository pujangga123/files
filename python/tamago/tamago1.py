# contoh game Tamago
# Pada program ini class dan digabung pada class utama
# check tamago2.py & tamago.py untuk contoh dimana class dan program utama di pisah
import os
class Tamago:
    name = ""
    life = 100
    energy = 100
    
    def __init__(self,name):
        self.name = name

    def eat(self):
        self.life -= 1
        self.energy += 10
        print(self.name,"MAKAN")
    

    def skipday(self):
        self.life -= 2
        self.energy -= 15
        print(self.name,"MELEWATI HARI")


    def die(self):
        print(self.name,"MATI")
        input()

    def draw(self):
        print(self.name, "HP:",self.life," - Energy:",self.energy)

def cetakmenu():
    print("="*40)
    print("1. Makan")
    print("2. Skip day")
    print("0. QUIT")

# PROGRAM UTAMA
beno = Tamago("Beno")
opsi = ""

while True:    
    beno.draw()
    cetakmenu()
    opsi = input("Opsi (1-2)?")

    os.system("cls")   

    if opsi == "1":
        beno.eat()

    if opsi == "2":
        beno.skipday()

    if opsi == "0":
        break


print("GAME OVER")
