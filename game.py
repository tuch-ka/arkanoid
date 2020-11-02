from world import World, levels


def main_loop():
    world = World()

    for level in levels:
        world.init(level=level)
        while True:
            if world.done:
                break
            world.run()


if __name__ == '__main__':
    main_loop()
