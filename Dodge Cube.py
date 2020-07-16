import pygame
import time
import random

pygame.init()

cubelist = []
score = 0
zinger = 0


display_width = 800
display_height = 600

spawnwidth = 80
spawnheight = 80
difficulty = 3

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge Cube')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

playerImg = pygame.image.load('Assets/playercube.png')
menuImg = pygame.image.load('Assets/MenuImage.png')
cube_height = 60
cube_width = 60

font = pygame.font.Font('Assets/unispace.ttf', 26)


def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def draw_menu():
    gameDisplay.blit(menuImg, (0,0))

def generate_cubes():
    i = 1
    cubeproperties = []
    
    while i <= difficulty:
        cubeproperties.append(random.randint(0, display_width - spawnwidth))
        cubeproperties.append(random.randint(0, display_height - spawnheight))
        cubeproperties.append(random.choice([-2,2]))
        cubeproperties.append(random.choice([-2,2]))
        cubeproperties.append(0)
        cubelist.append(cubeproperties)
        cubeproperties = []
        print(cubelist)
        i += 1

def add_cube():
    cubeproperties = []
    cubeproperties.append(random.randint(0, display_width - spawnwidth))
    cubeproperties.append(random.randint(0, display_height - spawnheight))
    cubeproperties.append(random.choice([-2,2]))
    cubeproperties.append(random.choice([-2,2]))
    cubeproperties.append(0)
    cubelist.append(cubeproperties)
    cubeproperties = []

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
            ceilingbounce(i)

        if (cube_x >= display_width - spawnwidth and x_move > 0):
            x_move = 0
            right_wallbounce(i)

        if (cube_x <= 0 and x_move < 0):
            x_move = 0
            left_wallbounce(i)

        for j in cubelist:
            if i != j:
                if (((i[1] - (j[1] + spawnheight) > 0 and i[1] - (j[1] + spawnheight) <=4))):
                    if (i[0] > j[0] and i[0] < (j[0] + spawnheight) or (i[0] + spawnheight > j[0] and i[0] + spawnheight < j[0] + spawnheight)):
                        print(j[4])
                        print(i[4])
                        if j[4] == 0:
                            floorbounce(j)
                            j[4] == 5
                        if i[4] == 0:    
                            ceilingbounce(i)
                            i[4] = 5

                if ((i[1] + spawnheight) - j[1] > 0 and i[1] + spawnheight -j[1] <=4):
                    if (i[0] > j[0] and i[0] < (j[0] + spawnheight) or (i[0] + spawnheight > j[0] and i[0] + spawnheight < j[0] + spawnheight)):
                        print(j[4])
                        print(i[4])
                        if j[4] == 0:
                            ceilingbounce(j)
                            j[4] == 5
                        if i[4] == 0:    
                            floorbounce(i)
                            i[4] = 5
                        
                if (i[0] - (j[0] + spawnwidth) > 0 and i[0] - (j[0] + spawnwidth) <=4): 
                    if (i[1] > j[1] and i[1] < (j[1] + spawnheight)) or (i[1] + spawnheight > j[1] and i[1] + spawnheight < j[1] + spawnheight):    
                        print(j[4])
                        print(i[4])
                        if j[4] == 0:
                            right_wallbounce(j)
                            j[4] == 5
                        if i[4] == 0:
                            left_wallbounce(i)
                            i[4] == 5

                if ((i[0] + spawnwidth - j[0] > 0) and (i[0] + spawnwidth - j[0] <=4)): 
                    if (i[1] > j[1] and i[1] < (j[1] + spawnheight)) or (i[1] + spawnheight > j[1] and i[1] + spawnheight < j[1] + spawnheight):    
                        print(j[4])
                        print(i[4])
                        if j[4] == 0:
                            left_wallbounce(j)
                            j[4] == 5
                        if i[4] == 0:
                            right_wallbounce(i)
                            i[4] == 5

        i[0] = i[0] + x_move
        i[1] = i[1] + y_move

def collision_check(x,y):
    for i in cubelist:
        if(x + cube_width - i[0] < 0)  and (x + cube_width - i[0] >= -8):
            if ((y + cube_height > i[1]) and (y + cube_height < i[1] + spawnheight)) or ((y > i[1]) and (y < i[1] + spawnheight)):
                print("left hit!")

        if(x - (i[0] + spawnwidth) < 0)  and (x - (i[0] + spawnwidth) >= -8):
            if ((y + cube_height > i[1]) and (y + cube_height < i[1] + spawnheight)) or ((y > i[1]) and (y < i[1] + spawnheight)):
                print("right hit!")

        if(y + cube_height - i[1] < 0)  and (y + cube_height - i[1] >= -8):
            if ((x + cube_width > i[0]) and (x + cube_width < i[0] + spawnwidth)) or ((x > i[0]) and (x < i[0] + spawnwidth)):
                print("top hit!")

        if(y - (i[1] + spawnheight) < 0)  and (y - (i[1] + spawnheight) >= -8):
            if ((x + cube_width > i[0]) and (x + cube_width < i[0] + spawnwidth)) or ((x > i[0]) and (x < i[0] + spawnwidth)):
                print ("bottom hit!")

        




def lower_cooldowns():
    for i in cubelist:
        if i[4] > 0:
            i[4] = i[4] - 1

def left_wallbounce(bounce_cube):
    bounce_cube[2] = -(bounce_cube[2])
    bounce_cube[0] += 2
    return bounce_cube

def right_wallbounce(bounce_cube):
    bounce_cube[2] = -(bounce_cube[2])
    bounce_cube[0] -= 2
    return bounce_cube    

def floorbounce(bounce_cube):
    bounce_cube[3] = -(bounce_cube[3])
    bounce_cube[1] -= 2
    return bounce_cube

def ceilingbounce(bounce_cube):
    bounce_cube[3] = -(bounce_cube[3])
    bounce_cube[1] += 2
    return bounce_cube

def menu():

    gameExit = False
    
    text = font.render('High Score: ' + str(zinger), True, black, white)
    textRect = text.get_rect()
    textRect.center = (600, 550)

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = true

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        
        gameDisplay.fill(white)
        draw_menu()
        gameDisplay.blit(text, textRect)
        
        
        pygame.display.update()
        clock.tick(60)
    
    
def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    score = 0
    ticks = 0
    generate_cubes()

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_ESCAPE:
                    del cubelist[:]
                    gameExit = True
                    

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
        
        if ticks % 1800 == 0 and ticks != 0:
            add_cube()
        
        if ticks % 60 == 0 and ticks != 0:
            score += 1
            print(score)
        
        collision_check(x,y)
        
        
        y += y_change
        x += x_change

        move_cubes()
        lower_cooldowns()
        gameDisplay.fill(white)
        player(x,y)
        draw_cubes()
        ticks += 1
                
        pygame.display.update()
        clock.tick(60)
menu()
pygame.quit()
quit()
