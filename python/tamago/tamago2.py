# contoh menggunakan class Tamago di modul terpisah

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
    os.system("cls")    
    beno.draw()
    cetakmenu()
    opsi = input("Opsi (1-3)?")

    if opsi == "1":
        beno.eat()

    if opsi == "2":
        beno.skipday()

    if opsi == "0":
        break

    input()
    

print("GAME OVER")
