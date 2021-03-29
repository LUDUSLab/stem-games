import pygame
import pygame_menu


class MainMenu:
    def __init__(self, height, width, title, theme=pygame_menu.themes.THEME_DARK):
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

    def _play_game(self):
        pass

    def _credits(self):
        CreditsMenu(self._height, self._width, theme=self._theme)
        pygame.display.set_mode((self._width, self._height))

    def _setting(self):
        SettingMenu(self._height, self._width, theme=self._theme)
        pygame.display.set_mode((self._width, self._height))


class CreditsMenu:
    def __init__(self, height, width, title="Credits", theme=pygame_menu.themes.THEME_DARK):
        self._width, self._height = width, height
        self._screen = pygame.display.set_mode((width, height))
        self._menu = pygame_menu.Menu(height, width, title, theme=theme)
        self._menu.add_label("Criators: ")
        self._menu.add_label("Allef")
        self._menu.add_label("Arthur")
        self._menu.add_label("Emanuel")
        self._menu.add_label("Gabriela Breval de Oliveira Santiago ")

        self._menu.add_vertical_margin(100)
        self._menu.add_button("Back", self._menu.disable)
        self._menu.mainloop(self._screen)


class SettingMenu:
    def __init__(self, height, width, title="Credits", theme=pygame_menu.themes.THEME_DARK):
        self._width, self._height = width, height
        self._screen = pygame.display.set_mode((width, height))
        self._menu = pygame_menu.Menu(height, width, title, theme=theme)

        self._menu.add_vertical_margin(100)
        self._menu.add_button("Back", self._menu.disable)
        self._menu.mainloop(self._screen)
