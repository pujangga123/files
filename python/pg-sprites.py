# inisialisasi
import pygame
pygame.init()
screen = pygame.display.set_mode([100,100])
clock = pygame.time.Clock()

# inisisalisasi variable
mario = [pygame.image.load('mario1.png'),
         pygame.image.load('mario2.png'),
         pygame.image.load('mario3.png')]
n = 0
running = True
while running:
    # event checking
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False
   
    screen.fill((255,255,255))
    n += 1
    if n>=len(mario):
        n = 0
    screen.blit(mario[n],(10,10))    
    pygame.display.flip() # refresh form
    clock.tick(10) # kecepatan

pygame.quit()

