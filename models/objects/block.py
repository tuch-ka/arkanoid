from random import randrange

import pygame

from models.abc.abc_objects import VisibleObject


class Block(VisibleObject):
    def __init__(self, col: int, row: int, world_width: int, world_height: int, **kwargs):
        offset = kwargs.get('offset') or 10
        distance = kwargs.get('distance') or 20
        self.color = kwargs.get('color') or (randrange(30, 256), randrange(30, 256), randrange(30, 256))

        self.height = self.calculate_side(world_limit=world_height, offset=offset, distance=distance, max_value=15)
        self.width = self.calculate_side(world_limit=world_width, offset=offset, distance=distance, max_value=10)

        self.x = offset + (self.width + distance) * col
        self.y = offset + (self.height + distance) * row

        self.instance = None

    @classmethod
    def create(cls, world, *args, **kwargs) -> 'Block':

        block = cls(
            *args,
            **kwargs,
            world_width=world.width,
            world_height=world.height,
        )

        block.instance = pygame.Rect(
            block.x,
            block.y,
            block.width,
            block.height,
        )
        return block

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.color, self.instance)

    @staticmethod
    def calculate_side(world_limit: int, offset: int, distance: int, max_value: int) -> int:
        return (world_limit - (offset + distance * max_value)) // max_value
