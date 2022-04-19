# pylint: disable=R0903
'''Example service.'''

class ExampleService():
    '''Example service class.'''

    def __init__(self, example_repo):
        '''Initialize example service.'''

        self.example_repo = example_repo

    def get_message(self, key):
        '''Get example message.'''

        example_str = self.example_repo.get_example_data(key)

        return example_str
