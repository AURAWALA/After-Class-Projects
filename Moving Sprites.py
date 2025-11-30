import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Two Moving Rectangular Sprites")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

x1, y1 = 100, 250
x2, y2 = 600, 250
speed = 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        x1 -= speed
    if keys[pygame.K_RIGHT]:
        x1 += speed
    if keys[pygame.K_UP]:
        y1 -= speed
    if keys[pygame.K_DOWN]:
        y1 += speed


    if keys[pygame.K_a]:
        x2 -= speed
    if keys[pygame.K_d]:
        x2 += speed
    if keys[pygame.K_w]:
        y2 -= speed
    if keys[pygame.K_s]:
        y2 += speed

    screen.fill(WHITE)


    pygame.draw.rect(screen, BLUE, (x1, y1, 60, 60))
    pygame.draw.rect(screen, RED, (x2, y2, 60, 60))


    pygame.display.update()


pygame.quit()