from pygame.time import Clock
import pygame
import config
from snake import Player, ArtificialIntelligence
from fruit import Fruit
from wall import Wall


class GameLoop:
    """Implementando o loop principal"""

    def __init__(self):
        self.screen = GameScreen()

        self.snake = Player(config.color_0D6895, config.color_0B3C53, [(416, 288), (384, 288), (352, 288)],
                            'assets/player_head.png')
        self.ia = ArtificialIntelligence(config.color_C0771C, config.color_C01C1C, [(672, 288), (640, 288), (608, 288)],
                                         'assets/ia_head.png')
        self.fruit = Fruit()
        self.wall = Wall()

    def start(self):
        alive = True
        clock = Clock()
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

            if (self.snake.position[0][1] in [32, 608]) \
                    or (self.snake.position[0][0] in [0, 1248]) \
                    or (self.snake.position[0] in self.ia.position) \
                    or (
                    self.snake.position[0] in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192),
                                               (1056, 448)]):
                direction = 0
                self.snake.reset([(416, 288), (384, 288), (352, 288)])

            if (self.ia.position[0][1] in [32, 608]) \
                    or (self.ia.position[0][0] in [0, 1248]) \
                    or (self.ia.position[0] in self.snake.position) \
                    or (
                    self.ia.position[0] in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192), (1056, 448)]):
                self.ia.reset([(672, 288), (640, 288), (608, 288)])

            config.screen.fill((0, 0, 0))

            # moves snake
            self.snake.snake_moves(direction)
            self.ia.ia_moves(self.fruit._fruit_position)

            # new body add
            self.snake.new_body(self.fruit._fruit_position)
            self.ia.new_body(self.fruit._fruit_position)

            # change position of apple
            self.fruit.change_position(self.snake.position)
            self.fruit.change_position(self.ia.position)

            # draw
            self.wall.draw_wall()
            self.snake.draw_snake()
            self.ia.draw_snake()
            self.fruit.draw_fruit()

            pygame.display.update()
