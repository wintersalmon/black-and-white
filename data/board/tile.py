'''
BLACK-AND-WHITE
WinterSalmon
Class Name
'''

from data.board.block import WhiteBlock, GrayBlock, BlackBlock

class Tile():
    '''
    Class Description
    '''
    def __init__(self):
        self.blocks = list()

    def get_block(self, pos):
        '''
        Method Description
        '''
        # Todo figure out how to handle index out of range errors
        # if pos < 0 or pos >= len(self.blocks):
        #     raise IndexError
        return self.blocks[pos]

    def get_block_count(self):
        '''
        Method Description
        '''
        return len(self.blocks)

class TileWW(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(WhiteBlock())
        self.blocks.append(WhiteBlock())

class TileWG(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(WhiteBlock())
        self.blocks.append(GrayBlock())

class TileWB(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(WhiteBlock())
        self.blocks.append(BlackBlock())

class TileGB(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(GrayBlock())
        self.blocks.append(BlackBlock())
