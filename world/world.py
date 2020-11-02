import pygame

from handlers import PaddleHandler, BallHandler, BlockHandler
from world.surface import Surface
from objects import Paddle, Ball, Block


class World(object):
    def __init__(self, width: int = 800, height: int = 600, **kwargs):
        pygame.init()
        self.paddle_handler = PaddleHandler()
        self.ball_handler = BallHandler()
        self.block_handler = BlockHandler()

        self.width = width
        self.height = height

        self.surface = Surface(
            width=self.width,
            height=self.height,
            **kwargs,
        )

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

    # def add_blocks(self, columns: int = 10, rows: int = 4):
    #     for col in range(columns):
    #         for row in range(rows):
    #             new_block = Block.create(world=self, col=col, row=row)
    #             self.block_handler.register(new_block)

    def add_blocks(self, level: list = []):

        for row in range(len(level)):
            for col in range(len(level[row])):
                block_level = int(level[row][col])

                if block_level:
                    new_block = Block.create(world=self, col=col, row=row, level=block_level)
                    self.block_handler.register(new_block)

    def move_balls(self):
        self.ball_handler.move()

    def draw_objects(self):
        self.surface.draw_background()

        self.surface.draw(handler=self.paddle_handler)
        self.surface.draw(handler=self.ball_handler)
        self.surface.draw(handler=self.block_handler)

        self.surface.flip()

    def init(self, level: list) -> None:
        self.ball_handler.clear()
        self.block_handler.clear()

        self.add_ball()
        self.add_blocks(level=level)

    @property
    def done(self) -> bool:
        if self.block_handler.blocks:
            return False
        return True
