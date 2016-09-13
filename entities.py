from pygame import math


class BaseEntity(object):
    STATE_STOPPED = 'stopped'
    STATE_MOVING = 'moving'

    image_path = None
    movement_path = []
    image = None
    speed = 0
    angle = 0
    position = None
    delta_time = 0
    state = STATE_STOPPED

    def __init__(self, pos, velocity=(0, 0)):
        self.position = pos
        self.velocity = math.Vector2(velocity[0], velocity[1])
        self.gravity = math.Vector2(0, 0)

    def set_delta_time(self, delta_time):
        self.delta_time = delta_time

    def get_pos(self, delta_time):
        raise NotImplementedError

    # this class is not interested in the image format,
    # but simply is storing the image for the engine to access as needed
    def set_image(self, image):
        self.image = image

    def get_image(self):
        if self.image is None:
            raise RuntimeError('Must set_image() before using get_image()')
        return self.image

    # def attack(self, attack_pos):
    #     raise NotImplementedError

    def stop(self):
        self.speed = 0

    def get_image_path(self):
        return self.image_path

    def move_to(self, destination_pos):
        self.state = self.STATE_MOVING
        self.speed = 5


        destination_vector = Vector(destination_pos)

        self.position = self.position + self.velocity * self.delta_time
        self.velocity = self.velocity + self.gravity * self.delta_time

        # build path from current location to destination
        current_vector = self.movement_path.pop(1)
        # need to find ratio of height to width of our

        # x_movement = abs(current_pos[0] - destination_pos[0])
        # y_movement = abs(current_pos[1] - destination_pos[0])

        # new_movement_path = [current_pos]
        # while True:
        #     current_pos[0] += int(x_lcd)
        #     current_pos[1] += int(y_lcd)
        #     new_movement_path.append(current_pos)


class BaseSpaceship(BaseEntity):
    def get_pos(self, delta_time):
        self.delta_time = delta_time

        if self.state == self.STATE_MOVING:
            pass

        return self.position

    def stop(self):
        self.stop()
        self.hover()

    def hover(self):
        # ideally we'll use the move_to method to just move up and down
        # we'll deviate 7 pixels up and down to hover
        hover_matrix = [
            0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1,
            0, -1, -2, -3, -4, -5, -6, -7, -6, -5, -4, -3, -2, -1
        ]
        for modifier in hover_matrix:
            self.movement_path.append((
                self.position[0],
                self.position[1] + modifier,
            ))


class YellowSpaceship(BaseSpaceship):
    image_path = 'assets/guibuttons/YellowButton-Active.png'
