
import os
from puppy import Puppy

def cetakmenu():
    print("="*40)
    print("1. Makan")
    print("2. Bermain")
    print("3. Skip day")
    print("0. QUIT")

# PROGRAM UTAMA
nino = Puppy("Nino")
opsi = ""

while True:
    nino.draw()
    cetakmenu()
    opsi = input("Opsi (1-3)?")
    os.system("cls")    

    if opsi == "1":
        nino.eat()

    if opsi == "2":
        nino.play()

    if opsi == "3":
        nino.skipday()

    if opsi == "0":
        break


    

print("GAME OVER")