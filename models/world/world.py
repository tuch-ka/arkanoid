import pygame

from models.world.surface import Surface
from models.objects import *


class World(object):
    def __init__(self, width: int = 800, height: int = 600, **kwargs):
        self.width = width
        self.height = height

        self.fps = kwargs.get('fps') or 60

        self.clock = pygame.time.Clock()
        self.surface = Surface(width=self.width, height=self.height)

        self.paddle = None
        self.balls = []
        self.blocks = []

    def add_paddle(self, **kwargs):
        self.paddle = Paddle.create(world=self, **kwargs)

    def add_ball(self):
        self.balls.append(Ball.create(world=self))

    def clear_balls(self):
        self.balls = []

    def add_blocks(self, columns: int = 10, rows: int = 4):
        self.blocks = [
            Block.create(world=self, col=i, row=j)
            for i in range(columns)
            for j in range(rows)
        ]

    def clear_blocks(self):
        self.blocks = []

    def move_balls(self):
        for ball in self.balls:
            ball.move()
            ball.collision_world(world=self)
            ball.collision_paddle(paddle=self.paddle.instance)

    def draw_objects(self):
        self.surface.draw_background()

        self.surface.draw_item(self.paddle)
        self.surface.draw_items(self.balls + self.blocks)

        self.wait()

    def init(self):
        if self.paddle is None:
            self.add_paddle()
        if self.balls:
            self.clear_balls()
        if self.blocks:
            self.clear_blocks()

    def wait(self):
        pygame.display.flip()
        self.clock.tick(self.fps)
