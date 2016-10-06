

class BaseGame(object):
    # dict of entity objects to be rendered
    entities = {}
    background_image = None
    background_image_path = None

    def init_sounds(self):
        raise NotImplementedError('Must implement method')

    def process_game_event(self, event):
        raise NotImplementedError('Must implement method')

    def get_background_path(self):
        return self.background_image_path

    def set_background_image(self, image):
        self.background_image = image
