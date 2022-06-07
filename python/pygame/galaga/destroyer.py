import pygame
from drone import Drone

class Destroyer(Drone):
    def __init__(self,screen):
        Drone.__init__(self,screen)
        self.img_drone = pygame.image.load("destroyer.png")
        self.speed = 3
        self.screen = screen
        self.active = True