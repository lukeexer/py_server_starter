# pylint: disable=W0603
'''Configuration Share Library.'''
import configparser

SCONFIG_DEFAULT_CONFIG_FILE_NAME = 'conf.ini'
SCONFIG_DEFAULT_SECTION = 'CONFIG'
SCONFIG_CONFIG_FILE = None

class ConfigNotFound(Exception):
    '''Raised when config not found.'''

class ConfigDataTypeNotMatch(Exception):
    '''Raised when config data type not match.'''

class SConfig():
    '''Access default config file.'''

    @staticmethod
    def init(file=None):
        '''Initialize config file.'''

        global SCONFIG_CONFIG_FILE

        conf = configparser.ConfigParser()

        if file is None:
            conf.read(SCONFIG_DEFAULT_CONFIG_FILE_NAME)
        else:
            conf.read(file)

        SCONFIG_CONFIG_FILE = conf

    @staticmethod
    def get_str_conf(key):
        '''Get config with key.'''

        ret_val = None

        try:
            ret_val = SCONFIG_CONFIG_FILE[SCONFIG_DEFAULT_SECTION][key]
        except KeyError:
            raise ConfigNotFound('Config was not found with the incorrect key name.') from KeyError

        return ret_val

    @staticmethod
    def get_int_conf(key):
        '''Get integer config with key.'''

        val = SConfig.get_str_conf(key)
        try:
            val = int(val)
        except ValueError:
            raise ConfigDataTypeNotMatch('Incorrect config data type.') from ValueError

        return val

    @staticmethod
    def get_all_keys():
        '''Get all keys'''

        keys = []

        for key in SCONFIG_CONFIG_FILE[SCONFIG_DEFAULT_SECTION]:
            keys.append(key)

        return keys

    @staticmethod
    def get_all_key_and_value_pairs():
        '''Get all keys and value pairs'''

        pairs = []

        for key in SCONFIG_CONFIG_FILE[SCONFIG_DEFAULT_SECTION]:
            pairs.append((key, SCONFIG_CONFIG_FILE[SCONFIG_DEFAULT_SECTION][key]))

        return pairs

    @staticmethod
    def is_conf_exist(key):
        '''Check whether the specified config exists or not.'''

        try:
            SCONFIG_CONFIG_FILE[SCONFIG_DEFAULT_SECTION][key]
        except KeyError:
            return False

        return True
