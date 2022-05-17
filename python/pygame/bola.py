import pygame

class Bola:
    def __init__(self, screen):
        self.x = 120 # property: posisi x pusat bola
        self.y = 120 # property: posisi y pusat bola
        self.xspeed = 5
        self.yspeed = 5
        self.radius = 10 # property: radius bola
        self.color = (0,0,255) # property: warna bola
        self.screen = screen # property: link ke objek screen, tempat bola berada

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def xbounce(self):
        self.xspeed *= -1
    
    def ybounce(self):
        self.yspeed *= -1

    def draw(self):
        pygame.draw.circle(self.screen,self.color, (self.x,self.y),self.radius)

