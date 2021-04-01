import pygame
import pygame_menu
from snake import *
from fruits import *
import config
from wall import Wall


class MainMenu:
    def __init__(self, height, width, title, theme=pygame_menu.themes.THEME_GREEN):
        self._width = width
        self._height = height
        self._theme = theme

        self._screen = pygame.display.set_mode((width, height))
        self._menu = pygame_menu.Menu(height, width, title, theme=theme)

        self._menu.add_button('Play', self._play_game)
        self._menu.add_button('Credits', self._credits)
        self._menu.add_button('Settings', self._setting)

        self._menu.add_vertical_margin(100)
        self._menu.add_button('Quit', pygame_menu.events.EXIT)
        self._menu.mainloop(self._screen)

    @staticmethod
    def _play_game():
        player = Player(config.color_0D6895,
                        config.color_0B3C53,
                        [(416, 288), (384, 288), (352, 288)],
                        'assets/player_head.png')

        ai = ArtificialIntelligence(config.color_C0771C,
                                    config.color_C01C1C,
                                    [(672, 288), (640, 288), (608, 288)],
                                    'assets/ia_head.png')

        wall = Wall()

        fruit = Fruit()

        score_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
        score_text = score_font.render('Score: 0', True, (0, 0, 0), (255, 255, 255))

        direction = 0

        alive = True
        died = False

        while alive:
            config.game_clock.tick(config.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if not direction == 3:
                        if event.key == pygame.K_w:
                            direction = 1

                    if not direction == 4:
                        if event.key == pygame.K_a:
                            direction = 2

                    if not direction == 1:
                        if event.key == pygame.K_s:
                            direction = 3

                    if not direction == 2:
                        if event.key == pygame.K_d:
                            direction = 4

            if (player.position[0][1] in [32, 608]) \
                    or (player.position[0][0] in [0, 1248]) \
                    or (player.position[0] in ai.position) \
                    or (
                    player.position[0] in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192), (1056, 448)]):

                direction = 0
                config.game_over.play()
                player.score = 0
                score_text = score_font.render(f'Score: {player.score}', True, (0, 0, 0), (255, 255, 255))
                player.reset([(416, 288), (384, 288), (352, 288)])
                died = True

                alive = False

            if (ai.position[0][1] in [32, 608]) \
                    or (ai.position[0][0] in [0, 1248]) \
                    or (ai.position[0] in player.position) \
                    or (
                    ai.position[0] in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192), (1056, 448)]):
                ai.reset([(672, 288), (640, 288), (608, 288)])

            if player.position[0] == fruit.position:
                if fruit.type == 0:
                    player.score += 1
                    config.eat_fruit.play()

                elif fruit.type == 1:
                    player.score += 5
                    config.eat_fruit.play()

                elif fruit.type == 2:
                    player.score += 10
                    config.eat_fruit.play()

                elif fruit.type == 4:
                    player.score += 20
                    config.eat_fruit.play()

                score_text = score_font.render(f'Score: {player.score}', True, (0, 0, 0), (255, 255, 255))

                fruit.choose_fruit()
                fruit.change_position()
                player.new_body()

            if ai.position[0] == fruit.position:
                if fruit.type == 0:
                    ai.score += 1

                elif fruit.type == 1:
                    ai.score += 5

                elif fruit.type == 2:
                    ai.score += 10

                elif fruit.type == 3:
                    ai.score += 20
                fruit.choose_fruit()
                fruit.change_position()
                ai.new_body()

            # moves snake
            player.snake_moves(direction)
            ai.ia_moves(fruit.position)

            # draw
            screen.fill((46, 139, 87))
            screen.blit(score_text, (0, 0))

            wall.draw_wall()
            fruit.draw_fruit()
            ai.draw_snake()
            player.draw_snake()

            pygame.display.update()

    def _credits(self):
        CreditsMenu(self._height, self._width, theme=self._theme)

    def _setting(self):
        SettingMenu(self._height, self._width, theme=self._theme)


class CreditsMenu:
    def __init__(self, height, width, title="Credits", theme=pygame_menu.themes.THEME_DARK):
        self._width, self._height = width, height
        self._screen = pygame.display.set_mode((width, height))
        self._menu = pygame_menu.Menu(height, width, title, theme=theme)
        self._menu.add_label("Create by ")
        self._menu.add_label("Allef Oliveira Ramos")
        self._menu.add_label("Arthur Gustavo Paiva Carvalho")
        self._menu.add_label("Emanuel Henrique Oliveira Dias")
        self._menu.add_label("Gabriela Breval de Oliveira Santiago ")

        self._menu.add_vertical_margin(100)
        self._menu.add_button("Back", self._menu.disable)
        self._menu.mainloop(self._screen)


class SettingMenu:
    def __init__(self, height, width, title="Settings", theme=pygame_menu.themes.THEME_DARK):
        self._width, self._height = width, height
        self._screen = pygame.display.set_mode((width, height))
        self._menu = pygame_menu.Menu(height, width, title, theme=theme)

        self._menu.add_vertical_margin(100)
        self._menu.add_button("Back", self._menu.disable)
        self._menu.mainloop(self._screen)