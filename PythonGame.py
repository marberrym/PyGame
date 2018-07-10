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
        for beam in laserbeams:
            beam.redraw(g.screen)
        pg.display.flip()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # self.playing = False
                pg.quit()

        for beam in laserbeams:
            if  beam.x < 1278 and beam.x > 0:
                beam.x += beam.vel
            else:
                laserbeams.pop(laserbeams.index(beam))
            
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            if g.player.left:
                facing = -1
            else:
                facing = 1
            if len(laserbeams) < 15:
                if facing == -1:
                    laserbeams.append(Laser(g, (g.player.x - 60), (g.player.y - 10), facing))
                elif facing == 1:
                    laserbeams.append(Laser(g, (g.player.x + 20), (g.player.y - 10), facing))
            

        if keys[pg.K_LEFT] and g.player.x > g.player.vel:
            g.player.x -= g.player.vel
            g.player.left = True
            g.player.right = False
            g.player.stand = False
        elif keys[pg.K_RIGHT] and g.player.x < (screenwidth - g.player.width - g.player.vel):
            g.player.x += g.player.vel
            g.player.right = True
            g.player.left = False
            g.player.stand = False
        else:
            g.player.stand = True
            g.player.stepcount = 0
        if not g.player.jump:
            if keys[pg.K_UP]:
                g.player.jump = True
        else:
            if g.player.airtime >= -10:
                neg = 1
                if g.player.airtime < 0:
                    neg = -1
                g.player.y -= (g.player.airtime ** 2) * .4 * neg
                g.player.airtime -= 1
            else:
                g.player.jump = False
                g.player.airtime = 10   

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
