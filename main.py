import pygame 

pygame.init() 

gameWindow = pygame.display.set_mode((800, 600))
white = (255, 255, 255)

running = True

snakeImg = pygame.image.load('assets/Green_Snake_Pixel.png')

clock = pygame.time.Clock()

x = 0
y = 0

def snake(x, y):
    gameWindow.blit(snakeImg, (x, y))

def handleRightMove():
    global x 
    x = x + 15

def handleLeftMove():
    global x
    x = x - 15

def handleDownMove():
    global y
    y = y + 15

def handleUpMove():
    global y
    y = y - 15


while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         x = x + 15
        #     if event.key == pygame.K_DOWN:
        #         y = y + 15
            match event.key:
                case pygame.K_UP:
                    handleUpMove()
                case pygame.K_DOWN:
                    handleDownMove()
                case pygame.K_RIGHT:
                    handleRightMove()
                case pygame.K_LEFT:
                    handleLeftMove()


    
    gameWindow.fill(white)
    snake(x, y)
    clock.tick(60)

    pygame.display.update()


pygame.quit()
quit()
