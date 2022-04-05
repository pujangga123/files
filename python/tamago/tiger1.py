# contoh game Tamagoci
# pada program ini karakter tamagoci menggunakan class Cat
# yang adalah turunan dari class Tamago
import os
from tiger import Tiger

def cetakmenu():
    print("="*40)
    print("1. Makan")
    print("2. Bermain")
    print("3. Berlari")
    print("4. Skip day")
    print("0. QUIT")

# PROGRAM UTAMA
jack = Tiger("Jack")
opsi = ""

while True:
    jack.draw()
    cetakmenu()
    opsi = input("Opsi (1-3)?")
    os.system("cls")    

    if opsi == "1":
        jack.eat()

    if opsi == "2":
        jack.play()

    if opsi == "3":
        jarak = int(input("Jarak:"))
        jack.run(jarak)

    if opsi == "4":
        jack.skipday()

    if opsi == "0":
        break


    

print("GAME OVER")