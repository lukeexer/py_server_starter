'''Server error code and message enumeration definition.'''
from enum import Enum

class ErrCode(Enum):
    '''Server error code enumeration definition.'''
    INVALID_INPUT = 'I00001'
    UNKNOWN_ERROR = 'S00001'
    METHOD_NOT_ALLOWED = 'S00002'
    RESOURCE_NOT_FOUND = 'S00003'
    INTERNAL_SERVER_ERROR = 'S00004'

class ErrMsg(Enum):
    '''Server error message enumeration definition.'''
    INVALID_INPUT = 'invalid input'
    UNKNOWN_ERROR = 'unknown error'
    METHOD_NOT_ALLOWED = 'method not allowed'
    RESOURCE_NOT_FOUND = 'resource not found'
    INTERNAL_SERVER_ERROR = 'internal server error'
