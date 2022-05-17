# contoh program seperti pg10.py 
# tambahan:
#    class Bola di pisah pada file bola.py

# inisialisasi
import pygame

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

stage = pygame.image.load("world.png")
mario = pygame.image.load("mario0.png")

running = True
while running: # selama running bernilai True, ulangi proses

    # check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # isi screen dengan kode warna RGB 255,255,255 (warna putih)
    screen.blit(stage,(0,0))    
    screen.blit(mario,(200,400))
    
    # update windows
    pygame.display.flip()
    clock.tick(20) 

pygame.quit()

