import pygame
import random
from events import EngineEvent
from games.cannondefense.game import CannonDefender as Game

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


class Engine:
    background = None
    settings = {}
    display = None
    clock = None
    enable_logging = True
    # game is just an injected dependency, main menu could swap games out
    # too bad python doesn't use interfaces :(  quack quack
    game = None

    def __init__(self):
        pygame.init()
        settings['resolution'] = (
            settings['screen_width'],
            settings['screen_height']
        )
        self.display = pygame.display.set_mode(settings['resolution'])
        self.clock = pygame.time.Clock()
        self.game = Game()
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
                self.process_game_events(pygame.event.get(), delta_t)

            # set background before rendering entities
            self.set_background()

            # events have updated the entity objects, we can update the surface now
            for i, entity in self.game.entities.items():
                self.display.blit(entity.get_image(), entity.get_next_position(delta_t))

            pygame.display.flip()
            self.clock.tick(settings['fps'])
        self.main_menu()

    def set_background(self):
        if self.background is None:
            bg = pygame.image.load(self.game.get_background_path())
            bg = pygame.transform.scale(bg, settings['resolution'])
            self.background = bg
        self.display.blit(self.background, (0, 0))

    def process_game_events(self, events, delta_t):
        for event in events:
            if EngineEvent.is_exit_game(event):
                self.exit_game()
            self.game.process_game_event(event)

    def init_entities(self):
        for key, entity in self.game.entities.items():
            entity.init()
            image = pygame.image.load(entity.get_image_path())
            entity.set_image(image)

    def init_sounds(self):
        self.game.init_sounds()

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

    @staticmethod
    def exit_game():
        pygame.quit()
        quit()
