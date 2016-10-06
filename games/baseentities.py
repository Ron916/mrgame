from pygame import math


class BaseEntity(object):
    STATE_STOPPED = 'stopped'
    STATE_MOVING = 'moving'

    gravity = (0, 1)
    image_path = None
    image = None
    vector = None
    current_speed = 0
    max_speed = 1
    position = None
    state = STATE_STOPPED

    def __init__(self, position):
        self.position = math.Vector2(position[0], position[1])
        self.gravity = math.Vector2(0, 0)

    def init(self):
        # optional
        pass

    def get_next_position(self, delta_time):
        # if we're moving, set the vector length according to speed
        # then return the endpoint
        if self.state == self.STATE_MOVING:
            self.position = math.Vector2()
            pass
        else:
            pass

        return self.position

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
        self.current_speed = self.max_speed
        self.vector = math.Vector2(destination[0], destination[1])

    def stop(self):
        self.vector = None
        self.current_speed = 0
        self.state = self.STATE_STOPPED


class BaseProjectile(object):
    RADIUS = 1

    gravity = 1
    x = None
    y = None
    time_interval = None
    angle = None
    x_velocity = None
    y_velocity = None
    is_flying = True
    x_delta = None
    container = None
    hit_ground = None

    def __init__(self, initial_x, initial_y, launch_angle, launch_velocity, time_interval):
        self.x = initial_x
        self.y = initial_y
        self.time_interval = time_interval
        self.angle = launch_angle
        self.x_velocity = launch_velocity * math.cos(self.angle)
        self.y_velocity = launch_velocity * math.sin(self.angle)
        self.x_delta = self.time_interval * self.x_velocity

    def move(self):
        prev_y_velocity = self.y_velocity
        self.y_velocity = self.y_velocity - (9.8 * self.time_interval)
        self.y = (self.y + (self.time_interval *
                            ((prev_y_velocity + self.y_velocity) / 2)))
        self.y = max(self.y, 0)
        self.x += (self.x_delta)
        self.container = pygame.Rect(self.x - self.RADIUS, self.y - self.RADIUS, self.RADIUS * 2, self.RADIUS * 2)
        self.is_flying = (self.y > 0)
        self.hit_ground = (self.y <= 0)
