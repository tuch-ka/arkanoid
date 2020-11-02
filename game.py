from world import World


def main_loop():
    world = World()

    world.init(level=1)

    while True:
        if not world.blocks:
            break

        world.event_handler()
        world.key_handler()
        world.collision_handler()
        world.draw_objects()
        world.move_balls()


if __name__ == '__main__':
    main_loop()
