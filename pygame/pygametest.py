#---------------------------------------------------------------------------------------------------#
'''
#################################GETTING A WINDOW#######################################################
import pygame
from pygame.locals import *

pygame.init() #Initialize all pygame modules

gameDisplay = pygame.display.set_mode((800, 600))  # Create a window
pygame.display.set_caption("Race Game")  # Set title of window

clock = pygame.time.Clock()  # Create a clock
crashed = False  # Variable to check if program has crashed

while not crashed:
    for event in pygame.event.get():  # For each event in all the events that happened
        if event.type == pygame.QUIT:  # If the event is closing the window
            crashed = True
        print(event)
    pygame.display.update()  # Update the display
    clock.tick(60)  # 60 FPS?
'''
#---------------------------------------------------------------------------------------------------#
'''
#################################IMAGE ON SCREEN#######################################################
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
'''
#---------------------------------------------------------------------------------------------------#
'''
#################################MOVING & BOUNDRIES#######################################################
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
'''
#---------------------------------------------------------------------------------------------------#
'''
#################################ADDING TEXT#######################################################
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
'''

#---------------------------------------------------------------------------------------------------#
'''
#################################BOXES AND COLLISIONS#######################################################
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
'''
#---------------------------------------------------------------------------------------------------#

#################################ADDED SCORE & CONTINOUS RECTANGLES#######################################################
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

def scoreDisplay(score):
    style = pygame.font.SysFont(None,25)
    text = style.render("Score: "+str(score), True, BLACK)
    gameDisplay.blit(text,(0,0))

def gameLoop():
    crashed = False
    x = (display_width*.45)
    y = (display_height*.75)
    current_lane = 1
    num_lanes = 8
    lane_width = 100

    rect_lane = random.randrange(0, num_lanes)
    rect_startx = rect_lane * lane_width
    rect_starty = -200
    rect_width = 100
    rect_height = 100
    rect_speed = random.randrange(10, 20)
    dodged = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_lane += -1
                elif event.key == pygame.K_RIGHT:
                    current_lane += 1

        if current_lane <= 0:
            current_lane = 0
        elif current_lane >= (num_lanes-1):
            current_lane = (num_lanes-1)

        center_of_lane = (current_lane * lane_width) + lane_width/2
        center_of_car = car_width/2
        x = center_of_lane - center_of_car

        gameDisplay.fill(WHITE)
        placeCar(x, y)
        scoreDisplay(dodged)

        for i in range(0, num_lanes):
            pygame.draw.line(gameDisplay, BLACK, (lane_width * i, 0), (lane_width * i, display_height))

        rect_starty += rect_speed
        drawRect(rect_startx, rect_starty, rect_width, rect_height, BLACK)
        pygame.display.update()

        if current_lane == rect_lane and rect_starty+rect_height > y and rect_starty <= display_height:
            messageDisplay("DEAD")
            pygame.display.update()
            crashed = True

        if rect_starty >= display_height:
            rect_lane = random.randrange(0, num_lanes)
            rect_startx = rect_lane * lane_width
            rect_starty = -200
            rect_speed = random.randrange(10, 20)
            dodged += 1

        scoreDisplay(dodged)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

gameLoop()


