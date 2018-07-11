import pygame
import sys

FPS = 60
#Screen Dimensions
screenwidth = 1280
screenheight = 704


#Tile Size
tilesize = 32

#Colors
white = (255, 255, 255)
red = (255, 0, 0)

#Grid Dimensions
gridwidth = screenwidth / tilesize
# Grid Width is 40 tiles
gridheight = screenheight / tilesize
# Grid Height is 22 tiles
win = pygame.Surface
pg = pygame

#PNG IMAGES
platform = pg.image.load('PNGImages/platform2.png')
# beam = pg.image.load('PNGImages/laser1.png')
