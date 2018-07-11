import pygame as pg 
from PGSettings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.imageleft = [pg.image.load('PNGImages/L1.png'), pg.image.load('PNGImages/L2.png'), pg.image.load('PNGImages/L3.png'), 
        pg.image.load('PNGImages/L4.png'), pg.image.load('PNGImages/L5.png'), pg.image.load('PNGImages/L6.png'), 
        pg.image.load('PNGImages/L7.png'), pg.image.load('PNGImages/L8.png'), pg.image.load('PNGImages/L9.png')]
        self.imageright = [pg.image.load('PNGImages/R1.png'), pg.image.load('PNGImages/R2.png'), pg.image.load('PNGImages/R3.png'), 
        pg.image.load('PNGImages/R4.png'), pg.image.load('PNGImages/R5.png'), pg.image.load('PNGImages/R6.png'), 
        pg.image.load('PNGImages/R7.png'), pg.image.load('PNGImages/R8.png'), pg.image.load('PNGImages/R9.png')]
        self.image = pg.image.load('PNGImages/Standing.png')
        self.groups = game.all_sprites
        self.game = game
        self.x = x
        self.y = y
        self.yvel = 0
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.vel = 10
        self.left = False
        self.right = False
        self.stepcount = 0
        self.jump = False
        self.airtime = 10
        self.facing = 1
        self.laserbeams = []

    def moveleft(self):
        self.x -= self.vel
        self.left = True
        self.right = False

    def moveright(self):
        self.x += self.vel
        self.right = True
        self.left = False

    def moveup(self, game):
        if self.airtime >= -10:
            neg = 1
            if self.airtime < 0:
                neg = -1
            if not checkcollision(self, game):
                self.y -= (self.airtime ** 2) * .4 * neg
                self.airtime -= 1
        else:
            self.jump = False
            self.airtime = 10
        # elif checkcollision(self, game):
        #     self.jump = False
        #     self.airtime = 10
        

        
    def shootlaser(self, game):
        if self.left:
            self.facing = -1
        else:
            self.facing = 1
        if len(self.laserbeams) < 15:
            if self.facing == -1:
                self.laserbeams.append(Laser(game, (self.x - 20), (self.y - 10), self.facing))
            elif self.facing == 1:
                self.laserbeams.append(Laser(game, (self.x), (self.y - 10), self.facing))

    def update(self, screen):
        self.screen = screen
        if self.stepcount + 1 >= 27:
            self.stepcount = 0
        if self.left:
            win.blit(self.screen, self.imageleft[self.stepcount//3], (self.x, self.y))
            self.stepcount += 1
        elif self.right:
            win.blit(self.screen, self.imageright[self.stepcount//3], (self.x, self.y))
            self.stepcount += 1
        else:
            if self.right:
                win.blit(self.screen, self.imageright[0], (self.x, self.y))
            else:
                win.blit(self.screen, self.imageleft[0], (self.x, self.y))

    
    # def wallcollision(self):
    #     for wall in self.game.walls:
    #         if self.x == wall.x and self.y == wall.y:
    #             return True
    #     return False

##Wall collision function

def checkcollision(self, game):
    for wall in game.walls:
        if (wall.y - 32) == (self.y + 32) and wall.x == self.x:
            return True
    return False

class Orc(Player):
    def __init__(self, game, x, y, width, height, vel, airtime):
        self.imageleft = [pg.image.load('PNGImages/L1E.png'), pg.image.load('PNGImages/L2E.png'), pg.image.load('PNGImages/L3E.png'), 
        pg.image.load('PNGImages/L4E.png'), pg.image.load('PNGImages/L5E.png'), pg.image.load('PNGImages/L6E.png'), 
        pg.image.load('PNGImages/L7E.png'), pg.image.load('PNGImages/L8E.png'), pg.image.load('PNGImages/L9E.png')]
        self.imageright = [pg.image.load('PNGImages/R1E.png'), pg.image.load('PNGImages/R2E.png'), pg.image.load('PNGImages/R3E.png'), 
        pg.image.load('PNGImages/R4E.png'), pg.image.load('PNGImages/R5E.png'), pg.image.load('PNGImages/R6E.png'), 
        pg.image.load('PNGImages/R7E.png'), pg.image.load('PNGImages/R8E.png'), pg.image.load('PNGImages/R9E.png')]
        self.image = pg.image.load('PNGImages/Standing.png')
        self.groups = game.all_sprites, game.orcs
        self.game = game
        self.x = x
        self.y = y
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.vel = vel
        self.left = False
        self.right = False
        self.stepcount = 0
        self.jump = False
        self.airtime = airtime
        self.facing = 1
        self.laserbeams = []

    def orclaser(self, game):
        if self.left:
            self.facing = -1
        else:
            self.facing = 1
        if len(self.laserbeams) < 10:
            if self.facing == -1:
                self.laserbeams.append(Orclaser(game, (self.x - 20), (self.y - 10), self.facing))
            elif self.facing == 1:
                self.laserbeams.append(Orclaser(game, (self.x), (self.y - 10), self.facing))

    
    def orcjumpautoleft(self, screen, game):
        self.moveleft()
        self.moveup(game)
        self.orclaser(screen)

    def orcjumpautoright(self, screen, game):
        self.moveright()
        self.moveup(game)
        self.orclaser(screen)

    def orcautoleft(self, screen):
        self.moveleft()
        self.orclaser(screen)

    def orcautoright(self, screen):
        self.moveright()
        self.orclaser(screen)
    


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((tilesize, tilesize))
        self.image.fill(red)
        self.game = game
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tilesize
        self.rect.y = y * tilesize

class Laser(pg.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        # self.groups = game.all_sprites, game.lasers
        # pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('PNGImages/laser1.png')
        self.x = x
        self.y = y
        # self.rect = self.image.get_rect()
        self.width = 20
        self.height = 20
        self.direction = direction
        self.vel = 3 * direction
        self.lasercount = 0

    def redraw(self, screen):
        self.screen = screen
        win.blit(self.screen, self.image, (self.x, self.y))

    def project(self, shooter):
        for beam in shooter.laserbeams:
            if  beam.x < 1280 and beam.x > 0:
                beam.x += beam.vel
            else:
                shooter.laserbeams.pop(shooter.laserbeams.index(beam))

class Orclaser(Laser):
    def __init__(self, game, x, y, direction):
        # self.groups = game.all_sprites, game.lasers
        # pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load('PNGImages/laser2.png')
        self.x = x
        self.y = y
        # self.rect = self.image.get_rect()
        self.width = 20
        self.height = 20
        self.direction = direction
        self.vel = direction
        self.lasercount = 0