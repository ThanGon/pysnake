import pygame, random
from pygame.math import Vector2

pygame.init() 

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bgGreen = (95, 167, 0)

snakeImg = pygame.image.load('assets/Green_Snake_Pixel.png')

clock = pygame.time.Clock()

cell_size = 20
cell_number = 30

gameWindow = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

class SNAKE: 
    def __init__(self):
        self.body = [Vector2(2, 0), Vector2(1,0), Vector2(0,0)]
        self.direction =  Vector2(1,0)

    def drawSnake(self):
        for block in self.body: 
            blockRect = pygame.Rect(block.x * cell_size, block.y * cell_size , cell_size, cell_size)
            pygame.draw.rect(gameWindow, green, blockRect)

    def moveSnake(self):
        body = self.body[:-1]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]

    def addBlock(self): 
        body = self.body[:]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]


class FRUIT: 
    def __init__(self):
        self.randomPosition()
    
    def drawFruit(self):
        fruitRect = pygame.Rect(self.pos.x * cell_size , self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(gameWindow, red, fruitRect)

    def randomPosition(self): 
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self): 
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self): 
        self.snake.moveSnake()
        self.checkCollision()

    def draw(self): 
        self.snake.drawSnake()
        self.fruit.drawFruit()

    def checkCollision(self):
        self.checkBoundaries()
        if self.fruit.pos == self.snake.body[0]: 
            self.fruit.randomPosition()
            self.snake.addBlock()

    def checkBoundaries(self): 
        if not 0 <= self.snake.body[0].x:
            self.snake.body[0].x = cell_number -1
        elif not cell_number >= self.snake.body[0].x :
            self.snake.body[0].x = 0 

        if not 0 <= self.snake.body[0].y:
            self.snake.body[0].y = cell_number -1
        elif not cell_number >= self.snake.body[0].y :
            self.snake.body[0].y = 0 

        for block in self.snake.body[1:]: 
            if block == self.snake.body[0]:
                self.gameOver()
    
    def gameOver(self):
        self.snake = SNAKE() 
        self.fruit = FRUIT()


def gameLoop():
    main = MAIN()

    running = True

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 175)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            if event.type == SCREEN_UPDATE: 
                main.update()
            if event.type == pygame.KEYDOWN: 
                match event.key: 
                    case pygame.K_UP: 
                        main.snake.direction = Vector2(0, -1)
                    case pygame.K_DOWN:
                        main.snake.direction = Vector2(0, 1)
                    case pygame.K_LEFT:
                        main.snake.direction = Vector2(-1, 0)
                    case pygame.K_RIGHT:
                        main.snake.direction = Vector2(1, 0)
        
        gameWindow.fill(bgGreen)

        main.draw()
        pygame.display.update()
        clock.tick(60)


gameLoop()
pygame.quit()
quit()
