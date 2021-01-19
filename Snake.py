import pygame
import random

pygame.init()
#dis = pygame.display.set_mode((800, 600))
#pygame.display.update()
#pygame.display.set_caption("Snake by Havel")

game_over = False
snakeRGB = (0, 255, 127)
appleRGB = (220, 20, 60)
clock = pygame.time.Clock()

class SnakeGame:
    black = (0, 0, 0)
    def __init__(self, windowX, windowY, X, Y):
        self.windowX = windowX
        self.windowY = windowY
        self.X = X
        self.Y = Y
        self.dis = pygame.display.set_mode((self.windowX, self.windowY))
        self.changeX = 0
        self.changeY = 0
        self.foodX = round((random.randrange(0, self.windowX))/10)*10
        self.foodY = round((random.randrange(0, self.windowY))/10)*10
        self.snakeLenght = 1
        self.snakeList = []

    def Window(self):
        pygame.display.update()
        pygame.display.set_caption("Snake by Havel")   

    def make_snake(self):
        self.dis.fill(SnakeGame.black)
        pygame.draw.rect(self.dis, appleRGB, [self.foodX, self.foodY, 10, 10])
        self.X += self.changeX
        self.Y += self.changeY
        pygame.draw.rect(self.dis, snakeRGB, [self.X, self.Y, 10, 10])
        snakeHead = []
        snakeHead.append(self.X)
        snakeHead.append(self.Y)
        self.snakeList.append(snakeHead)
        if len(self.snakeList) > self.snakeLenght:
            del self.snakeList[0]
        print (len(self.snakeList))
        for x in self.snakeList:
            pygame.draw.rect(self.dis, snakeRGB, [x[0], x[1], 10, 10])

    def move_snake_left(self):
        self.changeX = -10
        self.changeY = 0

    def move_snake_right(self):
        self.changeX = +10
        self.changeY = 0

    def move_snake_down(self):
        self.changeY = 10
        self.changeX = 0

    def move_snake_up(self):
        self.changeY = -10
        self.changeX = 0

    def boundaries(self):
        if self.X <= 0 or self.X >= self.windowX or self.Y <= 0 or self.Y >= self.windowY:
            return True
        snakeHead = []
        snakeHead.append(self.X)
        snakeHead.append(self.Y)
        for x in self.snakeList[:-1]:
            if x == snakeHead:
                return True

        else:
            return False

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def food(self):
        if self.foodX == self.X and self.foodY == self.Y:
                self.foodX = round((random.randrange(0, self.windowX-10))/10)*10
                self.foodY = round((random.randrange(0, self.windowY-10))/10)*10
                self.snakeLenght += 1

snake = SnakeGame(300, 200, 150, 100)
snake.Window()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_snake_left()
            if event.key == pygame.K_RIGHT:
                snake.move_snake_right()
            if event.key == pygame.K_UP:
                snake.move_snake_up()
            if event.key == pygame.K_DOWN:
                snake.move_snake_down()
    #game_over = snake.boundaries()
    snake.food()
    snake.make_snake()
    game_over = snake.boundaries()
    pygame.display.update()
    clock.tick (10)
    #print(snake.get_X())
pygame.quit()
quit()
