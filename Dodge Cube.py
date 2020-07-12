import pygame
import time
import random

pygame.init()

cubelist = []


display_width = 800
display_height = 600

spawnwidth = 80
spawnheight = 80
difficulty = 5

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge Cube')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

playerImg = pygame.image.load('playercube.png')
cube_height = 60
cube_width = 60

def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def generate_cubes():
    i = 1
    cubeproperties = []
    while i <= difficulty:
        cubeproperties.append(random.randint(0, display_width - spawnwidth))
        cubeproperties.append(random.randint(0, display_height - spawnheight))
        cubeproperties.append(random.randint(-3,3))
        cubeproperties.append(random.randint(-3,3))
        cubelist.append(cubeproperties)
        cubeproperties = []
        print(cubelist)
        i += 1

def draw_cubes():
    for i in cubelist:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], spawnwidth, spawnheight])

def move_cubes():
    for i in cubelist:
        cube_x = i[0]
        cube_y = i[1]
        x_move = i[2]
        y_move = i[3]

        if (cube_y >= display_height - spawnheight and y_move > 0):
            y_move = 0
            floorbounce(i)

        if (cube_y <= 0 and y_move < 0):
            y_move = 0
            floorbounce(i)

        if (cube_x >= display_width - spawnwidth and x_move > 0):
            x_move = 0
            wallbounce(i)

        if (cube_x <= 0 and x_move < 0):
            x_move = 0
            wallbounce(i)

        i[0] = i[0] + x_move
        i[1] = i[1] + y_move

def wallbounce(bounce_cube):
    bounce_cube[2] = -(bounce_cube[2])
    return bounce_cube

def floorbounce(bounce_cube):
    bounce_cube[3] = -(bounce_cube[3])
    return bounce_cube


def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if (y > display_height - cube_height and y_change > 0):
            y_change = 0

        if (y == 0 and y_change < 0):
            y_change = 0

        if (x > display_width - cube_width and x_change > 0):
            x_change = 0

        if (x == 0 and x_change < 0):
            x_change = 0
        
        y += y_change
        x += x_change

        move_cubes()

        gameDisplay.fill(white)
        player(x,y)
        draw_cubes()
                
        
        pygame.display.update()
        clock.tick(60)
        
generate_cubes()
game_loop()
pygame.quit()
quit()