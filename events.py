import pygame


class EngineEvent(object):
    # event helper class
    MOUSE_SCROLL_DOWN = 5
    MOUSE_SCROLL_UP = 4
    MOUSE_R = 3
    MOUSE_M = 2
    MOUSE_L = 1

    @staticmethod
    def is_exit_game(event):
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x)

    @staticmethod
    def is_mouse_l(event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == EngineEvent.MOUSE_L