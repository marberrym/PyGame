import pygame
pygame.init()
pygame.mixer.init()

#Music - Destroy the Orcs
pygame.mixer.music.load('MP3Songs/DTO.mp3')
pygame.mixer.music.queue('MP3Songs/DTO.mp3')
pygame.mixer.music.play()


screenwidth = 1280
screenheight = 704

win = pygame.display.set_mode((screenwidth, screenheight))

Background = pygame.image.load('JPGImages/background.jpg')
Platform = pygame.image.load('PNGImages/platform2.png')
Beam = pygame.image.load('PNGImages/laser1.png')

moveRight = [pygame.image.load('PNGImages/R1.png'), pygame.image.load('PNGImages/R2.png'), pygame.image.load('PNGImages/R3.png'), pygame.image.load('PNGImages/R4.png'), pygame.image.load('PNGImages/R5.png'), pygame.image.load('PNGImages/R6.png'), pygame.image.load('PNGImages/R7.png'), pygame.image.load('PNGImages/R8.png'), pygame.image.load('PNGImages/R9.png')]
moveLeft = [pygame.image.load('PNGImages/L1.png'), pygame.image.load('PNGImages/L2.png'), pygame.image.load('PNGImages/L3.png'), pygame.image.load('PNGImages/L4.png'), pygame.image.load('PNGImages/L5.png'), pygame.image.load('PNGImages/L6.png'), pygame.image.load('PNGImages/L7.png'), pygame.image.load('PNGImages/L8.png'), pygame.image.load('PNGImages/L9.png')]
char = pygame.image.load('PNGImages/standing.png')

pygame.display.set_caption("Matt Saves Atlanta From the Orcs!")

Clock = pygame.time.Clock()

# Super class to be integrated
# class Mob(object):
#     def __init__(self, x, y, width, height, vel, health):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.vel = vel
#         self.left = False
#         self.right = False
#         self.stepcount = 0
#         self.jump = False
#         self.airtime = 10
#         self.stand = True
#         self.falling = True

#Player Character Class Set
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.stepcount = 0
        self.jump = False
        self.airtime = 10
        self.stand = True
        self.falling = True

    # def Collision(self):
    #     if 220 < self.x < 350 and self.y > 520:

    
    def redraw(self, win):
        if self.stepcount + 1 >= 27:
            self.stepcount = 0
        if not self.stand:
            if self.left:
                win.blit(moveLeft[self.stepcount//3], (self.x, self.y))
                self.stepcount += 1
            elif self.right:
                win.blit(moveRight[self.stepcount//3], (self.x, self.y))
                self.stepcount += 1
        else:
            if self.right:
                win.blit(moveRight[0], (self.x, self.y))
            else:
                win.blit(moveLeft[0], (self.x, self.y))

#Laser Beam Class
class Laser(object):
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.vel = 20 * direction
        self.lasercount = 0

    def redraw(self, win):
        win.blit(Beam, (self.x, self.y))
            

#Game Screen Refresh Function
def ScreenRefresh ():
    #Background
    win.blit(Background, (0, 0))
    
    #Platforms
    win.blit(Platform, (550, 400))
    win.blit(Platform, (220, 420))
    win.blit(Platform, (950, 420))
    
    #Laserbeams
    for beam in laserbeams:
        beam.redraw(win)
    #Player
    main.redraw(win)
    pygame.display.update()


#Global Variables
run = True
main = Player(600, 600, 64, 64)
laserbeams = []

#Main Game Run Loop
while run:
    Clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for beam in laserbeams:
        if  beam.x < 1278 and beam.x > 0:
            beam.x += beam.vel
        else:
            laserbeams.pop(laserbeams.index(beam))
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if main.left:
            facing = -1
        else:
            facing = 1
        if len(laserbeams) < 5:
            if facing == -1:
                laserbeams.append(Laser((main.x - 60), (main.y - 10), 20, 20, facing))
            elif facing == 1:
                laserbeams.append(Laser((main.x + 20), (main.y - 10), 20, 20, facing))
        

    if keys[pygame.K_LEFT] and main.x > main.vel:
        main.x -= main.vel
        main.left = True
        main.right = False
        main.stand = False
    elif keys[pygame.K_RIGHT] and main.x < (screenwidth - main.width - main.vel):
        main.x += main.vel
        main.right = True
        main.left = False
        main.stand = False
    else:
        main.stand = True
        main.stepcount = 0
    if not main.jump:
        if keys[pygame.K_UP]:
            main.jump = True
    else:
        if main.airtime >= -10:
            neg = 1
            if main.airtime < 0:
                neg = -1
            main.y -= (main.airtime ** 2) * .4 * neg
            main.airtime -= 1
        else:
            main.jump = False
            main.airtime = 10
    
    
    ScreenRefresh()
    pygame.display.flip()

    

pygame.quit()