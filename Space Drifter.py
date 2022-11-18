#New pygame program

#import and initialize package(s)
import pygame
import random

pygame.init()

#Constants
screenwidth =1000
screenheight = 500
fps = 60
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
totalpixels = screenwidth*screenheight
numstars = (screenwidth+screenheight)/2
starodds = int(totalpixels/numstars)
backgroundscrollx = 0
speed = (0,0)

#Start clock
fpsclock = pygame.time.Clock()

#Initialize screen
screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption('Space Shooter Game')

#Player properties
class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

#Asteroid properties
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,color,radius,location):
        super().__init__()
    def spawnasteroid(self):
        pygame.draw.circle(screen,self.color,self.location,self.radius)
#Unimplemented (so far!)


#Star properties
star  = pygame.Surface([2,2])
star.fill(white)

#Active sprites list
active_sprites_list = pygame.sprite.Group()

#Initialize player class
player = Player(red,30,20)
player.rect.x = int(screenwidth/2)
player.rect.y = int(screenheight/2)

active_sprites_list.add(player)

#Position variable
position = (player.rect.x,player.rect.y)

#Make background
background = pygame.Surface([screenwidth,screenheight])
background.fill(black)
backgroundstrip = pygame.Surface([1,screenheight])
backgroundstrip.fill(black)

#Generate stars
star  = pygame.Surface([2,2])
star.fill(white)

for x in range(screenwidth):
    for y in range(screenheight):        
        if random.randint(0,starodds) == 0:
            background.blit(star,(x,y))
            

#Run until user quits
running = True

while running:
    #Player controls
    for event in pygame.event.get():
        #Shut down if user clicks x
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed = (speed[0], speed[1]-5)
            elif event.key == pygame.K_a:
                speed = (speed[0]-5, speed[1])
            elif event.key == pygame.K_s:
                speed = (speed[0], speed[1]+5)
            elif event.key == pygame.K_d:
                speed = (speed[0]+5, speed[1])
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed = (speed[0], speed[1]+5)
            elif event.key == pygame.K_a:
                speed = (speed[0]+5, speed[1])
            elif event.key == pygame.K_s:
                speed = (speed[0], speed[1]-5)
            elif event.key == pygame.K_d:
                speed = (speed[0]-5, speed[1])

            
    #Game logic
    #move player
    position = (position[0]+speed[0],position[1]+speed[1])
    if position[0]>screenwidth-player.width:
        position = (screenwidth-player.width, position[1])
    elif position[0]<0:
        position = (0, position[1])
    if position[1]>screenheight-player.height:
        position = (position[0], screenheight-player.height)
    elif position[1]<0:
        position = (position[0],0)

    player.rect.x = int(position[0])
    player.rect.y = int(position[1])
        
    active_sprites_list.update()

    #Draw background
    screen.blit(background, (0,0))
    
    background.blit(background,(-1, 0))
    background.blit(backgroundstrip,(screenwidth-1,0)) #add black strip
    for y in range(screenheight):
        if random.randint(0,starodds) == 0:
            background.blit(star,(screenwidth-2,y))
    
    #Draw sprites
    active_sprites_list.draw(screen)

    #Update display
    pygame.display.update()
    fpsclock.tick(fps)

pygame.quit()
