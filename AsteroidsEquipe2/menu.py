import config
import ufo
import hud
import asteroid

class Menu:
    start_game = False
    header = config.Text("1 COIN 1 PLAY", 32)
    footer = config.Text("2 0 2 1  STEM GAMES", 16)
    header.pos = ((config.window.size[0] - header.font.size(header.message)[0])/2, 580)
    footer.pos = ((config.window.size[0] - footer.font.size(footer.message)[0])/2, 695)
    ufo = ufo.BigUFO((1.5, 0))
    hud = hud.HUD()
    asteroids = []
    for _ in range(4):
        asteroids.append(asteroid.BigAsteroid())

    def __init__(self, bg_color: tuple = config.COLOR_BLACK):
        self.bg_color = bg_color

    # def check_game_enter(self):
        # if key_pressed:
        #   self.start_game = True

    def display_bg_animation(self):
        self.header.display()
        self.footer.display()
        self.hud.menu_display()
        self.ufo.display()
        for ast in self.asteroids:
            ast.display()
            ast.move()
        self.ufo.move()
