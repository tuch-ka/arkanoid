from world import World
from world.level import generic_level


def main_loop():
    world = World()

    for difficult in range(10):
        world.init(level=generic_level(rows=difficult))

        while True:
            if world.done:
                break
            world.run()


if __name__ == '__main__':
    main_loop()
