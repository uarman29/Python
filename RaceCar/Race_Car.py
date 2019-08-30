import pygame
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load("car.png")


def placeCar(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (display_width*.45)
y = (display_height*.70)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(WHITE)
    placeCar(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()