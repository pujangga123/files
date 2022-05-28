import pygame

class Drone:  # nama class
    def __init__(self,screen):
        self.img_drone = pygame.image.load("drone1.png")
        self.x = 0
        self.y = 0
        self.speed = 7
        self.screen = screen

    def move(self):
        self.x += self.speed
        if self.x<10 or self.x>470:
            self.bounce()

    def bounce(self):
        self.speed *= -1

    def draw(self):
        self.screen.blit(self.img_drone,(self.x,self.y))