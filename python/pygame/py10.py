# contoh program seperti pg9.py 
# tambahan:
#    radius, color, xspeed, yspeed menjadi properti bola
#    fungsi move ditambahkan untuk melakukan pergerakan

# inisialisasi
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

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

bola = Bola(screen)
bola.x = 150  #posisi awal bola bisa dirubah dengan cara seperti ini
bola.yspeed = 7  # kecepatan awalnya juga bisa dirubah

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

    if bola.y<0 or bola.y>500:
        bola.ybounce()

    bola.move()
    bola.draw()

    # update windows
    pygame.display.flip()
    clock.tick(20) 

pygame.quit()

