'''Server error code and message enumeration definition.'''
from enum import Enum

class ErrCode(Enum):
    '''Server error code enumeration definition.'''
    INTERNAL_SERVER_ERROR = 'S00004'
    RESOURCE_NOT_FOUND = 'S00003'
    METHOD_NOT_ALLOWED = 'S00002'
    UNKNOWN_ERROR = 'S00001'

class ErrMsg(Enum):
    '''Server error message enumeration definition.'''
    INTERNAL_SERVER_ERROR = 'internal server error'
    RESOURCE_NOT_FOUND = 'resource not found'
    METHOD_NOT_ALLOWED = 'method not allowed'
    UNKNOWN_ERROR = 'unknown error'
