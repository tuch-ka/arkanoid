from typing import List

import pygame

from handlers import PaddleHandler, BallHandler, BlockHandler
from models.abc.abc_objects import VisibleObject


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

    def draw_paddle(self):
        PaddleHandler.draw(surface=self.instance)

    def draw_balls(self):
        BallHandler.draw(surface=self.instance)

    def draw_blocks(self):
        BlockHandler.draw(surface=self.instance)
