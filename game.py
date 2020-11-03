from defaults import WorldConfig
from world import World
from world.level import generic_level


def main_loop():
    world = World()

    for difficult in range(2, WorldConfig.max_rows):
        level = generic_level(rows=difficult)
        world.init_level(level=level)
        world.init_ball()

        while True:
            world.run()

            status = world.status
            if status is not None:
                if status == 'win':
                    break
                elif status == 'fail':
                    world.init_ball()
                elif status == 'gameover':
                    exit()
    exit()


if __name__ == '__main__':
    main_loop()
