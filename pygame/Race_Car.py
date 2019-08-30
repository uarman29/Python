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