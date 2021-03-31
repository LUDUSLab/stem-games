from pygame.time import Clock
import pygame
import config
from game_screen import GameScreen
from game_logic import GameLogic


class GameLoop:
    """Implementando o loop principal"""

    def __init__(self, player):
        self._player = player
        self._screen = GameScreen()
        self._logic = GameLogic()

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
            clock.tick(config.fps)

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

            if (snake.position[0][1] in [32, 608]) \
                    or (snake.position[0][0] in [0, 1248]) \
                    or (snake.position[0] in ia.position) \
                    or (
                    snake.position[0] in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192), (1056, 448)]):
                direction = 0
                snake.reset([(416, 288), (384, 288), (352, 288)])

            if (ia.position[0][1] in [32, 608]) \
                    or (ia.position[0][0] in [0, 1248]) \
                    or (ia.position[0] in snake.position) \
                    or (ia.position[0] in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192), (1056, 448)]):
                ia.reset([(672, 288), (640, 288), (608, 288)])

            screen.fill((0, 0, 0))

            # moves snake
            snake.snake_moves(direction)
            ia.ia_moves(fruit._fruit_position)

            # new body add
            snake.new_body(fruit._fruit_position)
            ia.new_body(fruit._fruit_position)

            # change position of apple
            fruit.change_position(snake.position)
            fruit.change_position(ia.position)

            # draw
            wall.draw_wall()
            snake.draw_snake()
            ia.draw_snake()
            fruit.draw_fruit()

            pygame.display.update()
