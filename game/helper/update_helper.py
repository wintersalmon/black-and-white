'''
BLACK-AND-WHITE
WinterSalmon
UpdateHelper
'''

class UpdateHelper():
    '''
    Interface used to help User update target variables
    Need to call set_target(target) to use helper
    Need to call save() to confirm and save changes
    '''
    def set_target(self, target):
        '''
        set item
        '''
        raise NotImplementedError('You need to implement set_target')

    def can_save_target(self):
        '''
        returns True if Change made to target can be saved
        '''
        raise NotImplementedError('You need to implement can_save_target')

    def save_target(self):
        '''
        Save change made to target
        '''
        raise NotImplementedError('You need to implement save_target')
