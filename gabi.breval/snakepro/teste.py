#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import, division, print_function
from itertools import cycle
import pygame
from snake_sem_modulos import address


VISITOR_TTF_FILENAME = address('gabi.brevalFont.otf', 'font')
BLINK_EVENT = pygame.USEREVENT + 0


def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((800, 600))
        screen_rect = screen.get_rect()

        clock = pygame.time.Clock()

        font = pygame.font.Font(VISITOR_TTF_FILENAME, 50)
        on_text_surface = font.render(
            'Press Any Key To Start', True, pygame.Color('green3')
        )
        blink_rect = on_text_surface.get_rect()
        blink_rect.center = screen_rect.center
        off_text_surface = pygame.Surface(blink_rect.size)
        blink_surfaces = cycle([on_text_surface, off_text_surface])
        blink_surface = next(blink_surfaces)
        pygame.time.set_timer(BLINK_EVENT, 150)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)

            screen.blit(blink_surface, blink_rect)
            pygame.display.update()
            clock.tick(50)
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
