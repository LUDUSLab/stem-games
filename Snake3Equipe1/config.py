from pygame.mixer import Sound

BACKGROUND_COLOR = (0, 0, 0)
block_size = 32
fps = 10
screen_dimensions = (1280, 720)

''' # SOUNDS AND FONTS
game_over = Sound('assets/team_I.game-over.wav')
eat_fruit = Sound('assets/team_I.eat.wav')
music = Sound('assets/super_mario.wav')
font = '/assets/PressStart2P.ttf' '''

running_game = False


FOOD_APPLE = 100  # 0      aux = 0
FOOD_BANANA = 200  # 1     aux = 1
FOOD_ORANGE = 1000  # 2     aux = 2

# colours
color_0D6895 = (13, 104, 149)
color_0B3C53 = (11, 60, 83)
color_C01C1C = (192, 28, 28)
color_C0771C = (185, 110, 18)

'''Precisa adicionar um FOOD_SCORE refenrete a cada uma das frutas

FOOD_APPLE = 100
FOOD_BANANA = 200
FOOD_ORANGE = 1000

E ASSIM POR DIANTE... AI SERA USADA A PONTUAÇÃO DA FRUTA Q O JOGADOR
ACABOU DE COMER

'''

'''def pen(size):
    
    return Font(font, size)'''
