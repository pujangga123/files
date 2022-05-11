# contoh program seperti pg1.py tapi dengan implementasi OOP

# inisialisasi
import pygame

class Bola:
    def __init__(self, screen):
        self.x = 120
        self.y = 120
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen,(0,0,255), (self.x,self.y),10)

pygame.init()
screen = pygame.display.set_mode([500,500])
bola = Bola(screen)

running = True
while running: # selama running bernilai True, ulangi proses

    # check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # isi screen dengan kode warna RGB 100,100,100
    screen.fill((100,100,100))    

    # gambar lingkaran
    bola.draw()

    # update windows
    pygame.display.flip()

pygame.quit()

