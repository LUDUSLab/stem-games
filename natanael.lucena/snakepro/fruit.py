from random import randrange

# Fruits properties
fruits_imgs = [[] for x in range(4)]
general_fruit = img("apple1").get_rect()
general_fruit_x, general_fruit_y = 0, 0
img_names = ["apple", "banana", "grape", "avocado"]
for i in range(len(fruits_imgs)):
    for j in range(3):
        fruits_imgs[i].insert(j, img(img_names[i] + str(j + 1)))


def random_fruit(body_pos):
    global general_fruit_x, general_fruit_y  # Fruit rectangle coordinates
    while True:
        general_fruit_x = randrange(window[0] // snake.w) * snake.w
        general_fruit_y = randrange(window[1] // snake.h) * snake.h
        if not any(pos == (general_fruit_x, general_fruit_y) for pos in
                   body_pos):  # Checks if the fruit spawn position is not the same as the snake's body
            break
    set_obj_coordinates(general_fruit, general_fruit_x, general_fruit_y)  # set fruit random position
