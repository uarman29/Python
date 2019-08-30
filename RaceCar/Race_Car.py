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

car_width = 100
car_height = 125

def placeCar(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (display_width*.45)
y = (display_height*.45)
x_change = 0
y_change = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0


    x += x_change
    y += y_change

    if x < -20:
        x = -20
    elif x > display_width - car_width:
        x = display_width - car_width

    if y < 0:
        y = 0
    elif y > display_height - car_height:
        y = display_height - car_height

    gameDisplay.fill(WHITE)
    placeCar(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()