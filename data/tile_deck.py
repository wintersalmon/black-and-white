'''
BLACK-AND-WHITE
WinterSalmon
Contains TileDeck
'''

import random

from data.board.tile import TileWW, TileWG, TileWB, TileGB


class TileDeck():
    '''
    TileDeck
    '''
    def __init__(self):
        self.tiles = list()
        self.start_count = dict()
        self.__set_start_count()
        self.__reset_deck()
        self.shuffle()


    def __set_start_count(self, count_ww=12, count_wg=12, count_wb=6, count_gb=6):
        '''
        set default start count
        '''
        self.start_count['WW'] = count_ww
        self.start_count['WG'] = count_wg
        self.start_count['WB'] = count_wb
        self.start_count['GB'] = count_gb


    def __reset_deck(self):
        '''
        reset deck content with preseted start count
        '''
        for _ in range(self.start_count['WW']):
            self.tiles.append(TileWW())

        for _ in range(self.start_count['WG']):
            self.tiles.append(TileWG())

        for _ in range(self.start_count['WB']):
            self.tiles.append(TileWB())

        for _ in range(self.start_count['GB']):
            self.tiles.append(TileGB())


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
        return self.tiles.pop()
