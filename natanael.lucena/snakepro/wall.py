from config import img, window, screen

wall_imgs = []

def create_wall_img():
    for i in range(3):
        wall_imgs.insert(i, img("stone-block" + str(i+1)))

def draw_wall():
    general_wall = wall_imgs[0].get_rect()
    aux = 0
    while general_wall.x < window[0]:
        general_wall.y = 0
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y = window[1] - general_wall.h
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x += general_wall.w
        aux += 1
        if aux > 2:
            aux = 0
    general_wall.y = general_wall.h
    while general_wall.y < window[1] - general_wall.h:
        general_wall.x = 0
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x = window[0] - general_wall.w
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y += general_wall.h
        aux += 1
        if aux > 2:
            aux = 0