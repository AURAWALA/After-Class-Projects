import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Custom Event - Color Change")


WHITE = (255, 255, 255)


x1, y1 = 200, 250
x2, y2 = 500, 250


color1 = (0, 0, 255)
color2 = (255, 0, 0)


CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  # Trigger every 2 seconds


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


    screen.fill(WHITE)


    pygame.draw.rect(screen, color1, (x1, y1, 80, 80))
    pygame.draw.rect(screen, color2, (x2, y2, 80, 80))


    pygame.display.update()

pygame.quit()
