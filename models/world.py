from random import randrange

import pygame

from .paddle import Paddle
from .ball import Ball


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
