from random import randrange
from game import img, set_obj_coordinates
from config import window
from snake import snake

# Fruits properties
fruits_imgs = [[] for x in range(4)]
img_names = ["apple", "banana", "grape", "avocado"]
for i in range(len(fruits_imgs)):
    for j in range(3):
        fruits_imgs[i].insert(j, img(img_names[i] + str(j + 1)))

general_fruit = fruits_imgs[0][0].get_rect()


def random_fruit(body_pos):
    global general_fruit  # Fruit rectangle coordinates
    while True:
        general_fruit.x = randrange(1, (window[0] // snake.w) - 1) * snake.w
        general_fruit.y = randrange(3, (window[1] // snake.h) - 1) * snake.h
        if not any(pos == (general_fruit.x, general_fruit.y) for pos in
                   body_pos):  # Checks if the fruit spawn position is not the same as the snake's body
            break
    set_obj_coordinates(general_fruit, general_fruit.x, general_fruit.y)  # set fruit random position
