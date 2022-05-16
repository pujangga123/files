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
    pygame.draw.line(screen,(0,0,255), (10,10), (300,200), 2)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
