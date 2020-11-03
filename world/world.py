from typing import Optional, List

import pygame

from defaults import WorldConfig, Controls
from handlers import PaddleHandler, BallHandler, BlockHandler, ScoreHandler
from world.surface import Surface
from objects import Paddle, Ball, Block


class World(object):
    def __init__(self, **kwargs) -> None:
        pygame.init()
        self.pause = False
        self._status = 'active'

        self.paddle_handler = PaddleHandler()
        self.ball_handler = BallHandler()
        self.block_handler = BlockHandler()
        self.score_handler = ScoreHandler()

        self.width = WorldConfig.width
        self.height = WorldConfig.height

        self.surface = Surface(**kwargs)

        self.add_paddle()

    def run(self) -> None:
        self.event_handler()
        self.key_handler()

        if not self.pause:
            self.collision_handler()
            self.draw_objects()
            self.move_balls()

    @property
    def status(self) -> Optional[str]:
        if not self.any_block_left():
            self._status = 'win'

        if self._status == 'active':
            return None

        elif self._status == 'fail' and not self.score_handler.any_lives_left():
            return 'gameover'

        return self._status

    def event_handler(self) -> None:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == Controls.pause:
                    self.pause = not self.pause

    def key_handler(self) -> None:
        key = pygame.key.get_pressed()

        if key[Controls.move_left]:
            if not self.pause:
                self.paddle_handler.move_left()

        if key[Controls.move_right]:
            if not self.pause:
                self.paddle_handler.move_right()

    def collision_handler(self) -> None:

        if self.ball_handler.world_collision():
            self.score_handler.decrease_lives()
            self._status = 'fail'

        if self.ball_handler.blocks_collision(self.block_handler.blocks):
            self.score_handler.increase_score()

        self.ball_handler.paddle_collision(self.paddle_handler.paddle)

    def add_paddle(self) -> None:
        new_paddle = Paddle.create()
        self.paddle_handler.register(new_paddle)

    def add_ball(self) -> None:
        new_ball = Ball.create()
        self.ball_handler.register(new_ball)

    def add_blocks(self, level: List[str]) -> None:

        for row in range(len(level)):
            for col in range(len(level[row])):
                block_level = int(level[row][col])

                if block_level:
                    new_block = Block.create(col=col, row=row, level=block_level)
                    self.block_handler.register(new_block)

    def move_balls(self) -> None:
        self.ball_handler.move()

    def draw_objects(self) -> None:
        self.surface.draw_background()

        self.surface.draw(handler=self.paddle_handler)
        self.surface.draw(handler=self.ball_handler)
        self.surface.draw(handler=self.block_handler)
        self.surface.draw(handler=self.score_handler)

        self.surface.flip()

    def init_level(self, level: list) -> None:
        self.add_blocks(level=level)

    def init_ball(self) -> None:
        self._status = 'active'
        self.ball_handler.clear()
        self.add_ball()

    def any_block_left(self) -> bool:
        return bool(len(self.block_handler.blocks))
