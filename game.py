import pygame
import random
import time
# import sys
# print(sys.executable)
# exit()
width, heigth = 500, 480


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
screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Bargig Snake')
clock = pygame.time.Clock()
player = BasicSprite(10, 10, (255, 0, 0))
player2 = BasicSprite(10, 10, (255, 0, 0))

enemies = []
for i in range(0, random.randrange(300)):
    enemies.append(BasicSprite(10, 10, (random.randrange(200), random.randrange(
        255), random.randrange(255)), (random.randrange(heigth), random.randrange(width))))


# Main loop/ Game loop

eatSound = pygame.mixer.Sound('eatSound.wav')
# pygame.mixer.music.sound.load('eatSound.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
run = True
loopNmber = 0
joump = False
moves = []
moves2 = []
showText = False
losee = False
while run:
    loopNmber += 1
    lastx = player.x
    lasty = player.y
    lastx2 = player2.x
    lasty2 = player2.y
    if not losee:
        if loopNmber % 5 == 0:
            loopNmber = 0
            enemies.append(BasicSprite(10, 10, (random.randrange(200), random.randrange(
                255), random.randrange(255)), (random.randrange(heigth), random.randrange(width))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Handling events
        keys = pygame.key.get_pressed()
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
        # if keys[pygame.K_SPACE] and player.y > 10:
        #     player.y -= 10
        #     joump=True

        for i in enemies:
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
                text = font.render('player 1 win !', True, (0, 255, 0), (0, 0, 255))
                textRect = text.get_rect()
                textRect.center = (width // 2, heigth // 2)
                losee = True
                showText = True
                break
            if (abs( i.x -player2.x) < player2.width ) and ( abs(i.y -player2.y)  < player2.heigth):
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('player 2 win !', True, (0, 255, 0), (0, 0, 255))
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
            if (i.x, i.y) == (player2.x, player2.y):
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('Game Over', True, (0, 255, 0), (0, 0, 255))
                textRect = text.get_rect()
                textRect.center = (width // 2, heigth // 2)
                losee = True
                showText = True
                break
            if (abs(i.x -player.x) <player.width ) and (abs(i.y -player.y) <player.heigth):
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('player 1 win !', True, (0, 255, 0), (0, 0, 255))
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
