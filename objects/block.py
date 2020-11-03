from random import randrange

import pygame

from defaults import BlockConfig, WorldConfig


class Block(object):
    def __init__(self, col: int, row: int, **kwargs) -> None:
        self.offset = kwargs.get('offset') or BlockConfig.offset
        self.distance = kwargs.get('distance') or BlockConfig.distance

        self.height = self.calculate_side(world_limit=WorldConfig.height, max_value=WorldConfig.rows)
        self.width = self.calculate_side(world_limit=WorldConfig.width, max_value=WorldConfig.columns)

        self.x = self.offset + (self.width + self.distance) * col
        self.y = self.offset + (self.height + self.distance) * row

        self.hp = 1
        self.color = kwargs.get('color') or (randrange(30, 256), randrange(30, 256), randrange(30, 256))

        self.level = kwargs.get('level')
        if self.level is not None:
            self.change_level()

        self.instance = None

    @classmethod
    def create(cls, **kwargs) -> 'Block':

        block = cls(**kwargs)

        block.instance = pygame.Rect(
            block.x,
            block.y,
            block.width,
            block.height,
        )
        return block

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.color, self.instance)

    def hit(self) -> int:
        self.level -= 1
        self.change_level()
        return self.level

    def change_level(self) -> None:
        if self.level == 1:
            self.hp = 1
            self.color = 'yellow'

        elif self.level == 2:
            self.hp = 2
            self.color = 'green'

        elif self.level == 3:
            self.hp = 3
            self.color = 'blue'

    def calculate_side(self, world_limit: int, max_value: int) -> int:
        return (world_limit - (self.offset + self.distance * max_value)) // max_value
