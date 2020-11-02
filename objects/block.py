from random import randrange

import pygame


class Block(object):
    def __init__(self, col: int, row: int, world_width: int, world_height: int, **kwargs):
        offset = kwargs.get('offset') or 10
        distance = kwargs.get('distance') or 20

        self.height = self.calculate_side(world_limit=world_height, offset=offset, distance=distance, max_value=15)
        self.width = self.calculate_side(world_limit=world_width, offset=offset, distance=distance, max_value=10)

        self.x = offset + (self.width + distance) * col
        self.y = offset + (self.height + distance) * row

        self.hp = 1
        self.color = kwargs.get('color') or (randrange(30, 256), randrange(30, 256), randrange(30, 256))

        self.level = kwargs.get('level')
        if self.level is not None:
            self.change_level()

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

    def hit(self):
        self.level -= 1
        self.change_level()
        return self.level

    def change_level(self):
        if self.level == 1:
            self.hp = 1
            self.color = 'yellow'

        elif self.level == 2:
            self.hp = 2
            self.color = 'green'

        elif self.level == 3:
            self.hp = 3
            self.color = 'blue'

    @staticmethod
    def calculate_side(world_limit: int, offset: int, distance: int, max_value: int) -> int:
        return (world_limit - (offset + distance * max_value)) // max_value
