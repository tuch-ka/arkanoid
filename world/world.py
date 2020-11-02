import pygame

from handlers import PaddleHandler, BallHandler, BlockHandler
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

    @staticmethod
    def key_handler():
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            PaddleHandler.move_left()
        if key[pygame.K_RIGHT]:
            PaddleHandler.move_right()

    def collision_handler(self):
        BallHandler.world_collision(world=self)
        BallHandler.paddle_collision(PaddleHandler.paddle.instance)

    def add_paddle(self, **kwargs):
        new_paddle = Paddle.create(world=self, **kwargs)
        PaddleHandler.register(new_paddle)

    def add_ball(self):
        BallHandler.register(Ball.create(world=self))

    def clear_balls(self):
        BallHandler.clear()

    def add_blocks(self, columns: int = 10, rows: int = 4):
        for col in range(columns):
            for row in range(rows):
                new_block = Block.create(world=self, col=col, row=row)
                BlockHandler.register(new_block)

    def clear_blocks(self):
        BlockHandler.clear()

    def move_balls(self):
        BallHandler.move()

    def draw_objects(self):
        self.surface.draw_background()

        self.surface.draw(handler=PaddleHandler)
        self.surface.draw(handler=BallHandler)
        self.surface.draw(handler=BlockHandler)

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
        if BlockHandler.blocks:
            return False
        return True
