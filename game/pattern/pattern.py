'''
BLACK-AND-WHITE
WinterSalmon
Pattern
'''


import copy
from collections import namedtuple


SymbolRule = namedtuple('SymbolRule', ['symbol', 'count'])


class Pattern():
    '''
    Pattern
    '''
    def __init__(self):
        self.symbols = set()
        self.symbol_rule_list = list()
        self.max_length = 0
        self.current_pattern = list()


    def _init_add_symbol_rule(self, symbol, count=1):
        '''
        initialize symbol rule
        '''
        if symbol not in self.symbols:
            symbol_rule = SymbolRule(symbol=symbol, count=count)
            self.symbol_rule_list.append(symbol_rule)
            self.symbols.add(symbol)
            self.max_length += count
            for _ in range(count):
                self.current_pattern.append(symbol)
            return True
        return False


    def is_valid(self):
        '''
        returns True if current current_pattern obey all SymbolRules
        '''
        if self.max_length != self.get_length():
            return False

        for rule in self.symbol_rule_list:
            if rule.symbol not in self.current_pattern:
                return False
            if self.current_pattern.count(rule.symbol) != rule.count:
                return False

        return True


    def clone(self, pattern):
        '''
        clone pattern
        '''
        pattern.symbols = copy.deepcopy(self.symbols)
        pattern.symbol_rule_list = copy.deepcopy(self.symbol_rule_list)
        pattern.max_length = self.max_length
        pattern.current_pattern = copy.deepcopy(self.current_pattern)

        return pattern


    def get_max_length(self):
        '''
        returns max pattern length
        '''
        return self.max_length


    def get_length(self):
        '''
        returns current pattern length
        '''
        return len(self.current_pattern)


    def get_pattern(self):
        '''
        returns current pattern
        '''
        return self.current_pattern


    def get_symbol(self, index):
        '''
        returns symbol at index
        '''
        if 0 <= index < self.get_length():
            return self.current_pattern[index]
        return None


    def set_symbol(self, index, symbol):
        '''
        update symbol at index
        '''
        if 0 <= index < self.get_length():
            if symbol in self.symbols:
                self.current_pattern[index] = symbol
                return True
        return False
