'''Example Value Objects.'''
from dataclasses import dataclass
from typing import List

@dataclass
class ExampleVO:
    '''Class for keeping example information.'''
    example_str: str
    example_int: int
    example_list: List
