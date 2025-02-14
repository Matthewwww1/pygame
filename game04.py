import pygame
from pygame.locals import *

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BaiTonginwzaa007")
clock = pygame.time.Clock()
sheet = pygame.image.load('spritesheet.png')
running = True
frame = 0
x,y = 20,40
speed = 10
while running:
    # check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if event.type == pygame.KEYDOWN:
        #    if event.key == K_a or event.key== k_LEFT:
        #    if event.key in [K_a, K_LEFT]: x -= speed
        #    elif event.key in [K_d, K_RIGHT]: x += 2
        #    elif event.key in [K_s, K_DOWN]: y += 2
        #    elif event.key in [K_w, K_UP]: y -= 2

    keys = pygame.key.get_pressed()
    if keys[K_a] or keys[K_LEFT]: x -= speed
    elif keys[K_d] or keys[K_RIGHT]:x += speed
    elif keys[K_s] or keys[K_DOWN]:y += speed
    elif keys[K_w] or keys[K_UP]: y -= speed

    screen.fill((0, 200, 200))
    screen.blit(sheet,(x,y))
    pygame.display.flip()
    clock.tick(30)
    #frame += 1
    #print(frame)