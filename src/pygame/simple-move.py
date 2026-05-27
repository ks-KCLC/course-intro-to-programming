import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("キャラクター移動")

x, y = 300, 220
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    screen.fill(pygame.Color("black"))
    pygame.draw.rect(screen, pygame.Color("white"), (x, y, 40, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
