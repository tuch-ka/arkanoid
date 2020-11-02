class BlockHandler(object):
    blocks = []

    @classmethod
    def register(cls, block):
        cls.blocks.append(block)

    @classmethod
    def clear(cls):
        cls.blocks = []

    @classmethod
    def draw(cls, surface):
        for block in cls.blocks:
            block.draw(surface=surface)
