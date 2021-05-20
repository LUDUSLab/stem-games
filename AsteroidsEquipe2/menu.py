import pygame

import config
import ufo
import hud
import asteroid
from random import randrange

class Menu:
    start_game = False
    header = config.Text("1 COIN 1 PLAY", 32)
    footer = config.Text("2 0 2 1  STEM GAMES", 16)
    start_txt = config.Text("PUSH START", 32, blink=True)
    header.pos = ((config.window.size[0] - header.font.size(header.message)[0])/2, 580)
    footer.pos = ((config.window.size[0] - footer.font.size(footer.message)[0])/2, 695)
    ufo = None
    hud = hud.HUD(None)
    asteroids = [asteroid.Asteroid(pygame.Vector2(randrange(config.window.size[0]), randrange(
            config.window.size[1])), None) for _ in range(4)]

    def check_game_enter(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.start_game = True

    def display(self):
        self.header.display()
        self.footer.display()
        self.start_txt.display()
        self.hud.menu_display()
        if self.ufo is not None:
            self.ufo.display()
            self.ufo.move()
            if self.ufo.position.x > 1300 or self.ufo.position.x < -20:
                self.ufo = None
        else:
            randy = randrange(0, 721)
            randx = randrange(0, 1281)
            size = 1 if randx < 20 else 2
            if randx == 0 or randx == 1280:
                self.ufo = ufo.UFO(pygame.Vector2(randx, randy), size)
                print("UFO APPEARED!")
        for ast in self.asteroids:
            ast.display()
            ast.move()

