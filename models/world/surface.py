import pygame


class Surface(object):
    def __init__(self, width: int, height: int, **kwargs):
        self.fps = kwargs.get('fps') or 60
        self.color = kwargs.get('color') or 'black'
        self.img = self.convert_image(kwargs.get('img'))

        self.instance = pygame.display.set_mode((width, height))

    @staticmethod
    def convert_image(image: str = None):
        if image is not None:
            return pygame.image.load(image).convert()

    def draw_background(self):
        if self.img is not None:
            self.instance.blit(self.img, (0, 0))
        else:
            self.instance.fill(self.color)

    def draw_item(self, item):
        item.draw(surface=self.instance)

    def draw_items(self, items):
        for item in items:
            item.draw(surface=self.instance)
