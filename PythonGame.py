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
        self.platform = pg.image.load('PNGImages/platform2.png').convert()
    
    def load_data(self):
        pass


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.orcs = pg.sprite.Group()
        self.player = Player(self, 600, 600, 64, 64)
        self.orc = Orc(self, 800, 600, 64, 64, 4, 9)
        self.orc2 = Orc(self, 200, 600, 64, 64, 7, 9)
        self.orclist = [self.orc, self.orc2]
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
        pg.Surface.blit(self.screen, self.background, (0,0))
        self.all_sprites.draw(self.screen)
        self.player.update(g.screen)
        self.orc.update(g.screen)
        self.orc2.update(g.screen)
        for beam in self.player.laserbeams:
            beam.project(self.player)
            beam.redraw(g.screen)
        for beam in self.orc.laserbeams:
            beam.project(self.orc)
            beam.redraw(g.screen)
        for beam in self.orc2.laserbeams:
            beam.project(self.orc2)
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
            self.orc.orclaser(g.screen)
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
            self.player.moveup(g)

        #All orc movement
        for orc in self.orclist:
            if self.player.x < orc.x and self.player.y < orc.y:
                orc.orcjumpautoleft(g.screen, g)
            elif self.player.x > orc.x and self.player.y < orc.y:
                orc.orcjumpautoright(g.screen, g)
            elif self.player.x < orc.x:
                orc.orcautoleft(g.screen)  
            elif self.player.x > orc.x:
                orc.orcautoright(g.screen)
            

    def music(self):
        self.loadmusic = pg.mixer.music.load('MP3Songs/DTO.mp3')
        self.playmusic = pg.mixer.music.play()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while True:
    g.music()
    g.new()
    g.run()
    g.show_go_screen()
    
g.quit()
