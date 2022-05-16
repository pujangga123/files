# inisialisasi
import pygame
pygame.init()
screen = pygame.display.set_mode([600,500])
clock = pygame.time.Clock()
 
running = True
while running: # selama running bernilai True, ulangi proses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( (125,125,125) )   
    pygame.draw.rect(screen,(0,0,255), (20,20,300,300))
    pygame.draw.rect(screen,(0,255,255), (20,400,50,50),3)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
