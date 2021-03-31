from pygame.time import Clock
import pygame
import config
from game_screen import GameScreen
from game_logic import  GameLogic


class GameLoop:
    """Implementando o loop principal"""

    def __init__(self, player):
        self._player = player
        self._screen = GameScreen()
        self.__logic = GameLogic()

    def start(self):
        alive = True
        clock = Clock()
        self._screen.draw(self._player.score, start_msg=True)  # aqui a mensgem de "press fica true e desenhaos o score
        ask_start = True
        while ask_start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    ask_start = False
                    break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        while alive:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            move = self._player.act()
            state = self._logic.update(move)  #aqui tem as condicoes de quando a cobra bate nela mesma, quando bate nos obstasuclos ou quando come uma fruta
            alive = (state != GameLogic.State.DEAD)

            if state == GameLogic.State.FOOD_EATEN:  # quando ela come a cobra, e essa verificação deve ser feita da classe GameLogic
                self._player.score += config.FOOD_APPLE  # MAS TEM Q VERIFICAR QUAL FOI A FRUTA QUE FOI COMIDA

            # draw
            self._screen.draw(self._player.score)
            clock.tick(config.fps)

            if not alive:
                break
