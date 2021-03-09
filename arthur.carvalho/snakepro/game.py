from config import *


def scoring(sp, ap):
    global score
    score_text = score_font.render(f'Score: {score}', True, color_white, color_black)
    screen.blit(score_text, (0, 0))

    if sp == ap:
        score += 1


# score
score_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
score = 0
