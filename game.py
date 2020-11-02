import pygame

from models.world import World


def main_loop():
    pygame.init()

    world = World()
    world.init()

    world.add_ball()
    world.add_blocks()

    while True:
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # draw objects
        world.draw_objects()

        # move ball
        world.move_balls()

        # key handler
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            world.paddle.move_left()
        if key[pygame.K_RIGHT]:
            world.paddle.move_right()


if __name__ == '__main__':
    main_loop()
