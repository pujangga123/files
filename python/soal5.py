class Animal:
    weight = 10
    alive = True
    length = 2

    def eat(self, kilo):
        self.weight += kilo 

    def run(self,distance):
        self.weight -= distance

    def die(self):
        self.alive = False

mamal = Animal()
mamal.eat(5)
print(mamal.weight)
mamal.run(10)
print(mamal.weight)
print(mamal.length)
mamal.die()