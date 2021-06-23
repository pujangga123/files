import pygame

class Fire:
    img = None
    screen = None
    img_index = 0
    mario = None
    rect = pygame.Rect(0,0,16,16) # ukuran fire = 16x16
    direct = 0

    def __init__(self,screen, mario):
        self.screen = screen
        self.img = pygame.image.load('img/fire.png')                
        self.rect.x = mario.x
        self.rect.y = mario.y
        self.direct = mario.direct

    def draw(self):
        self.rect.x += 20
        self.img = pygame.transform.rotate(self.img,90)
        self.screen.blit(self.img, self.rect)
    
    def hit(self,enemyrect):
        return self.rect.colliderect(enemyrect)
