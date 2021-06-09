# inisialisasi
import pygame
pygame.init()
screen = pygame.display.set_mode([1024,568])
clock = pygame.time.Clock()

running = True
x = 10
y = 10
while running:
    # event checking
    for event in pygame.event.get():                
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_LEFT]:
        x -= 10
   
    # program menggambar, disini
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,255),(x,y),10)
    
    pygame.display.flip() # refresh form
    clock.tick(10) # kecepatan

pygame.quit()

