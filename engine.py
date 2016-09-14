import pygame
import random
from entities import YellowSpaceship

settings = {
    'screen_width': 1024,
    'screen_height': 768,
    'screen_title': 'No u',
    'fps': 30,
    'colors': {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
    },
}


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


class Engine:
    background = None
    settings = {}
    display = None
    avatar_image = None
    clock = None
    enable_logging = True
    # dict of entity objects to be rendered
    entities = {}

    def __init__(self):
        pygame.init()
        settings['resolution'] = (
            settings['screen_width'],
            settings['screen_height'],
        )
        self.display = pygame.display.set_mode(settings['resolution'])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(settings['screen_title'])
        random.seed()

    def game_loop(self):
        self.init_entities()

        self.init_sounds()

        program_loop = True
        while program_loop:
            # how much time has passed since the last iteration
            delta_t = self.clock.get_time()

            # read events and process accordingly
            # we should probably whitelist pygame events, so that we don't clutter the event queue
            # game input events don't need to be processed on every iteration
            # this however, is a ghetto way of doing it
            if random.randint(1, 5) == 2:
                for event in pygame.event.get():
                    self.process_game_event(event)

            # set background before rendering entities
            self.set_background()

            # events have updated the entity objects, we can render them now
            for i, entity in self.entities.items():
                self.display.blit(entity.get_image(), entity.get_pos(delta_t))

            pygame.display.flip()
            self.clock.tick(settings['fps'])
        self.main_menu()

    def init_entities(self):
        spaceship1 = YellowSpaceship((400, 300))
        image = pygame.image.load(spaceship1.get_image_path())
        image = pygame.transform.scale(image, (40, 40))
        spaceship1.set_image(image)
        # add to entities, will be rendered on first iteration
        self.entities['spaceship'] = spaceship1

    def init_sounds(self):
        # sounds
        # if 'win' in sys.platform:
        #     soundExt = '.wav'
        # else:
        #     soundExt = '.ogg'
        # SOUNDS['die'] = pygame.mixer.Sound('assets/audio/die' + soundExt)
        # SOUNDS['hit'] = pygame.mixer.Sound('assets/audio/hit' + soundExt)
        # SOUNDS['point'] = pygame.mixer.Sound('assets/audio/point' + soundExt)
        # SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt)
        # SOUNDS['wing'] = pygame.mixer.Sound('assets/audio/wing' + soundExt)
        pass

    def process_game_event(self, event):
        if EngineEvent.is_exit_game(event):
            self.exit_game()

        if EngineEvent.is_mouse_l(event):
            self.entities['spaceship'].move_to(event.pos)

    def set_background(self):
        if self.background is None:
            bg = pygame.image.load('./assets/space_bg.png')
            bg = pygame.transform.scale(bg, settings['resolution'])
            self.background = bg
        self.display.blit(self.background, (0, 0))

    # not used yet
    def main_menu(self):
        self.display.fill(settings['colors']['white'])
        menu_loop = True
        while menu_loop:
            for event in pygame.event.get():
                if EngineEvent.is_exit_game(event):
                    self.exit_game()

            self.display.blit(self.display, (0, 0))
            pygame.display.flip()
            self.clock.tick(settings['fps'])

    def exit_game(self):
        pygame.quit()
        quit()
