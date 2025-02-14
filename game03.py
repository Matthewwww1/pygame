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
    #color = Color(255,0,255)
    #rect = pygame.Rect(20,50,200,300)
    pygame.draw.rect(screen, (255,0,255), (20,50,200,300))
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 50))
    screen.fill((0, 200, 200))
    pygame.display.flip()
    clock.tick(30)
    frame += 1
    print(frame)