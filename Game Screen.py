import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game Screen")

bg_color = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    pygame.display.update()

pygame.quit()
