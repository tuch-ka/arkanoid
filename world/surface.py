import pygame

from defaults import SurfaceConfig


class Surface(object):
    def __init__(self, **kwargs) -> None:
        self.width = kwargs.get('width') or SurfaceConfig.width
        self.height = kwargs.get('height') or SurfaceConfig.height

        self.fps = kwargs.get('fps') or SurfaceConfig.fps
        self.color = kwargs.get('color') or SurfaceConfig.color
        self.img = self.convert_image(kwargs.get('img'))

        self.clock = pygame.time.Clock()
        self.instance = pygame.display.set_mode((self.width, self.height))

    @staticmethod
    def convert_image(image: str = None):
        if image is not None:
            return pygame.image.load(image).convert()

    def flip(self) -> None:
        pygame.display.flip()
        self.clock.tick(self.fps)

    def draw_background(self) -> None:
        if self.img is not None:
            self.instance.blit(self.img, (0, 0))
        else:
            self.instance.fill(self.color)

    def draw(self, handler) -> None:
        handler.draw(surface=self.instance)
