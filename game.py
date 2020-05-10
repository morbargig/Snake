import pygame
import random
# import time
import sys
# print(sys.executable)
# exit()
width, heigth = 500,480

class BasicSprite(object):
    def __init__(self,heigth,width,color,xy=False ,screen={'width' : width,"heigth" : heigth}):
        self.heigth = heigth
        self.width = width
        self.image = pygame.Surface((self.heigth,self.width))
        self.image.fill(color)
        if not xy:
            self.x= (screen['width'] - width) /2 
            self.y= (screen['heigth'] - heigth) /2
        else :
            self.x = xy[0]
            self.y = xy[1]

    def draw(self,window):
        window.blit(self.image, (self.x,self.y ))

pygame.init()
screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption('Bargig Snake')
clock = pygame.time.Clock()
player =  BasicSprite(10,10,(255,0,0))

print()
enemies= []
for i in range(0,random.randrange(200)):
    enemies.append(BasicSprite(10,10,(random.randrange(200),random.randrange(255),random.randrange(255)),(random.randrange(heigth),random.randrange(width) ) ))


#Main loop/ Game loop

run = True
loopNmber=0
joump=False
moves = []
while run:
    loopNmber+=1
    lastx=player.x
    lasty=player.y

    if loopNmber % 100 == 0:
        enemies.append(BasicSprite(10,10,(random.randrange(200),random.randrange(255),random.randrange(255)),(random.randrange(heigth),random.randrange(width) ) ))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    # Handling events
    keys = pygame.key.get_pressed()
    if joump :
        player.y += 10
        joump = False
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.y +  player.heigth < heigth:
        player.y += 5    
    if keys[pygame.K_RIGHT] and player.x +  player.width < width:
        player.x += 5
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5  
    if keys[pygame.K_SPACE] and player.y > 10:
        player.y -= 10
        joump=True 

    for i  in enemies:
        if player.x <= i.x + i.width and player.x + player.width >= i.x:
            if player.y <= i.y + i.heigth and player.y + player.heigth >= i.y:
                moves.append(i)
                del enemies[enemies.index(i)]
    # Creathing enemies
    for i in moves:
        if (lastx ,lasty) == (i.x ,i.y ) or (player.x ,player.y) == (lastx ,lasty) : break
        if (i.x ,i.y) == (player.x,player.y) :  print("end game") ; pygame.quit()  ; break
        newx,newy = i.x ,i.y 
        i.x ,i.y = lastx ,lasty
        lastx ,lasty = newx,newy
        
        



    # Redraw screen
    screen.fill((255,255,255))
    for i in enemies:
        i.draw(screen)
    for i in moves:
        i.draw(screen)   
    player.draw(screen)
    pygame.display.update()
    clock.tick(30)
    # time.sleep(1/27)
pygame.quit()