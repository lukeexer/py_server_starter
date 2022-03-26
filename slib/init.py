# pylint: disable=R0903
'''Initialize all configurations when program start running.'''
from slib.banner import SBanner
from slib.config import SConfig
from slib.log import SLog
from slib.log import SLogLevel

class SInit():
    '''Initialize all configurations in slib when program start running.'''

    @staticmethod
    def init():
        '''Initialize all configurations when program start running.'''
        SBanner.show_banner()

        SLog.init()
        SConfig.init()

        SLog.set_level(SLogLevel.DEBUG)

        SLog.debug('All Configurations:')
        pairs = SConfig.get_all_key_and_value_pairs()
        for key, val in pairs:
            SLog.debug(f'{key} = {val}')
