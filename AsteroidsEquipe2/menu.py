import pygame

import config
import ufo
import hud
import asteroid

class Menu:
    start_game = False
    header = config.Text("1 COIN 1 PLAY", 32)
    footer = config.Text("2 0 2 1  STEM GAMES", 16)
    start_txt = config.Text("PUSH START", 32, blink=True)
    header.pos = ((config.window.size[0] - header.font.size(header.message)[0])/2, 580)
    footer.pos = ((config.window.size[0] - footer.font.size(footer.message)[0])/2, 695)

    ufo = ufo.BigUFO((1.5, 0))
    hud = hud.HUD()
    asteroids = []
    for _ in range(4):
        asteroids.append(asteroid.BigAsteroid())

    def check_game_enter(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.start_game = True

    def display(self):
        self.header.display()
        self.footer.display()
        self.start_txt.display()
        self.hud.menu_display()
        self.ufo.display()
        for ast in self.asteroids:
            ast.display()
            ast.move()
        self.ufo.move()
