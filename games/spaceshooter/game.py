from events import EngineEvent
from games.spaceshooter.entities import YellowSpaceship
from games.basegame import BaseGame
# sadface, I wanted to limit the pygame dependency, but need it here
# other option would be an adapter class but meh, too much for now
import pygame

class SpaceShooter(BaseGame):

    background_image_path = './games/spaceshooter/assets/space_bg.png'

    def __init__(self):
        self.init_entities()

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

    def init_entities(self, ):
        yellow_spaceship = YellowSpaceship((200, 200))
        surface = pygame.image.load(yellow_spaceship.get_image_path())
        yellow_spaceship.set_image(surface)
        self.entities['spaceship1'] = yellow_spaceship

    def process_game_event(self, event):
        if EngineEvent.is_mouse_l(event):
            self.entities['spaceship'].move_to(event.pos)

    def set_background_image(self, image):
        self.background_image = image
