import pygame
from random import randrange as rnd

from models.world import World
from models.paddle import Paddle
from models.ball import Ball
from models.block import Block


def main_loop():
    pygame.init()

    world = World()
    world.add_paddle(Paddle)
    world.add_ball(Ball)
    world.add_blocks(Block)

    # background image
    # img = pygame.image.load('1.jpg').convert()

    clock = pygame.time.Clock()

    while True:
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # background image
        # sc.blit(img, (0, 0))
        world.surface.fill('black')

        # draw objects
        world.draw_objects()

        # move ball
        world.move_balls()

        # key handler
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and world.paddle.instance.left > 0:
            world.paddle.move_left()
        if key[pygame.K_RIGHT] and world.paddle.instance.right < world.width:
            world.paddle.move_right()

        # update screen
        pygame.display.flip()
        clock.tick(world.fps)


if __name__ == '__main__':
    main_loop()
