'''
BLACK-AND-WHITE
WinterSalmon
Class Name
'''

from game.board.block import WhiteBlock, GrayBlock, BlackBlock
from game.util.auto_number_enum import AutoNumberEnum

class TILE(AutoNumberEnum):
    '''
    Tile Type Enum
    '''
    NONE = ()
    WW = ()
    WG = ()
    WB = ()
    GB = ()

class Tile():
    '''
    Class Description
    '''
    def __init__(self):
        self.blocks = list()
        self.tile_type = TILE.NONE


    def get_type(self):
        '''
        returns tile type(TILE)
        '''
        return self.tile_type


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
        self.tile_type = TILE.WW

class TileWG(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(WhiteBlock())
        self.blocks.append(GrayBlock())
        self.tile_type = TILE.WG

class TileWB(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(WhiteBlock())
        self.blocks.append(BlackBlock())
        self.tile_type = TILE.WB

class TileGB(Tile):
    '''
    Class Description
    '''
    def __init__(self):
        super().__init__()
        self.blocks.append(GrayBlock())
        self.blocks.append(BlackBlock())
        self.tile_type = TILE.GB
