import config
import menu
import pygame

credits_surf = pygame.Surface(config.window_size)
back_button_dimension = (240, 50)
back_button = config.Button(back_button_dimension, (menu.button_center_x, 500), menu.menu_button_dimension, "Back")
back_button.set_selected(True)


def display_credits():
    while config.options["in_credits"]:
        for event in pygame.event.get():
            config.check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    config.options["in_credits"] = False
        config.screen.blit(credits_surf, (0, 0))
        back_button.draw(credits_surf)
        pygame.display.update()
