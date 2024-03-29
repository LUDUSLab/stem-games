import asteroid
import config
import ship
import ufo
import pygame
from random import randrange

class Scenario:
    min_asteroid_spawn_distance = 200
    min_ship_spawn_distance = 125
    switch_round = False

    def __init__(self, player):
        self.player = player
        self.asteroids_quantity = 4
        self.asteroids = []
        self.projectiles = [[], []]
        self.ship_can_spawn = False
        self.game_over_header = config.Text("GAME OVER", 32)
        self.game_over_header.pos = ((config.window.size[0] - self.game_over_header.text.get_size()[0])/2, 150)
        self.showing_game_over_header = False
        self.aux_time_game_over_header = 185
        self.aux_time = 100
        self.aux_time2 = 0
        self.aux_beat = 50
        self.max_ast_num = 4
        self.aux_ast_spawn_time = 100
        self.ship = ship.Ship(self.projectiles[0].append)
        self.ufo = None
        for _ in range(self.asteroids_quantity):
            while True:
                position = pygame.Vector2(randrange(config.window.size[0]), randrange(config.window.size[1]))
                if position.distance_to(self.ship.position) > self.min_asteroid_spawn_distance:
                    break
            self.asteroids.append(asteroid.Asteroid(position, self.asteroids.append))
        self.player_turn_text = config.Text(f'Player {self.player.id}', 32)
        self.player_turn_text.pos = ((config.window.size[0] -
                                      self.player_turn_text.font.size(self.player_turn_text.message)[0]) / 2, 110)
        self.aux_movey_time = 120
        self.aux_projectile_time = 40

    def display(self):
        if self.aux_time > 0:
            self.player_turn_text.display()
            self.aux_time -= 1
        else:
            if self.aux_beat % (121-6*self.max_ast_num) == 0:
                pygame.mixer.Channel(6).play(config.beat1)
            elif self.aux_beat % (121-6*self.max_ast_num) == (121-6*self.max_ast_num)//2:
                pygame.mixer.Channel(6).play(config.beat2)

            self.aux_beat -= 1
            if self.aux_time2 > 0:
                self.player_turn_text.display()
                self.aux_time2 -= 1
            if len(self.asteroids) == 0 and self.ufo is None:
                self.aux_ast_spawn_time -= 1
                if self.aux_ast_spawn_time <= 0:
                    if self.asteroids_quantity < 10:
                        self.asteroids_quantity += 2
                    for _ in range(self.asteroids_quantity):
                        while True:
                            position = pygame.Vector2(randrange(config.window.size[0]),randrange(config.window.size[1]))
                            if self.ship is not None and position.distance_to(self.ship.position) > \
                                    self.min_asteroid_spawn_distance:
                                break
                        self.asteroids.append(asteroid.Asteroid(position, self.asteroids.append))
                    self.aux_ast_spawn_time = 100
            if self.ufo is not None:
                self.ufo.display()
                if not self.ufo.running_death_animation:
                    self.ufo.move()
                aux_rand = randrange(250)
                if aux_rand == 10 and not self.ufo.moving_y:
                    self.ufo.movey()
                if self.ufo.moving_y:
                    self.aux_movey_time -= 1
                    if self.aux_movey_time <= 0:
                        self.aux_movey_time = 100
                        self.ufo.velocity.y = 0
                        self.ufo.moving_y = False
                self.aux_projectile_time -= 1
                if self.aux_projectile_time <= 0:
                    if self.ship is not None:
                        self.ufo.shoot(self.ship.position)
                        self.aux_projectile_time = 40
                if self.ufo.position.x > 1300 or self.ufo.position.x < -20:
                    pygame.mixer.Channel(4).stop()
                    self.ufo = None
            else:
                randy = randrange(721)
                randx = randrange(1281)
                auxrandsize = randrange(1024)
                size = 1 if auxrandsize < 102 else 2
                if randx == 0 or randx == 1280 and auxrandsize <= 100:
                    self.ufo = ufo.UFO(pygame.Vector2(randx, randy), size, self.projectiles[1].append)
            for ast in self.asteroids:
                ast.display()
                if not ast.running_death_animation:
                    ast.move()
                if self.ufo is not None and ast.collides_with(self.ufo):
                    ast.running_death_animation = True
                    self.ufo.running_death_animation = True
                if ast.running_death_animation:
                    ast.explosion_animation()
                    if ast.animation_aux > 5:
                        self.asteroids.remove(ast)
                        ast.running_death_animation = False
                        ast.animation_aux = 1
                        break
            if self.ufo is not None:
                if self.ufo.running_death_animation:
                    self.ufo.explosion_animation()
                    if self.ufo.animation_aux == 1:
                        pygame.mixer.Channel(5).play(config.asteroid_explosion_sounds[2])
                if self.ufo.animation_aux > 5:
                    self.ufo.running_death_animation = False
                    self.ufo.animation_aux = 1
                    pygame.mixer.Channel(4).stop()
                    self.ufo = None
            for ast in self.asteroids:
                if self.ship is not None:
                    if not self.ship.running_death_animation:
                        if ast.collides_with(self.ship):
                            ast.running_death_animation = True
                            self.player.lives -= 1
                            self.ship.running_death_animation = True
                            ast.split()
                            if len(self.asteroids) > self.max_ast_num:
                                self.max_ast_num = len(self.asteroids)
                            self.player.score += ast.score
                            if self.player.lives <= 0:
                                self.showing_game_over_header = True
                            break

            if self.ship is None:
                for ast in self.asteroids:
                    if pygame.Vector2(config.middle).distance_to(ast.position) < self.min_ship_spawn_distance:
                        self.ship_can_spawn = False
                        break
                    else:
                        self.ship_can_spawn = True
                if self.ufo is not None and pygame.Vector2(config.middle).distance_to(self.ufo.position)\
                        < self.min_ship_spawn_distance:
                    self.ship_can_spawn = False

                if self.ship_can_spawn and not self.showing_game_over_header:
                    self.switch_round = True
                    self.ship = ship.Ship(self.projectiles[0].append)

            if self.ship is not None:
                if self.ship.running_death_animation:
                    self.ship.death_animation()
                    if self.ship.death_animation_time <= 0:
                        self.ship.death_animation_time = 170
                        self.ship.running_death_animation = False
                        self.ship = None

            for p_lst in self.projectiles:
                for p in p_lst:
                    p.display()
                    p.move()
                    p.time_alive -= 1.45
                    if p.time_alive <= 0:
                        p_lst.remove(p)
                        break
                    for ast in self.asteroids:
                        if not ast.running_death_animation and ast.collides_with(p):
                            ast.running_death_animation = True
                            p_lst.remove(p)
                            ast.split()
                            if len(self.asteroids) > self.max_ast_num:
                                self.max_ast_num = len(self.asteroids)
                            if p_lst is self.projectiles[0]:
                                self.player.score += ast.score
                            break

                    if self.ufo is not None and p_lst is self.projectiles[0] and p.collides_with(self.ufo):
                        self.player.score += self.ufo.score
                        p_lst.remove(p)
                        self.ufo.running_death_animation = True
                        break
                    if self.ship is not None and p_lst is self.projectiles[1] and p.collides_with(self.ship) and\
                            not self.ship.running_death_animation:
                        self.ship.running_death_animation = True
                        self.player.lives -= 1
                        break

            if self.ship is not None:
                if not self.ship.running_death_animation:
                    self.ship.move()
                if not self.switch_round:
                    self.ship.display()
                if self.ufo is not None:
                    if not self.ship.running_death_animation and not self.ufo.running_death_animation and \
                            self.ship.collides_with(self.ufo):
                        self.ufo.running_death_animation = True
                        self.ship.running_death_animation = True
                        self.player.lives -= 1
                        self.player.score += self.ufo.score
                        if self.player.lives <= 0:
                            self.showing_game_over_header = True
            if self.showing_game_over_header:
                self.aux_time_game_over_header -= 1
                if self.aux_time_game_over_header >= 0:
                    self.game_over_header.display()
                else:
                    self.aux_time_game_over_header = 100
                    self.showing_game_over_header = False
