from config import img
from pygame import transform

# Snake properties
snake_colors = ["red", "yellow", "purple", "green"]
snake_imgs = []
for i in range(4):
    aux = []
    for j in range(3):
        aux.append(img("snake_" + snake_colors[i] + str(j + 1)))
    snake_imgs.append(aux)
snake = snake_imgs[0][0].get_rect()


# Rotates the snake image by the given angle
def rotate_imgs(angle, current_snake):
    for k in range(3):
        snake_imgs[current_snake][k] = transform.rotate(snake_imgs[current_snake][k], angle)
