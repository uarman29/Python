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
pause = False



def placeCar(x,y):
    gameDisplay.blit(carImg,(x,y))

def messageDisplay(text):
    largeStyle = pygame.font.Font("freesansbold.ttf", 115)
    text_surface = largeStyle.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width/2, display_height/2)
    gameDisplay.blit(text_surface, text_rect)


def drawRect(left, top, width, height, color):
    pygame.draw.rect(gameDisplay, color, [left, top, width, height])

def scoreDisplay(score):
    style = pygame.font.SysFont(None,25)
    text = style.render("Score: "+str(score), True, BLACK)
    gameDisplay.blit(text,(0,0))

def button(button_left,button_top,button_width,button_height,text,starting_color,active_color,action,font_size = 20):
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    smalltext = pygame.font.Font("freesansbold.ttf", font_size)
    text_surface = smalltext.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (button_left + button_width/2, button_top + button_height/2)

    if (button_left + button_width >= mouse_position[0] >= button_left) and (button_top + button_height >= mouse_position[1] >= button_top):
        drawRect(button_left, button_top, button_width, button_height, active_color)

        if click[0] == 1 and action != None:
            action()
    else:
        drawRect(button_left, button_top, button_width, button_height, starting_color)

    gameDisplay.blit(text_surface, text_rect)

def gameIntro():
    intro = True
    high_score = 0
    with open("scores.txt") as f:
        lines = f.readlines()
        for line in lines:
            if int(line) > high_score:
                high_score = int(line)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()

        largeStyle = pygame.font.Font("freesansbold.ttf", 115)
        text_surface = largeStyle.render("RACE CAR", True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (display_width / 2, (display_height / 4))
        gameDisplay.fill(WHITE)
        gameDisplay.blit(text_surface, text_rect)

        largeStyle = pygame.font.Font("freesansbold.ttf", 60)
        text_surface = largeStyle.render("HighScore: " + str(high_score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (display_width / 2, (display_height / 2))
        gameDisplay.blit(text_surface, text_rect)

        button(300,400,200,100,"START!",(0,200,0),(0,255,0),gameLoop,30)

        pygame.display.update()
        clock.tick(15)

def crash(score):
    with open("scores.txt","a+") as f:
        f.write("\n"+str(score))
    crashed = True
    largeStyle = pygame.font.Font("freesansbold.ttf", 115)
    text_surface = largeStyle.render("Game Over", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width / 2, (display_height / 2)-60)
    gameDisplay.blit(text_surface, text_rect)
    largeStyle = pygame.font.Font("freesansbold.ttf", 75)
    text_surface = largeStyle.render("Score: " + str(score), True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width / 2, (display_height / 2)+100)
    gameDisplay.blit(text_surface, text_rect)

    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = False
                pygame.quit()
                quit()

        button(150,450,150,50,"REPLAY",(0,200,0),(0,255,0),gameLoop)
        button(550,450,150,50,"MAIN MENU",(200,0,0),(255,0,0),gameIntro)
        pygame.display.update()

def paused():
    global pause
    largeStyle = pygame.font.Font("freesansbold.ttf", 115)
    text_surface = largeStyle.render("PAUSED", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(text_surface, text_rect)

    def resume():
        global pause
        pause = False
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
                quit()

        button(150,450,150,50,"CONTINUE",(0,200,0),(0,255,0),resume)
        button(550,450,150,50,"QUIT",(200,0,0),(255,0,0),gameIntro)
        pygame.display.update()

class Rectangle:
    def __init__(self,x,y,width,height,speed,lane):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.lane = lane

def gameLoop():
    gameOver = False
    x = (display_width*.45)
    y = (display_height*.75)
    current_lane = 1
    num_lanes = 8
    lane_width = 100

    start_time = time.time()
    list_of_rectangles = []
    rect_lane = random.randrange(0, num_lanes)
    rect_startx = rect_lane * lane_width
    rect_starty = -200
    rect_width = 100
    rect_height = 100
    rect_speed = 10
    list_of_rectangles.append(Rectangle(rect_startx,rect_starty,rect_width,rect_height,rect_speed,rect_lane))

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_lane += -1
                elif event.key == pygame.K_RIGHT:
                    current_lane += 1
                elif event.key == pygame.K_SPACE:
                    global pause
                    pause = True
                    paused()

        if current_lane <= 0:
            current_lane = 0
        elif current_lane >= (num_lanes-1):
            current_lane = (num_lanes-1)

        center_of_lane = (current_lane * lane_width) + lane_width/2
        center_of_car = car_width/2
        x = center_of_lane - center_of_car

        gameDisplay.fill(WHITE)
        placeCar(x, y)
        scoreDisplay(int(time.time() - start_time)*10)

        for i in range(0, num_lanes):
            pygame.draw.line(gameDisplay, BLACK, (lane_width * i, 0), (lane_width * i, display_height))

        for i in range(0,len(list_of_rectangles)):
            list_of_rectangles[i].y += list_of_rectangles[i].speed
            drawRect(list_of_rectangles[i].x, list_of_rectangles[i].y, list_of_rectangles[i].width, list_of_rectangles[i].height, (150,0,0))
        pygame.display.update()

        for i in range(0,len(list_of_rectangles)):
            if current_lane == list_of_rectangles[i].lane and list_of_rectangles[i].y + list_of_rectangles[i].height > y and list_of_rectangles[i].y <= (y + car_height):
                pygame.display.update()
                crash((int(time.time() - start_time) * 10))

        for i in range(0, len(list_of_rectangles)):
            if list_of_rectangles[i].y >= display_height:
                list_of_rectangles[i].lane = random.randrange(0, num_lanes)
                list_of_rectangles[i].x = list_of_rectangles[i].lane * lane_width
                list_of_rectangles[i].y = -200
                list_of_rectangles[i].speed = 10 + int((time.time() - start_time) / 5)


        if ((time.time() - start_time) > 10*len(list_of_rectangles)) and len(list_of_rectangles) < 6:
            rect_lane = random.randrange(0, num_lanes)
            rect_startx = rect_lane * lane_width
            rect_starty = -200
            rect_width = 100
            rect_height = 100
            rect_speed = 10 + int((time.time() - start_time) / 5)
            list_of_rectangles.append(Rectangle(rect_startx, rect_starty, rect_width, rect_height, rect_speed, rect_lane))

        scoreDisplay(int(time.time() - start_time)*10)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

gameIntro()
