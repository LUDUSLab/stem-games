from random import randrange
from config import window, img, set_obj_coordinates, BLOCK_SIZE

# Fruits properties
fruits_imgs = [[] for x in range(4)]
img_names = ["apple", "banana", "grape", "avocado"]
for i in range(len(fruits_imgs)):
    for j in range(3):
        fruits_imgs[i].insert(j, img(img_names[i] + str(j + 1)))

general_fruit = fruits_imgs[0][0].get_rect()


# Define the right location for fruit's spawn
def random_fruit(body_pos):
    global general_fruit  # Fruit rectangle coordinates
    while True:
        general_fruit.x = randrange(4, (window[0] // BLOCK_SIZE) - 4) * BLOCK_SIZE
        general_fruit.y = randrange(4, (window[1] // BLOCK_SIZE)) * BLOCK_SIZE
        # Check if the fruit spawn position is not the same as the snake's body
        if not any(pos == (general_fruit.x, general_fruit.y) for pos in body_pos):
            break
    set_obj_coordinates(general_fruit, general_fruit.x, general_fruit.y)  # set fruit random position
