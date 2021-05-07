import config
import ufo
import hud

class Menu:
    start_game = False
    header = config.Text("1 COIN 1 PLAY", 30)
    footer = config.Text("STEM GAMES", 20)
    header.pos = ((config.window.size[0] - header.font.size(header.message)[0])/2, 570)
    footer.pos = ((config.window.size[0] - footer.font.size(footer.message)[0])/2, 690)
    ufo = ufo.BigUFO(6, 1)
    hud = hud.HUD()

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
        self.ufo.move()
