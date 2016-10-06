from pygame import math
from ..baseentities import BaseEntity


class BaseSpaceship(BaseEntity):
    hover_path = []

    def get_pos(self, delta_time):
        if self.state == self.STATE_MOVING:
            pass
        if self.state == self.STATE_STOPPED:
            self.position = self.get_hover_pos()
        return self.position

    def get_hover_pos(self):
        hover_matrix = [
            0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1,
            0, -1, -2, -3, -4, -5, -6, -7, -6, -5, -4, -3, -2, -1
        ]
        if len(self.hover_path) == 0:
            for modifier in hover_matrix:
                self.hover_path.append((
                    self.position[0],
                    self.position[1] + modifier,
                ))
        return self.hover_path.pop()


class YellowSpaceship(BaseSpaceship):
    image_path = 'games/spaceshooter/assets/yellow_spaceship.png'
