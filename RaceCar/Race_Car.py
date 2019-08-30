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

def button(button_left,button_top,button_width,button_height,text,starting_color,active_color,action):
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    text_surface = smalltext.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (button_left + button_width/2, button_top + button_height/2)

    if button_left + button_width >= mouse_position[0] >= button_left and button_top + button_height >= mouse_position[1] >= button_height:
        drawRect(button_left, button_top, button_width, button_height, active_color)

        if click[0] == 1 and action != None:
            action()
    else:
        drawRect(button_left, button_top, button_width, button_height, starting_color)

    gameDisplay.blit(text_surface, text_rect)

def gameIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()

        largeStyle = pygame.font.Font("freesansbold.ttf", 115)
        text_surface = largeStyle.render("RACE CAR", True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (display_width / 2, display_height / 2)
        gameDisplay.fill(WHITE)
        gameDisplay.blit(text_surface, text_rect)

        button(150,450,100,50,"START!",(0,200,0),(0,255,0),gameLoop)
        button(550, 450, 100, 50, "ABOUT", (200,0, 0), (255,0, 0),None)

        pygame.display.update()
        clock.tick(15)

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

gameIntro()
