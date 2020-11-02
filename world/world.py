import pygame

from world.surface import Surface
from models.objects import *


class World(object):
    def __init__(self, width: int = 800, height: int = 600, **kwargs):
        pygame.init()

        self.width = width
        self.height = height

        self.fps = kwargs.get('fps') or 60

        self.clock = pygame.time.Clock()
        self.surface = Surface(width=self.width, height=self.height)

        self.paddle = None
        self.balls = []
        self.blocks = []

    @staticmethod
    def event_handler():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def key_handler(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.paddle.move_left()
        if key[pygame.K_RIGHT]:
            self.paddle.move_right()

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

        pygame.display.flip()
        self.clock.tick(self.fps)

    def init(self, level: int = 1) -> None:
        if self.paddle is None:
            self.add_paddle()
        if self.balls:
            self.clear_balls()
        if self.blocks:
            self.clear_blocks()

        if level == 1:
            self.add_ball()
            self.add_blocks()
