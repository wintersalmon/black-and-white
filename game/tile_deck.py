'''
BLACK-AND-WHITE
WinterSalmon
Contains TileDeck
'''
import random

from game.board.tile import TileWW, TileWG, TileWB, TileGB


class TileDeck():
    '''
    TileDeck
    '''
    def __init__(self):
        self.tiles = list()
        self.start_tile = dict()
        self.__set_start_tile()
        self.__reset_deck()
        self.shuffle()


    def __set_start_tile(self, *, count_ww=12, count_wg=12, count_wb=6, count_gb=6):
        '''
        set default start count
        '''
        # need better way to express start_tile
        self.start_tile['WW'] = (count_ww, TileWW)
        self.start_tile['WG'] = (count_wg, TileWG)
        self.start_tile['WB'] = (count_wb, TileWB)
        self.start_tile['GB'] = (count_gb, TileGB)


    def __reset_deck(self):
        '''
        reset deck content with preseted start count
        '''
        # need better way to express start_tile
        for count, tile in self.start_tile.values():
            for _ in range(count):
                self.tiles.append(tile())


    def __getitem__(self, key):
        return self.tiles[key]


    def size(self):
        '''
        returns number of tile in deck
        '''
        return len(self.tiles)


    def shuffle(self):
        '''
        shuffle the deck
        '''
        random.shuffle(self.tiles)


    def draw(self):
        '''
        draw tile from deck
        '''
        if self.size() > 0:
            return self.tiles.pop()
        else:
            return None
