from random import randrange

import pygame


class Block(object):
    def __init__(self, col: int, row: int, width: int = 100, height: int = 50, offset: int = 10, distance: int = 20):
        self.height = height
        self.width = width
        self.x = offset + (width + distance) * col
        self.y = offset + (height + distance) * row

        self.color = randrange(30, 256)

        self.instance = None

    @classmethod
    def create(cls, *args, **kwargs):
        block = cls(*args, **kwargs)
        block.instance = pygame.Rect(
            block.x,
            block.y,
            block.width,
            block.height,
        )
        return block

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.instance)
