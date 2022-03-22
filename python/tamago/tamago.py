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