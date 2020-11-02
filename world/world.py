import pygame

from handlers import PaddleHandler, BallHandler, BlockHandler
from world.surface import Surface
from models.objects import *


class World(object):
    def __init__(self, width: int = 800, height: int = 600, **kwargs):
        pygame.init()
        self.paddle_handler = PaddleHandler()
        self.ball_handler = BallHandler()
        self.block_handler = BlockHandler()

        self.width = width
        self.height = height

        self.fps = kwargs.get('fps') or 60

        self.clock = pygame.time.Clock()
        self.surface = Surface(width=self.width, height=self.height)

        self.add_paddle()

    def run(self):
        self.event_handler()
        self.key_handler()
        self.collision_handler()
        self.draw_objects()
        self.move_balls()

    @staticmethod
    def event_handler():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def key_handler(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.paddle_handler.move_left()

        if key[pygame.K_RIGHT]:
            self.paddle_handler.move_right()

    def collision_handler(self):
        self.ball_handler.world_collision(world=self)
        self.ball_handler.paddle_collision(self.paddle_handler.paddle)
        self.ball_handler.blocks_collision(self.block_handler.blocks)

    def add_paddle(self, **kwargs):
        new_paddle = Paddle.create(world=self, **kwargs)
        self.paddle_handler.register(new_paddle)

    def add_ball(self):
        new_ball = Ball.create(world=self)
        self.ball_handler.register(new_ball)

    def clear_balls(self):
        self.ball_handler.clear()

    def add_blocks(self, columns: int = 10, rows: int = 4):
        for col in range(columns):
            for row in range(rows):
                new_block = Block.create(world=self, col=col, row=row)
                self.block_handler.register(new_block)

    def clear_blocks(self):
        self.block_handler.clear()

    def move_balls(self):
        self.ball_handler.move()

    def draw_objects(self):
        self.surface.draw_background()

        self.surface.draw(handler=self.paddle_handler)
        self.surface.draw(handler=self.ball_handler)
        self.surface.draw(handler=self.block_handler)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def init(self, level: int = 1) -> None:
        self.clear_balls()
        self.clear_blocks()

        if level == 1:
            self.add_ball()
            self.add_blocks()

    @property
    def done(self) -> bool:
        if self.block_handler.blocks:
            return False
        return True
