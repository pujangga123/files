# class Tiger
# turunan dari Tamago, berarti mewarisi semua atribut dan fungsi dari Tamago
# dengan tambahan method play dan run
from tamago import Tamago

class Tiger(Tamago):    
    power = 100

    def run(self, distance):
        self.life -=2
        self.energy -= 2*distance
        print(self.name,"BERLARI SEJAUH",distance,"KM")

    def eat(self):
        self.life -2
        self.power += 20
        self.energy += 20
        print(self.name," MAKAN")  

    def draw(self):
        print("""
              (^\-==-/^)
              >\\ == //<
             :== q''p ==:      _,.---.._
              .__ qp __. ~.-'"'\   |   |''..
                 ^--^  | | \  \ |   , || /  '-. _______ .":
                  ;| | |    | |     |/   .^-./ _)_)__))_).'
                 / \ /      |       \ /  {/ \
             ..-'\_ \   \       ,.--'\ _ ) _/\
            |  ,_../ \- |'---"''"      '-/ \  |
             --       | |            /_.   |-|
                  __' | |   ._ ___   \  )  | |__
          _,______'__ddd'_______._____""__ddd'___SK______
                  __________,______.   _._

        """)
        super().draw()      
 

