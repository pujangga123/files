# contoh program seperti pg10.py 
# tambahan:
#    class Bola di pisah pada file bola.py

# inisialisasi
import pygame
from bola import Bola

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

bola = Bola(screen)
bola.x = 150  #posisi awal bola bisa dirubah dengan cara seperti ini
bola.yspeed = 0

running = True
while running: # selama running bernilai True, ulangi proses

    # check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # isi screen dengan kode warna RGB 255,255,255 (warna putih)
    screen.fill((255,255,255))    

    # periksa apakah posisi bolah berada di luar layar?
    # jika ya, maka panggil fungsi xbounce / ybounce untuk membalikan arah
    # gerak bola (merubah xspeed / yspeed)
    if bola.x<0 or bola.x>500:
        bola.xbounce()

    bola.move()
    bola.draw()

    # update windows
    pygame.display.flip()
    clock.tick(20) 

pygame.quit()

