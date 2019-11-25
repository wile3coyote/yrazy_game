import pygame
import random
import time

pygame.init()

display_height = 800
display_width = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
rotate_count = 0 

gameDisplay=pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption("Yrazy")
clock = pygame.time.Clock()

circleImg = pygame.image.load("misc_img/player_final.png")
backgroundImg = pygame.image.load("misc_img/grainy background.jpg")
bombImg = pygame.image.load("misc_img/bomb_3.png")
boostImg = pygame.image.load("misc_img/boost.png")
scoreImg = pygame.image.load("misc_img/score.png")
yokoSprite = [pygame.image.load("yoko/Frame 1-1.png"),pygame.image.load("yoko/Frame 1-2.png"),pygame.image.load("yoko/Frame 1-3.png"),pygame.image.load("yoko/Frame 1-4.png"),pygame.image.load("yoko/Frame 1-5.png"),pygame.image.load("yoko/Frame 1-6.png"),pygame.image.load("yoko/Frame 1-7.png"),pygame.image.load("yoko/Frame 1-8.png"),pygame.image.load("yoko/Frame 1-9.png"),pygame.image.load("yoko/Frame 1-10.png"),pygame.image.load("yoko/Frame 1-11.png"),pygame.image.load("yoko/Frame 1-12.png")]
sample = pygame.image.load("yoko/Frame 1-1.png")
def circle(x,y):
    gameDisplay.blit(circleImg, (x,y))
    
def text_objects(text,font):
    textSurface = font.render(text, 1, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    text_x = gameDisplay.get_width() / 2 - TextRect.width / 2
    text_y = gameDisplay.get_height() / 2 - TextRect.height / 2
    gameDisplay.blit(TextSurf, (text_x, text_y))

    
    pygame.display.update()

def text_display(x,y,text):
    textDisplay = pygame.font.Font('freesansbold.ttf',115)
    textSurf, textRect = text_objects(text, textDisplay)
    gameDisplay.blit(textSurf,(x,y))
    
def submenu_display(x,y,text):
    textDisplay = pygame.font.SysFont('sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic',30)
    textSurf, textRect = text_objects(text, textDisplay)
    gameDisplay.blit(textSurf,(x,y))
    
def customized_text_display(x,y,text,color,size,font):
    textDisplay = pygame.font.SysFont(font,size)
    textSurf = textDisplay.render(text, 1, color)
    textRect = textSurf.get_rect()
    gameDisplay.blit(textSurf,(x,y))

def crash():
    message_display("Game over")
    
    
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])
    
def randthings():
    xcoord,ycoord = random.randint(0,750),random.randint(0,550)
    return xcoord,ycoord

def collision(thingx,thingy,img,topl,topr,botl,bot):
    rectsize = img.get_rect()
    if(((thingx <= topl[0] <= thingx+rectsize.width) and (thingy <= topl[1] <= thingy+rectsize.height)) or ((thingx <= topr[0] <= thingx+rectsize.width) and (thingy <= topr[1] <= thingy+rectsize.height)) or ((thingx <= botl[0] <= thingx+rectsize.width) and (thingy <= botl[1] <= thingy+rectsize.height)) or ((thingx <= topr[0] <= thingx+rectsize.width) and (thingy <= topr[1] <= thingy+rectsize.height))):
        return True
    else:
        return False

def render_yoko():
    global rotate_count
    
    if rotate_count + 1 >= 36:
        rotate_count = 0
    
    gameDisplay.blit(yokoSprite[rotate_count//3], (550,80))
    rotate_count += 1
    
def game_menu():
    
    
    
    gameExit = False
    while not gameExit:
        
        if pygame.event.get(pygame.QUIT):
            gameExit = True
            
        gameDisplay.fill(white)
        text_display(180,100,"YRAZY")
        submenu_display(100,300,"Press spacebar to start or q to quit")
        render_yoko()
        pygame.display.update()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            gameExit = True
            game_loop()
        if pressed[pygame.K_q]:
            gameExit = True
        
        clock.tick(30)

def game_loop():
    x = display_height * 0.45
    y = display_width * 0.80
    bthingx,bthingy = randthings()
    gthingx,gthingy = -100,-100
    rthingx,rthingy = -100,-100
    rectsize = 30
    move = 5
    speedcountertime=None
    score = 0
    scorefont = pygame.font.SysFont("monospace", 16)
    gameoverfont = pygame.font.Font(None, 36)
    
    #spawning green square at random
    pygame.time.set_timer(pygame.USEREVENT+1, 3000)
    
    #spawning red square at random
    pygame.time.set_timer(pygame.USEREVENT+2, 10550)

    exit_check = False
    gameExit = False
    while not gameExit:
       
        if pygame.event.get(pygame.QUIT):
            gameExit = True
            
        #Events for spawning objects at random locations        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT+1:
                gthingx,gthingy = randthings()
            if event.type == pygame.USEREVENT+2:
                rthingx,rthingy = randthings()
                
        
        #player dimensions        
        topl = (x,y)
        topr = (x+50,y)
        botl = (x,y+50)
        botr = (x+50,y+50)
        
        #Control settings
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= move
            if x<0 : x=0
        if pressed[pygame.K_RIGHT]:
            x += move
            if x>750 : x = display_height-50
        if pressed[pygame.K_UP]:
            y -= move
            if y<0 : y=0
        if pressed[pygame.K_DOWN]:
            y += move
            if y>550 : y=display_width-50
        
                
        #Collision detection for black square
        if (collision(bthingx,bthingy,scoreImg,topl,topr,botl,botr)==True):
                bthingx,bthingy = randthings()
                score = score+1
        
        #Collision detection for green square
        if (collision(gthingx,gthingy,boostImg,topl,topr,botl,botr)==True):
                speedcountertime = pygame.time.get_ticks()
                gthingx,gthingy = -100,-100
                move = move + 2
                if move >= 11 : move = move-2
                
        #Collision detection for red square
        if (collision(rthingx,rthingy,bombImg,topl,topr,botl,botr)==True):
                rthingx,rthingy = -100,-100
                exit_check = True
                
                
        #Reset speed
        if speedcountertime:        
            if(pygame.time.get_ticks()-speedcountertime > 6500):
                speedcountertime=None
                move = 5
                
        #Rendering score
        scoretext = scorefont.render("Score = "+str(score), 1, black)
       
        #Displays the game over screen
        if exit_check:
                text_display(100,100,"Game Over")
                submenu_display(100,300,"Press spacebar to play again or q to quit")
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    gameExit = True
                    game_loop()
                if pressed[pygame.K_q]:
                    gameExit = True
        else:
            #update screen
            gameDisplay.blit(backgroundImg, (0,0))
            gameDisplay.blit(scoreImg,(bthingx,bthingy))
            gameDisplay.blit(boostImg,(gthingx,gthingy))
            gameDisplay.blit(bombImg, (rthingx,rthingy))
            circle(x,y)
            #gameDisplay.blit(scoretext, ( 800,0))
            customized_text_display(650,0,("Score:"+str(score)),black,30,'arial')
        pygame.display.update()
        clock.tick(60)

game_menu()


pygame.quit()
quit()