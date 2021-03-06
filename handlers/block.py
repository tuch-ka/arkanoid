class BlockHandler(object):
    blocks = list()

    def register(self, block):
        self.blocks.append(block)

    def clear(self):
        self.blocks = list()

    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface=surface)
