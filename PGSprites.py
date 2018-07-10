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
        self.facing = 1

    def update(self, screen):
        self.screen = screen
        if self.stepcount + 1 >= 27:
            self.stepcount = 0
        if not self.stand:
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

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((tilesize, tilesize))
        self.image.fill(red)
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
        self.vel = 20 * direction
        self.lasercount = 0

    def redraw(self, screen):
        self.screen = screen
        win.blit(self.screen, self.image, (self.x, self.y))