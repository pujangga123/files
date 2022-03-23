# contoh game Tamagoci
# pada program ini karakter tamagoci menggunakan class Cat
# yang adalah turunan dari class Tamago
import os
from cat import Cat

def cetakmenu():
    print("="*40)
    print("1. Makan")
    print("2. Bermain")
    print("3. Skip day")
    print("0. QUIT")

# PROGRAM UTAMA
neko = Cat("Neko")
opsi = ""

while True:
    neko.draw()
    cetakmenu()
    opsi = input("Opsi (1-3)?")
    os.system("cls")    

    if opsi == "1":
        neko.eat()

    if opsi == "2":
        neko.play()

    if opsi == "3":
        neko.skipday()

    if opsi == "0":
        break


    

print("GAME OVER")