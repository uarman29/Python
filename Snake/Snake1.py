from pygame.locals import *
import pygame
import time

##SNAKE
class Apple():
    x = 0
    y = 0
    apple_width = 30

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class Player:
    x = [0]
    y = [0]
    block_width = 35
    direction = 0
    length = 3


    def __init__(self,length):
        self.length = length
        for i in range(0,length):
            self.x.append(0)
            self.y.append(0)

        self.x[1] = self.block_width * -1
        self.x[2] = self.block_width * -2

    def update(self):
        for j in range(0,2):
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            if self.direction == 0:
                self.x[0] = self.x[0] + self.block_width
            if self.direction == 1:
                self.x[0] = self.x[0] - self.block_width
            if self.direction == 2:
                self.y[0] = self.y[0] - self.block_width
            if self.direction == 3:
                self.y[0] = self.y[0] + self.block_width


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3


    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.player = Player(3)
        self.apple = Apple(400,400)

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption("Snake")
        self.running = True
        self.image_surf = pygame.image.load("square.png").convert()
        self.apple_surf = pygame.image.load("square.png").convert()

    def on_event(self,event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        self.player.update()

        for i in range(0, self.player.length):
            if self.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], self.apple.apple_width):
                self.apple.x = randint(0,self.windowWidth-self.apple.apple_width)
                self.apple.y = randint(0,self.windowHeight-self.apple.apple_width)
                self.player.length = self.player.length + 1

        for i in range(2,self.player.length):
            if self.isCollision(self.player.x[0],self.player.y[0],self.player.x[i],self.player.y[i],self.player.block_width):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)


    def on_render(self):
        self.display_surf.fill((0, 0, 0))
        self.player.draw(self.display_surf, self.image_surf)
        self.apple.draw(self.display_surf, self.apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2+bsize:
            if y1 >= y2 and y1<= y2+bsize:
                return True
        return False

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

            self.on_loop()
            self.on_render()
            time.sleep(50.0 / 1000.0)
        self.on_cleanup()


if __name__ == "__main__":
    app1 = App()
    app1.on_execute()