# pylint: disable=R0903
'''Example repository.'''

class ExampleRepo():
    '''Example repository class.'''

    def __init__(self):
        '''Initialize example repository.'''

        self.data = {}
        self.data['default'] = 'default message'
        self.data['message'] = 'example value of key message'

    def get_example_data(self, key):
        '''Get example data.'''

        return self.data[key]
