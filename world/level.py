from random import randrange

from defaults import WorldConfig

BLOCK_MIN_LEVEL = 0
BLOCK_MAX_LEVEL = 3


def generic_level(rows: int = WorldConfig.max_rows, columns: int = WorldConfig.columns):
    level = list()

    for row in range(rows):
        level.append('')

        for col in range(columns):
            level[row] += str(randrange(BLOCK_MIN_LEVEL, BLOCK_MAX_LEVEL))

    return level
