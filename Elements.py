import pygame


pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Add Elements to My Screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 32)
text = font.render("Welcome to My Game", True, BLACK)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (300, 250, 200, 100))

    screen.blit(text, (250, 150))

    pygame.display.update()

pygame.quit()
