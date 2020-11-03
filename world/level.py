from random import randrange

BLOCK_MIN_LEVEL = 0
BLOCK_MAX_LEVEL = 3


def generic_level(rows: int = 5, columns: int = 10):
    level = list()

    for row in range(rows):
        level.append('')

        for col in range(columns):
            level[row] += str(randrange(BLOCK_MIN_LEVEL, BLOCK_MAX_LEVEL))

    return level
