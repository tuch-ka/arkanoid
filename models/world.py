from random import randrange

import pygame

from .paddle import Paddle
from .ball import Ball
from .block import Block


class World(object):
    def __init__(self, width: int = 1200, height: int = 800, fps: int = 60):
        self.width = width
        self.height = height
        self.fps = fps

        self.surface = pygame.display.set_mode((self.width, self.height))
        self.paddle = None
        self.paddle_color = None
        self.balls = []
        self.blocks = []

    def add_paddle(self, paddle):
        self.paddle = paddle.create(world=self)

    def add_ball(self, ball):
        self.balls.append(ball.create(world=self))

    def add_blocks(self, block):
        self.blocks = [block.create(col=i, row=j) for i in range(10) for j in range(4)]

    def move_balls(self):
        for ball in self.balls:
            ball.move()
            ball.collision_world(world=self)
            ball.collision_paddle(paddle=self.paddle.instance)

    def draw_objects(self):
        # draw paddle
        self.paddle.draw(surface=self.surface)

        # draw balls
        for ball in self.balls:
            ball.draw(surface=self.surface)

        # draw blocks
        for block in self.blocks:
            block.draw(surface=self.surface)
