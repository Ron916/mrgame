from pygame import math, rect


class BaseEntity(object):
    STATE_STOPPED = 'stopped'
    STATE_MOVING = 'moving'

    mass = 1
    image_path = None
    image = None
    destination = None
    speed = 0
    position = None
    state = STATE_STOPPED

    def __init__(self, position, velocity=(0, 0)):
        self.position = math.Vector2(position[0], position[1])
        self.velocity = math.Vector2(velocity[0], velocity[1])
        self.gravity = math.Vector2(0, 0)

    def get_pos(self, delta_time):
        raise NotImplementedError

    # this object is not interested in the image format,
    # but simply is storing the image for the engine to access as needed
    def set_image(self, image):
        self.image = image

    def get_image(self):
        if self.image is None:
            raise RuntimeError('Must set_image() before using get_image()')
        return self.image

    def get_image_path(self):
        return self.image_path

    def move_to(self, destination):
        self.state = self.STATE_MOVING
        self.speed = 5
        self.destination = destination


class BaseSpaceship(BaseEntity):
    hover_path = []

    def get_pos(self, delta_time):
        if self.state == self.STATE_MOVING:
            self.position = self.position + self.velocity * delta_time
            self.velocity = self.velocity + self.gravity * delta_time
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
    image_path = 'assets/guibuttons/YellowButton-Active.png'
