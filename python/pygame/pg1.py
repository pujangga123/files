# inisialisasi
import pygame
pygame.init()
screen = pygame.display.set_mode([600,500])
clock = pygame.time.Clock()
 
running = True
x = 13

speedx = 5
while running: # selama running bernilai True, ulangi proses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( (125,125,125) )   

    x = x + speedx   

    pygame.draw.circle(screen,(0,0,255), (x,10),10)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
