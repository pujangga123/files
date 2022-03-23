# class Cat
# turunan dari Tamago, berarti mewarisi semua atribut dan fungsi dari Tamago
# dengan tambahan method eat dan hunting
# fungsi eat pada class merupakan fungsi overloading. Walaupun superclass (Tamago)
# memiliki fungsi eat, pada class Cat fungsi eat nya berbeda.
from tamago import Tamago

class Cat(Tamago):
    happy = 50

    def eat(self):
        super().eat()
        print("... KEMUDIAN TIDUR")

    def hunting(self, target):
        self.life -=2
        self.happy += 15
        self.energy -= 15
        print(self.name,"BERBURU", target)

    def draw(self):
        print("""
╭━━━╮┈┈╱╲┈┈┈╱╲
┃╭━━╯┈┈▏▔▔▔▔▔▕
┃╰━━━━━▏╭▆┊╭▆▕
╰┫╯╯╯╯╯▏╰╯▼╰╯▕
┈┃╯╯╯╯╯▏╰━┻━╯▕
┈╰┓┏┳━┓┏┳┳━━━╯
┈┈┃┃┃┈┃┃┃┃┈┈┈┈
┈┈┗┻┛┈┗┛┗┛┈┈┈┈
        """)
        super().draw()
        