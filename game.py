from world import World


def main_loop():
    world = World()

    world.init(level=1)
    while True:
        if world.done:
            break
        world.run()


if __name__ == '__main__':
    main_loop()
