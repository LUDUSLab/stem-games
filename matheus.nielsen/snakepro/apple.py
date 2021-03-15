from screen import *
from random import randrange
import pygame


points = 0
apple_coord = (randrange(grid_square, play_area[0] - grid_square, grid_square),
               randrange(hud_y + grid_square, play_area[1] - grid_square, grid_square))
sprite = pygame.image.load('assets/matheus.nielsen_apple.png')


# randomizes apple's location
def randomize():
    global apple_coord
    apple_coord = (randrange(grid_square, play_area[0] - grid_square, grid_square),
                   randrange(hud_y + grid_square, play_area[1] - grid_square, grid_square))
    print(apple_coord)


# apple render
def blit():
    screen.blit(sprite, apple_coord)


# game score controller
def score():
    global points
    points += 1
    randomize()
    score_sfx.play()


# exports apple's coordinates
def get_coord():
    return apple_coord


# exports game points
def get_points():
    return points
