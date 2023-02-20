import pygame, random

pygame.init() 

displayWidth = 800
displayHeight = 600

gameWindow = pygame.display.set_mode((displayWidth, displayHeight))
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)

running = True

snakeImg = pygame.image.load('assets/Green_Snake_Pixel.png')

clock = pygame.time.Clock()

foodX = random.randint(0, displayWidth)
foodY = random.randint(0, displayHeight)

snakeX = 0
snakeY = 0

snakeX_move = 0 
snakeY_move = 0

def snake(x, y):
    # gameWindow.blit(snakeImg, (x, y))
    pygame.draw.rect(gameWindow, blue, [x, y, 20, 20])


def handleRightMove():
    global snakeX_move
    global snakeY_move
    snakeX_move = 10
    snakeY_move = 0

def handleLeftMove():
    global snakeX_move
    global snakeY_move
    snakeX_move = -10
    snakeY_move = 0

def handleDownMove():
    global snakeX_move
    global snakeY_move
    snakeX_move = 0
    snakeY_move = 10

def handleUpMove():
    global snakeX_move
    global snakeY_move
    snakeX_move = 0
    snakeY_move = -10

def handleStopMove(): 
    global snakeX_move
    global snakeY_move
    snakeX_move = 0
    snakeY_move = 0

def boundaries():
    global displayHeight
    global displayWidth
    global snakeX 
    global snakeY
    
    if snakeX > displayWidth: 
        snakeX = 0
    elif snakeX < 0: 
        snakeX = displayWidth
    
    if snakeY > displayHeight:
        snakeY = 0
    elif snakeY < 0: 
        snakeY = displayHeight

def snakeCollision(): 
    global snakeX
    global snakeY
    global foodX
    global foodY 
    # VALOR DE 20 COMO ALTURA DO BLOCO 
    if snakeX + 20 > foodX  and snakeX < foodX + 20 and snakeY + 20 > foodY and snakeY < foodY + 20:
        randomFoodCords()

def randomFoodCords():
    global foodX 
    global foodY 
    foodX = random.randint(0, displayWidth)
    foodY = random.randint(0, displayHeight)

def foodSpawn():
   global foodX 
   global foodY
   pygame.draw.rect(gameWindow, red, [foodX, foodY, 20, 20])

def gameLoop():
    global running
    global snakeX
    global snakeY

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        handleUpMove()
                    case pygame.K_DOWN:
                        handleDownMove()
                    case pygame.K_RIGHT:
                        handleRightMove()
                    case pygame.K_LEFT:
                        handleLeftMove()
                    case pygame.K_SPACE:
                        handleStopMove()
    

        snakeX += snakeX_move
        snakeY += snakeY_move

        boundaries()
        snakeCollision()

        gameWindow.fill(white)
        foodSpawn()
        snake(snakeX, snakeY)
        

        pygame.display.update()
        clock.tick(10)


gameLoop()
pygame.quit()
quit()
