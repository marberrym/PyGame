import pygame as pg
import sys
from PGSettings import *
from PGSprites import *


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((screenwidth, screenheight))
        pg.display.set_caption("Atlanta Orcs")
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.background = pg.image.load('JPGImages/background.jpg').convert()
    
    def load_data(self):
        pass


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 600, 600, 64, 64)
        for x in range (4, 12):
            Wall(self, x, 17)
        for x in range (15, 25):
            Wall(self, x, 13)
        for x in range (28, 36):
            Wall(self, x, 17)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
        pg.quit()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, screenwidth, tilesize):
            pg.draw.line(self.screen, white, (x, 0), (x, screenheight))
        for y in range(0, screenheight, tilesize):
            pg.draw.line(self.screen, white, (0, y), (screenwidth, y))

    def draw(self):
        # self.lasers = Laser(g, self.player.x, self.player.y, self.player.facing)
        pg.Surface.blit(self.screen, self.background, (0,0))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.player.update(g.screen)
        for beam in self.player.laserbeams:
            beam.project(self.player)
            beam.redraw(g.screen)
        pg.display.flip()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        keys = pg.key.get_pressed()
        
        #All player movement
        if keys[pg.K_SPACE]:
            self.player.shootlaser(g.screen)
        if keys[pg.K_LEFT] and self.player.x > self.player.vel:
            self.player.moveleft()
        elif keys[pg.K_RIGHT] and self.player.x < (screenwidth - self.player.width - self.player.vel):
            self.player.moveright()
        else:
            self.player.stand = True
            self.player.stepcount = 0
        if not self.player.jump:
            if keys[pg.K_UP]:
                self.player.jump = True
        else:
            self.player.moveup()
  

    def music(self):
        self.loadmusic = pg.mixer.music.load('MP3Songs/DTO.mp3')
        self.playmusic = pg.mixer.music.play()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


    #Platforms
    # win.blit(Platform, (550, 400))
    # win.blit(Platform, (220, 420))
    # win.blit(Platform, (950, 420))
    
    #Laserbeams
    # for beam in laserbeams:
    #     beam.redraw(win)
    

# laserbeams = []

g = Game()
g.show_start_screen()
while True:
    g.music()
    g.draw_grid
    g.new()
    g.run()
    g.show_go_screen()
    
g.quit()
