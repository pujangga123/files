from tamago import Tamago

class Puppy(Tamago):    
    happy = 100

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

