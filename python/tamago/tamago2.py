# contoh game Tamagoci
# class dan program utama dipisah menjadi 2 file

import os
from tamago import Tamago

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
