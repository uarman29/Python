import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load("car.png")

car_width = 60
car_height = 114


def placeCar(x,y):
    gameDisplay.blit(carImg,(x,y))

def messageDisplay(text):
    largeStyle = pygame.font.Font("freesansbold.ttf", 115)
    text_surface = largeStyle.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width/2, display_height/2)
    gameDisplay.blit(text_surface, text_rect)

#def makeRect(left, top, width, height):
#    return pygame.rect(left,top,width,height)

def drawRect(left, top, width, height, color):
    pygame.draw.rect(gameDisplay, color, [left, top, width, height])

def laneManker():
    laneNumber = display_width/8


def gameLoop():
    crashed = False
    x = (display_width*.45)
    y = (display_height*.75)
    current_direction = 0
    current_lane = 1
    num_lanes = 8
    lane_width = 100

    rect_lane = random.randrange(0, num_lanes)
    rect_startx = rect_lane * lane_width
    rect_starty = -200
    rect_width = 100
    rect_height = 100
    rect_speed = 7

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_direction = -1
                elif event.key == pygame.K_RIGHT:
                    current_direction = 1

            if event.type == pygame.KEYUP:
                if (current_direction == -1 and event.key == pygame.K_LEFT) or (current_direction == 1 and event.key == pygame.K_RIGHT):
                    current_lane += current_direction

        if current_lane <= 0:
            current_lane = 0
        elif current_lane >= (num_lanes-1):
            current_lane = (num_lanes-1)

        center_of_lane = (current_lane * lane_width) + lane_width/2
        center_of_car = car_width/2
        x = center_of_lane - center_of_car

        gameDisplay.fill(WHITE)
        placeCar(x, y)

        drawRect(rect_startx, rect_starty, rect_width, rect_height, BLACK)
        rect_starty += rect_speed

        for i in range(0, num_lanes):
            pygame.draw.line(gameDisplay, BLACK, (lane_width * i, 0), (lane_width * i, display_height))

        pygame.display.update()

        if current_lane == rect_lane and rect_starty+rect_height > y and rect_starty <= display_height:
            messageDisplay("DEAD")
            pygame.display.update()
            crashed = True

        if rect_starty >= display_height:
            rect_lane = random.randrange(0, num_lanes)
            rect_startx = rect_lane * lane_width
            rect_starty = -200

        clock.tick(60)

    pygame.quit()
    quit()

gameLoop()