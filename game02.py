import pygame
pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BaiTonginwzaa007")
clock = pygame.time.Clock()
running = True
frame = 0
while running:
    # check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 200, 200))
    pygame.display.flip()
    clock.tick(30)
    frame += 1
    print(frame)