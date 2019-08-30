import pygame
import time

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load("car.png")

car_width = 100
car_height = 125


def placeCar(x,y):
    gameDisplay.blit(carImg,(x,y))

def messageDisplay(text):
    largeStyle = pygame.font.Font("freesansbold.ttf", 115)
    text_surface = largeStyle.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width/2, display_height/2)
    gameDisplay.blit(text_surface, text_rect)

def gameLoop():
    crashed = False
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
                if (x_change == -5 and event.key == pygame.K_LEFT) or (x_change == 5 and event.key == pygame.K_RIGHT):
                    x_change = 0
                if (y_change == -5 and event.key == pygame.K_UP) or (y_change == 5 and event.key == pygame.K_DOWN):
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

        if x <= -20 or x >= display_width - car_width or y <= 0 or y >= display_height - car_height:
            messageDisplay("GO BACK")

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

gameLoop()