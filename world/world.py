import pygame

from models import *


class World(object):
    def __init__(self, width: int = 800, height: int = 600, fps: int = 60):
        self.width = width
        self.height = height

        self.fps = fps
        self.clock = pygame.time.Clock()

        self.surface = pygame.display.set_mode((self.width, self.height))
        self.paddle = None
        self.paddle_color = None
        self.balls = []
        self.blocks = []

        # background image
        # self.img = pygame.image.load('1.jpg').convert()

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
        # draw background image
        # self.surface.blit(self.img, (0, 0))
        self.surface.fill('black')

        # draw paddle
        self.paddle.draw(surface=self.surface)

        # draw balls
        for ball in self.balls:
            ball.draw(surface=self.surface)

        # draw blocks
        for block in self.blocks:
            block.draw(surface=self.surface)

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
