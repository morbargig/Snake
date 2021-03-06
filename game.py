import pygame
import random
import time
# import sys
# print(sys.executable)
# exit()

width, heigth = 800, 768

class BasicSprite(object):
    def __init__(self, heigth, width, color, xy=False, screen={'width': width, "heigth": heigth}):
        self.heigth = heigth
        self.width = width
        self.image = pygame.Surface((self.heigth, self.width))
        self.image.fill(color)
        if not xy:
            self.x = (screen['width'] - width) / 2
            self.y = (screen['heigth'] - heigth) / 2
        else:
            self.x = xy[0]
            self.y = xy[1]

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

pygame.init()
pygame.mixer.init()
eatSound = pygame.mixer.Sound('eatSound.wav')
# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)
run = True
loopNmber = 0
joump = False
moves = []
moves2 = []
computer= True
showText = False
losee = False
actTry=5
pygame.display.set_caption('Bargig Snake')
screen = pygame.display.set_mode((width, heigth))
player = BasicSprite(10, 10, (255, 0, 0),[int(random.randrange(int(width/2),width)),heigth])
player2 = BasicSprite(10, 10, (255, 0, 0),[int(random.randrange(1,int(width/2))),heigth])
clock = pygame.time.Clock()
enemies = []
# Main loop/ Game loop
def menu():
    while(True):
        screen.fill((255, 255, 255))
        textHeigth = heigth // 2
        for i in ["start game","end game","1 player","play agin computer","play agin frined"]:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(i, True, (0,0,255), (255, 0, 0))
            textRect = text.get_rect()
            textRect.center = (width // 2, textHeigth)
            screen.blit(text, textRect)
            textHeigth+=40
        print(pygame.mouse.get_pressed,pygame.mouse.get_pos)
        pygame.display.update()
        clock.tick(30)
menu()
def startGame ():
    global enemies,run,loopNmber,joump,moves,moves2,showText,losee,actTry
    enemies = []
    for i in range(0, random.randrange(300)):
        enemies.append(BasicSprite(10, 10, (random.randrange(200), random.randrange(
            255), random.randrange(255)), (random.randrange(heigth), random.randrange(width))))
    run = True
    actTry = 0
    loopNmber = 0
    joump = False
    moves = []
    moves2 = []
    showText = False
    losee = False
# startGame()
while run:
    loopNmber += 1
    lastx = player.x
    lasty = player.y
    lastx2 = player2.x
    lasty2 = player2.y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if losee :
        # run = True
        losee =False
        # startGame()
        menu()
        break
    if not losee:
        if loopNmber % 5 == 0:
            loopNmber = 0
            enemies.append(BasicSprite(10, 10, (random.randrange(200), random.randrange(
                255), random.randrange(255)), (random.randrange(heigth), random.randrange(width))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Handling events
        # if joump :
        #     player.y += 10
        #     joump = False
        if keys[pygame.K_UP]:
            if player.y > 0:
                player.y -= 5
            else:
                player.y = heigth - 5
        if keys[pygame.K_DOWN]:
            if player.y + player.heigth < heigth:
                player.y += 5
            else:
                player.y = 5
        if keys[pygame.K_RIGHT]:
            if player.x + player.width < width:
                player.x += 5
            else:
                player.x = 5
        if keys[pygame.K_LEFT]:
            if player.x > 0:
                player.x -= 5
            else:
                player.x = width - 5
        # jump
        # if keys[pygame.K_SPACE] and player.y > 10:
        #     player.y -= 10
        #     joump=True
        if not computer:
            # player 2
            if keys[pygame.K_w]:
                if player2.y > 0:
                    player2.y -= 5
                else:
                    player2.y = heigth - 5
            if keys[pygame.K_s]:
                if player2.y + player2.heigth < heigth:
                    player2.y += 5
                else:
                    player2.y = 5
            if keys[pygame.K_d]:
                if player2.x + player2.width < width:
                    player2.x += 5
                else:
                    player2.x = 5
            if keys[pygame.K_a]:
                if player2.x > 0:
                    player2.x -= 5
                else:
                    player2.x = width - 5
        else : 
            enemieIndex = None
            enemie = None
            optionalEnemies = enemies[:]
            
            # bedEnemies =[]
            # while(True):
            actlist = [0,0]
            
            def act():
                global actTry
                actTry+=1
                minDistance = ((heigth**2) + (width**2) )**0.5
                global actlist, enemie
                actlist= [0,0]
                for i in optionalEnemies:
                    newDis =  int(( (abs(player2.x - i.x)**2) + (abs(player2.y - i.y)**2))**0.5)
                    if newDis < minDistance:
                        minDistance = newDis
                        enemie = i
                yDic = player2.y - enemie.y
                xDic = player2.x - enemie.x
                if abs(yDic) > abs(xDic):
                    if yDic > 0:
                        actlist[0] -= 5
                    else :  actlist[0] += 5
                elif xDic > 0 :
                    actlist[1]-=5
                else : actlist[1]+=5
                player2.y += actlist[0]
                player2.x +=actlist[1]
            def unAct ():
                if enemie in optionalEnemies:
                    optionalEnemies.remove(enemie)
                player2.y -= actlist[0]
                player2.x -=actlist[1]
            if computer:
                act()
        # print(enemieIndex)


        for i in enemies:
            # newDis = ((abs(player2.x - i.x) + abs(player2.y - i.y))**2)**0.5
            # if newDis < minDistance:
            #     minDistance = newDis 

            if player.x <= i.x + i.width and player.x + player.width >= i.x:
                if player.y <= i.y + i.heigth and player.y + player.heigth >= i.y:
                    eatSound.play()
                    moves.append(i)
                    del enemies[enemies.index(i)]
                    eatSound.play() 
            if player2.x <= i.x + i.width and player2.x + player2.width >= i.x:
                if player2.y <= i.y + i.heigth and player2.y + player2.heigth >= i.y:
                    eatSound.play()
                    moves2.append(i)
                    del enemies[enemies.index(i)]
                    eatSound.play()
        # Creathing enemies
        for i in moves:
            if (lastx, lasty) == (i.x, i.y) or (player.x, player.y) == (lastx, lasty):
                break
            if (i.x, i.y) == (player.x, player.y):
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('player 2 win !', True, (0, 255, 0), (0, 0, 255))
                textRect = text.get_rect()
                textRect.center = (width // 2, heigth // 2)
                losee = True
                showText = True
                break
            if computer :
                while(abs( i.x -player2.x) < player2.width ) and ( abs(i.y -player2.y)  < player2.heigth):
                    if actTry < 10:
                        unAct()
                        act()
                    elif (abs( i.x -player2.x) < player2.width ) and ( abs(i.y -player2.y)  < player2.heigth):
                        font = pygame.font.Font('freesansbold.ttf', 32)
                        text = font.render('player 1 win !', True, (0, 255, 0), (0, 0, 255))
                        textRect = text.get_rect()
                        textRect.center = (width // 2, heigth // 2)
                        losee = True
                        showText = True
                        break
            else:
                if (abs( i.x -player2.x) < player2.width ) and ( abs(i.y -player2.y)  < player2.heigth):
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render('player 1 win !', True, (0, 255, 0), (0, 0, 255))
                    textRect = text.get_rect()
                    textRect.center = (width // 2, heigth // 2)
                    losee = True
                    showText = True
                    break
            newx, newy = i.x, i.y
            i.x, i.y = lastx, lasty
            lastx, lasty = newx, newy

        for i in moves2:
            if (lastx2, lasty2) == (i.x, i.y) or (player2.x, player2.y) == (lastx2, lasty2):
                break
            if computer:
                while (i.x, i.y) == (player2.x, player2.y):
                    unAct()
                    act()
            else : 
                if (i.x, i.y) == (player2.x, player2.y):
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render('player 1 win !', True, (0, 255, 0), (0, 0, 255))
                    textRect = text.get_rect()
                    textRect.center = (width // 2, heigth // 2)
                    losee = True
                    showText = True
                    break
            if (abs(i.x -player.x) <player.width ) and (abs(i.y -player.y) <player.heigth):
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('player 2 win !', True, (0, 255, 0), (0, 0, 255))
                textRect = text.get_rect()
                textRect.center = (width // 2, heigth // 2)
                losee = True
                showText = True
                break
            newx, newy = i.x, i.y
            i.x, i.y = lastx2, lasty2
            lastx2, lasty2 = newx, newy

        # Redraw screen
        screen.fill((255, 255, 255))
        for i in enemies:
            i.draw(screen)
        for i in moves:
            i.draw(screen)
        for i in moves2:
            i.draw(screen)
        player.draw(screen)
        player2.draw(screen)
    clock.tick(30)
    if showText:
        print("game over")
        screen.blit(text, textRect)
    pygame.display.update()
pygame.quit()
