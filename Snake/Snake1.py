from pygame.locals import *
import pygame
import time

##SNAKE
class Player:
    x = 0
    y = 0
    speed = 32
    direction = 0

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3


class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption("Snake")
        self.running = True
        self.image_surf = pygame.image.load("square.png").convert()

    def on_event(self,event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.display_surf.fill((0, 0, 0))
        self.display_surf.blit(self.image_surf,(self.player.x,self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.moveRight()

            if keys[K_LEFT]:
                self.player.moveLeft()

            if keys[K_UP]:
                self.player.moveUp()

            if keys[K_DOWN]:
                self.player.moveDown()

            self.player.update()
            self.on_loop()
            self.on_render()
            time.sleep(50.0 / 1000.0)
        self.on_cleanup()


if __name__ == "__main__":
    app1 = App()
    app1.on_execute()